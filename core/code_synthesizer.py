"""
Combine AI responses
"""
from typing import Dict, List, Any

def synthesize_code(groq_resp: Dict, gemini_resp: Dict, glm_resp: Dict) -> Dict[str, Any]:
    """
    Combine 3 AI outputs into final result
    In the generate flow, GLM is the final polisher, so its code is the final code.
    However, we aggregate metadata and explanations.
    """
    
    # Final code comes from GLM (Step 3)
    final_code = glm_resp.get('code', '')
    
    # Combine explanations
    explanation = f"""
## 1. SpeedCoder (Groq) Draft
{groq_resp.get('explanation', '')}

## 2. Reviewer (Gemini) Analysis
{gemini_resp.get('explanation', '')}

## 3. Polisher (GLM) Final Notes
{glm_resp.get('explanation', '')}
"""

    return {
        'groq_version': groq_resp.get('code', ''),
        'gemini_version': gemini_resp.get('code', ''),
        'glm_version': glm_resp.get('code', ''),
        'final_code': final_code,
        'explanation': explanation,
        'metadata': {
            'tokens': sum([
                groq_resp.get('metadata', {}).get('tokens', 0),
                gemini_resp.get('metadata', {}).get('tokens', 0),
                glm_resp.get('metadata', {}).get('tokens', 0)
            ])
        }
    }

def prioritize_upgrades(responses: List[Dict]) -> List[Dict]:
    """
    Prioritize upgrade suggestions using voting logic
    responses: List of dicts returned by analyze() from each agent
    """
    # Flatten all suggestions
    all_suggestions = []
    
    # Map agent index/name to suggestions
    agent_names = ['Groq', 'Gemini', 'GLM']
    
    for i, resp in enumerate(responses):
        agent_name = agent_names[i]
        suggestions = resp.get('suggestions', [])
        # Handle case where suggestions might be None
        if not suggestions:
            continue
            
        for sugg in suggestions:
            all_suggestions.append({
                'description': sugg,
                'agent': agent_name
            })
            
    # Simple semantic grouping would be hard without an embedding model.
    # For now, we rely on exact string matching or simple consolidation 
    # since we are mocking or getting distinct text.
    # However, to implement the "Voting" logic requested:
    # We will treat each suggestion as unique unless identical.
    # In a real system, we'd use an LLM to deduplicate.
    
    # Let's create a list of unique items with vote counts
    # For the Mock/Simple version, we'll just list them all and assign priorities
    # based on which agent found them or if they overlap (mock overlap).
    
    consolidated = []
    seen = set()
    
    for item in all_suggestions:
        desc = item['description']
        if desc in seen:
            # Find existing and add vote
            for c in consolidated:
                if c['description'] == desc:
                    c['agents'].append(item['agent'])
                    c['votes'] += 1
        else:
            seen.add(desc)
            consolidated.append({
                'description': desc,
                'agents': [item['agent']],
                'votes': 1
            })
            
    # Assign Priority
    for item in consolidated:
        if item['votes'] >= 2:
            item['priority'] = 'high'
        elif item['votes'] == 1:
            # Arbitrary logic for medium vs low
            item['priority'] = 'medium'
            
    # Sort by priority (High > Medium > Low)
    priority_map = {'high': 3, 'medium': 2, 'low': 1}
    consolidated.sort(key=lambda x: priority_map.get(x['priority'], 1), reverse=True)
    
    return consolidated
