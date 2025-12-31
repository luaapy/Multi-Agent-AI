"""
Main orchestrator that manages 3 AI agents
"""
import asyncio
import logging
from typing import Dict, Any, List

from core.agent_groq import GroqAgent
from core.agent_gemini import GeminiAgent
from core.agent_glm import GLMAgent
from core.conversation_manager import ConversationManager
from core.code_synthesizer import synthesize_code, prioritize_upgrades
from prompts.generation_prompts import get_generation_prompt
from prompts.upgrade_prompts import get_upgrade_prompt
from utils.token_counter import TokenTracker
from utils.diff_generator import generate_diff
from config import FEATURES, COST_PER_TOKEN

class Orchestrator:
    def __init__(self):
        self.groq_agent = GroqAgent()
        self.gemini_agent = GeminiAgent()
        self.glm_agent = GLMAgent()
        
        self.conversation_manager = ConversationManager()
        self.token_tracker = TokenTracker()
        
        self.current_code = None
        
        self.stats = {
            'total_requests': 0,
            'total_tokens': 0,
            'total_cost': 0,
            'response_times': [] # Not fully implemented for mock
        }
        
    async def generate_code(self, user_request: str) -> Dict[str, Any]:
        """
        3-stage code generation process
        """
        # STAGE 1: Groq generates initial draft
        groq_prompt = get_generation_prompt(user_request, stage='draft')
        groq_response = await self.groq_agent.generate(groq_prompt)
        self._track_usage('groq', groq_response)
        
        # STAGE 2: Gemini reviews & improves
        gemini_prompt = get_generation_prompt(
            user_request, 
            stage='review', 
            previous_code=groq_response['code']
        )
        gemini_response = await self.gemini_agent.generate(gemini_prompt)
        self._track_usage('gemini', gemini_response)
        
        # STAGE 3: Jules polishes
        glm_prompt = get_generation_prompt(
            user_request,
            stage='polish',
            previous_code=gemini_response['code']
        )
        glm_response = await self.glm_agent.generate(glm_prompt)
        self._track_usage('glm', glm_response)
        
        # Synthesize
        final_result = synthesize_code(groq_response, gemini_response, glm_response)
        
        # Update State
        self.current_code = final_result['final_code']
        self.conversation_manager.add_turn(user_request, final_result)
        self.stats['total_requests'] += 1
        
        return final_result

    async def upgrade_code(self, existing_code: str, instructions: str = None) -> Dict[str, Any]:
        """
        3-AI parallel code review & upgrade
        """
        base_instructions = instructions or "Improve this code."
        
        prompts = {
            'groq': get_upgrade_prompt(existing_code, focus='security_modernization') + f"\nContext: {base_instructions}",
            'gemini': get_upgrade_prompt(existing_code, focus='performance') + f"\nContext: {base_instructions}",
            'glm': get_upgrade_prompt(existing_code, focus='quality') + f"\nContext: {base_instructions}"
        }
        
        # Parallel Execution
        if FEATURES['parallel_requests']:
            responses = await asyncio.gather(
                self.groq_agent.analyze(prompts['groq']),
                self.gemini_agent.analyze(prompts['gemini']),
                self.glm_agent.analyze(prompts['glm'])
            )
        else:
            responses = [
                await self.groq_agent.analyze(prompts['groq']),
                await self.gemini_agent.analyze(prompts['gemini']),
                await self.glm_agent.analyze(prompts['glm'])
            ]
            
        # Track usage
        self._track_usage('groq', responses[0])
        self._track_usage('gemini', responses[1])
        self._track_usage('glm', responses[2])
        
        # Prioritize
        upgrade_plan = prioritize_upgrades(responses)
        
        # Apply Upgrades (For this version, we simulate application or take the best snippet if available)
        # In a real scenario, we might ask one agent to apply the specific plan.
        # For simplicity/Mock, we assume the 'Jules' analysis result might contain an upgraded version
        # OR we just say "Upgraded code not automatically generated in upgrade-only mode, please use generate with instructions".
        # BUT the requirement says "Apply selected improvements" and "Show before/after comparison".
        
        # Let's do a quick "Apply" step using Jules to apply the plan
        apply_prompt = f"""Apply the following upgrades to the code:
{existing_code}

Upgrades:
{[u['description'] for u in upgrade_plan]}
"""
        # We reuse the generate capability of Jules for this application step
        # Note: This is an extra call not explicitly detailed in the parallel flow diagram but necessary to get 'upgraded_code'
        final_upgrade_response = await self.glm_agent.generate(apply_prompt)
        upgraded_code = final_upgrade_response['code']
        self._track_usage('glm', final_upgrade_response)
        
        diff = generate_diff(existing_code, upgraded_code)
        
        result = {
            'groq_suggestions': responses[0].get('suggestions', []),
            'gemini_suggestions': responses[1].get('suggestions', []),
            'glm_suggestions': responses[2].get('suggestions', []),
            'prioritized_upgrades': upgrade_plan,
            'upgraded_code': upgraded_code,
            'diff': diff
        }
        
        self.stats['total_requests'] += 1
        self.current_code = upgraded_code
        return result

    def _track_usage(self, agent: str, response: Dict):
        tokens = response.get('metadata', {}).get('tokens', 0)
        self.token_tracker.track(agent, tokens, COST_PER_TOKEN[agent])
        self.stats['total_tokens'] += tokens
        # Recalculate total cost from tracker
        self.stats['total_cost'] = self.token_tracker.get_stats()['total_cost']

