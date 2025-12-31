"""
Utility for parsing code from AI responses
"""
import re
from typing import Dict

def parse_response(content: str) -> Dict[str, str]:
    """
    Extract code blocks and explanation from response
    
    Returns:
        {
            'code': str,
            'language': str,
            'explanation': str,
            'documentation': str (optional),
            'improvements': list (optional)
        }
    """
    # Pattern to find ```language\ncode\n``` blocks
    # We use non-greedy matching (.*?) to handle multiple blocks if needed,
    # but primarily we want the first main block.
    code_pattern = r'```(\w+)?\n(.*?)```'
    matches = re.findall(code_pattern, content, re.DOTALL)
    
    if matches:
        language = matches[0][0] or 'python'
        code = matches[0][1].strip()
    else:
        # No code block found, assume entire response is code if it looks like code,
        # otherwise treat as explanation.
        # For safety, let's look for common code indicators or just treat it as code
        # if the agent was explicitly asked for code.
        # Here we default to empty code if no block found to avoid executing random text.
        code = ""
        if "def " in content or "import " in content:
             code = content.strip()
        language = 'python'
    
    # Extract explanation (text outside code blocks)
    explanation = re.sub(code_pattern, '', content, flags=re.DOTALL).strip()
    
    # Extract documentation (simple heuristic)
    documentation = []
    doc_keywords = ['documentation:', 'docstring:', 'comments:']
    for keyword in doc_keywords:
        if keyword in content.lower():
            try:
                start = content.lower().index(keyword)
                # Take everything until double newline
                doc_text = content[start:].split('\n\n')[0]
                documentation.append(doc_text)
            except ValueError:
                continue

    # Extract improvements (bullet points)
    improvement_pattern = r'(?:^|\n)[\d\-\*]\s*(.+?)(?=\n[\d\-\*]|\n\n|$)'
    improvements = re.findall(improvement_pattern, content, re.MULTILINE)
    
    return {
        'code': code,
        'language': language,
        'explanation': explanation,
        'documentation': '\n'.join(documentation),
        'improvements': improvements
    }
