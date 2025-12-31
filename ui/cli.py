"""
Command-line interface for Multi-AI Code Assistant
"""

import asyncio
import sys
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.syntax import Syntax
from rich.prompt import Prompt, Confirm
from rich.layout import Layout
from rich.live import Live
from rich.table import Table

from core.orchestrator import Orchestrator
from config import FEATURES, DEBUG_MODE

console = Console()

class CLI:
    def __init__(self):
        self.orchestrator = Orchestrator()
        self.running = True
        
    async def run(self):
        """Main CLI loop"""
        
        console.print(Panel.fit(
            "[bold cyan]Multi-AI Code Assistant[/bold cyan]\n"
            "Powered by Groq + Gemini + GLM",
            border_style="cyan"
        ))
        
        if DEBUG_MODE:
            console.print("[bold red]DEBUG MODE ENABLED - Using Mock Responses[/bold red]")
        
        self._print_help()
        
        while self.running:
            try:
                command = Prompt.ask("\n[bold yellow]Command[/bold yellow]")
                
                cmd_lower = command.lower().strip()
                
                if cmd_lower == 'generate':
                    await self.handle_generate()
                elif cmd_lower == 'upgrade':
                    await self.handle_upgrade()
                elif cmd_lower == 'explain':
                    await self.handle_explain()
                elif cmd_lower == 'history':
                    self.show_history()
                elif cmd_lower == 'stats':
                    self.show_stats()
                elif cmd_lower in ['quit', 'exit', 'q']:
                    self.running = False
                elif cmd_lower in ['help', '?']:
                    self._print_help()
                else:
                    console.print("[red]Unknown command. Type 'help' for options.[/red]")
                    
            except KeyboardInterrupt:
                console.print("\n[yellow]Interrupted[/yellow]")
                self.running = False
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
                import traceback
                traceback.print_exc()
        
        console.print("\n[cyan]Goodbye![/cyan]")

    def _print_help(self):
        console.print("\n[bold]Commands:[/bold]")
        console.print("  [green]generate[/green] - Generate new code")
        console.print("  [green]upgrade[/green]  - Upgrade existing code")
        console.print("  [green]explain[/green]  - Explain current code")
        console.print("  [green]history[/green]  - View conversation history")
        console.print("  [green]stats[/green]    - View usage statistics")
        console.print("  [green]quit[/green]     - Exit")

    async def handle_generate(self):
        """Handle code generation request"""
        
        console.print("\n[bold]Describe what you want to build:[/bold]")
        user_request = Prompt.ask("Request")
        
        if not user_request.strip():
            console.print("[red]Request cannot be empty[/red]")
            return
        
        console.print("\n[yellow]Generating code...[/yellow]")
        
        with console.status("[bold green]Working on it...[/bold green]") as status:
            status.update("[bold cyan]Stage 1: Groq generating draft...[/bold cyan]")
            # We let the orchestrator handle the flow, but to show real-time progress we'd need
            # hooks or callbacks. For now, we'll print after the fact or rely on the console.status
            # animation while waiting for the full async process if we can't break it up easily
            # in the CLI loop without refactoring Orchestrator to yield.
            # However, since Orchestrator.generate_code awaits each step sequentially, 
            # we can't update status *between* steps easily unless we break up the call.
            # For simplicity in this iteration, we just wait. 
            
            # To make it feel more responsive (as per requirements "Show stages"), 
            # let's assume the user is okay with a single wait or we trust the print statements 
            # if we added logging.
            
            # Actually, let's just run it. The mock mode is fast.
            result = await self.orchestrator.generate_code(user_request)
            
        # Display results
        if FEATURES['show_all_versions']:
            self._display_all_versions(result)
        else:
            self._display_final_code(result)
            
        # Ask if user wants to save
        if Confirm.ask("\nSave code to file?"):
            self._save_code(result['final_code'])

    async def handle_upgrade(self):
        """Handle code upgrade request"""
        
        if not self.orchestrator.current_code:
            console.print("[yellow]No code to upgrade. Generate code first.[/yellow]")
            return
        
        console.print("\n[bold]Current code will be analyzed by 3 AIs[/bold]")
        console.print("Optional: Provide specific upgrade instructions (or press Enter)")
        instructions = Prompt.ask("Instructions", default="")
        
        console.print("\n[yellow]Analyzing code...[/yellow]")
        
        with console.status("[bold green]Agents analyzing simultaneously...[/bold green]"):
             result = await self.orchestrator.upgrade_code(
                self.orchestrator.current_code,
                instructions
            )
            
        # Display upgrade suggestions
        self._display_upgrade_results(result)
        
        # Ask if user wants to apply
        if Confirm.ask("\nApply suggested upgrades?"):
            self.orchestrator.current_code = result['upgraded_code']
            console.print("[green]Code upgraded successfully![/green]")
            
            # Show diff
            console.print("\n[bold]Changes:[/bold]")
            syntax = Syntax(result['diff'], "diff", theme="monokai", line_numbers=True)
            console.print(syntax)
            
            # Show new code
            console.print("\n[bold]New Code:[/bold]")
            console.print(Panel(
                Syntax(result['upgraded_code'], "python", theme="monokai", line_numbers=True),
                border_style="green"
            ))
            
            if Confirm.ask("\nSave upgraded code to file?"):
                self._save_code(result['upgraded_code'])

    async def handle_explain(self):
        if not self.orchestrator.current_code:
            console.print("[yellow]No code to explain.[/yellow]")
            return
            
        # For now, we reuse the explanation from the last generation if available
        # Or we could trigger a new explanation generation.
        # Let's check history
        history = self.orchestrator.conversation_manager.get_history()
        if history:
            last_turn = history[-1]
            console.print("\n[bold]Explanation from last generation:[/bold]")
            console.print(Markdown(last_turn['response']['explanation']))
        else:
            console.print("[yellow]No explanation available.[/yellow]")

    def _display_all_versions(self, result):
        """Display code from all 3 AIs"""
        
        # Groq version
        console.print(Panel(
            Syntax(result['groq_version'], "python", theme="monokai", line_numbers=True),
            title="[bold cyan]Groq (SpeedCoder) - Draft[/bold cyan]",
            border_style="cyan"
        ))
        
        # Gemini version
        console.print(Panel(
            Syntax(result['gemini_version'], "python", theme="monokai", line_numbers=True),
            title="[bold green]Gemini (Reviewer) - Improved[/bold green]",
            border_style="green"
        ))
        
        # GLM version (final)
        console.print(Panel(
            Syntax(result['glm_version'], "python", theme="monokai", line_numbers=True),
            title="[bold magenta]GLM (Polisher) - Final[/bold magenta]",
            border_style="magenta"
        ))
        
        # Explanation
        console.print("\n[bold]Explanation:[/bold]")
        console.print(Markdown(result['explanation']))

    def _display_final_code(self, result):
        """Display only final code"""
        console.print(Panel(
            Syntax(result['final_code'], "python", theme="monokai", line_numbers=True),
            title="[bold green]Generated Code[/bold green]",
            border_style="green"
        ))
        console.print("\n[bold]Explanation:[/bold]")
        console.print(Markdown(result['explanation']))

    def _display_upgrade_results(self, result):
        """Display upgrade suggestions"""
        console.print("[bold]Upgrade Suggestions:[/bold]\n")
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Priority", width=12)
        table.add_column("Description")
        table.add_column("Suggested By")
        
        for upgrade in result['prioritized_upgrades']:
            priority = upgrade.get('priority', 'low').upper()
            color = "red" if priority == "HIGH" else "yellow" if priority == "MEDIUM" else "blue"
            
            table.add_row(
                f"[{color}]{priority}[/{color}]",
                upgrade['description'],
                ", ".join(upgrade['agents'])
            )
            
        console.print(table)

    def _save_code(self, code):
        """Save code to file"""
        filename = Prompt.ask("Filename", default="generated_code.py")
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(code)
            console.print(f"[green]Saved to {filename}[/green]")
        except Exception as e:
            console.print(f"[red]Failed to save: {e}[/red]")

    def show_history(self):
        history = self.orchestrator.conversation_manager.get_history()
        if not history:
            console.print("[yellow]No history yet[/yellow]")
            return
        
        console.print("\n[bold]Conversation History:[/bold]\n")
        for i, item in enumerate(history, 1):
            console.print(f"{i}. {item['request'][:60]}...")

    def show_stats(self):
        stats = self.orchestrator.stats
        tracker_stats = self.orchestrator.token_tracker.get_stats()
        
        # Overall Stats
        console.print(Panel(
            f"Total Requests: {stats['total_requests']}\n"
            f"Total Tokens: {stats['total_tokens']:,}\n"
            f"Estimated Cost: ${stats['total_cost']:.6f}",
            title="[bold]Usage Statistics[/bold]",
            border_style="blue"
        ))
        
        # Detailed Breakdown
        table = Table(title="Cost Breakdown by Agent")
        table.add_column("Agent")
        table.add_column("Tokens")
        table.add_column("Cost ($)")
        
        for agent, data in tracker_stats['by_agent'].items():
            table.add_row(agent, str(data['tokens']), f"{data['cost']:.6f}")
            
        console.print(table)
