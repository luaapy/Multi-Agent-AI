"""
Utility for tracking token usage
"""
from typing import Dict

def estimate_tokens(text: str) -> int:
    """
    Estimate token count (approx 4 chars per token)
    Real implementations would use tiktoken or similar
    """
    if not text:
        return 0
    return len(text) // 4

class TokenTracker:
    def __init__(self):
        self.usage = {}  # {agent_name: {'tokens': int, 'cost': float}}
        
    def track(self, agent: str, tokens: int, cost_per_token: float):
        if agent not in self.usage:
            self.usage[agent] = {'tokens': 0, 'cost': 0.0}
            
        self.usage[agent]['tokens'] += tokens
        self.usage[agent]['cost'] += tokens * cost_per_token
        
    def get_stats(self) -> Dict:
        total_tokens = sum(d['tokens'] for d in self.usage.values())
        total_cost = sum(d['cost'] for d in self.usage.values())
        return {
            'by_agent': self.usage,
            'total_tokens': total_tokens,
            'total_cost': total_cost
        }
