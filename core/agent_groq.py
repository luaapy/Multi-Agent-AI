"""
Groq Agent - Fast code generation specialist
"""

import httpx
import logging
import asyncio
from typing import Dict, Any
from config import API_KEYS, API_ENDPOINTS, MODELS, AGENT_ROLES, REQUEST_SETTINGS, DEBUG_MODE, MOCK_RESPONSES
from utils.code_parser import parse_response
from utils.error_handler import retry_with_backoff

class GroqAgent:
    def __init__(self):
        self.api_key = API_KEYS['groq']
        self.endpoint = API_ENDPOINTS['groq']
        self.model = MODELS['groq']
        self.role = AGENT_ROLES['groq']
        
    @retry_with_backoff(retries=REQUEST_SETTINGS['max_retries'])
    async def generate(self, prompt: str) -> Dict[str, Any]:
        """
        Generate code draft (fast)
        """
        if DEBUG_MODE:
            await asyncio.sleep(0.5)
            content = MOCK_RESPONSES['groq']['draft']
            parsed = parse_response(content)
            return {
                'code': parsed['code'],
                'explanation': parsed['explanation'],
                'language': parsed['language'],
                'metadata': {
                    'agent': self.role['name'],
                    'tokens': 100, # Mock token count
                    'model': self.model
                }
            }

        system_prompt = f"""You are {self.role['name']}, a {self.role['role']}. Your priority: {self.role['priority']}. Generate functional code rapidly prioritizing speed and core functionality. Focus on immediate execution capability using modern syntax patterns with minimal setup overhead. Implement essential features first avoiding unnecessary complexity or over-engineering. Use proven libraries and straightforward approaches ensuring code runs immediately without extensive configuration. Include basic error handling for critical paths only focusing on must-have validations. Leverage latest language features and idiomatic patterns for concise readable implementation. Optimize for quick iteration and fast prototyping rather than premature optimization. Structure code modularly allowing easy extension and modification. Ensure cross-platform compatibility especially mobile environments like Termux. Minimize dependencies using lightweight standard library solutions where possible. Provide working draft that can be refined later prioritizing functionality over perfection. Output clean executable code with brief explanation of core logic and key design decisions.
        
        CRITICAL RULES:
        - Output ONLY ONE single Python file
        - NO explanations, NO documentation text
        - NO markdown code blocks (no ```)
        - Just the final polished raw Python code
        - Keep ALL code in ONE single file
        - Do NOT create multiple files or suggest file structure
        
        Polish requirements:
        - PEP 8 compliant formatting
        - Clear variable and function names
        - Type hints where appropriate
        - Docstrings for functions
        - Proper error handling
        - Production-ready quality
        
        Output only the polished code, nothing else"""

        async with httpx.AsyncClient(timeout=REQUEST_SETTINGS['timeout']) as client:
            response = await client.post(
                self.endpoint,
                headers={
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                },
                json={
                    'model': self.model,
                    'messages': [
                        {'role': 'system', 'content': system_prompt},
                        {'role': 'user', 'content': prompt}
                    ],
                    'temperature': self.role['temperature'],
                    'max_tokens': REQUEST_SETTINGS['max_tokens']
                }
            )
            response.raise_for_status()
            
            data = response.json()
            content = data['choices'][0]['message']['content']
            parsed = parse_response(content)
            
            return {
                'code': parsed['code'],
                'explanation': parsed['explanation'],
                'language': parsed['language'],
                'metadata': {
                    'agent': self.role['name'],
                    'tokens': data['usage']['total_tokens'],
                    'model': self.model
                }
            }

    @retry_with_backoff(retries=REQUEST_SETTINGS['max_retries'])
    async def analyze(self, prompt: str) -> Dict[str, Any]:
        """
        Analyze code for upgrades
        """
        if DEBUG_MODE:
            await asyncio.sleep(0.5)
            mock_data = MOCK_RESPONSES['groq']['upgrade']
            return {
                'suggestions': mock_data['suggestions'],
                'analysis': mock_data['analysis'],
                'metadata': {
                    'agent': self.role['name'],
                    'tokens': 50,
                    'model': self.model
                }
            }

        # Similar implementation for analyze, just returning structure expected by upgrade flow
        system_prompt = f"You are {self.role['name']}. Analyze code for security and modernization."
        
        async with httpx.AsyncClient(timeout=REQUEST_SETTINGS['timeout']) as client:
            response = await client.post(
                self.endpoint,
                headers={
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                },
                json={
                    'model': self.model,
                    'messages': [
                        {'role': 'system', 'content': system_prompt},
                        {'role': 'user', 'content': prompt}
                    ],
                    'temperature': self.role['temperature'],
                    'max_tokens': REQUEST_SETTINGS['max_tokens']
                }
            )
            response.raise_for_status()
            content = response.json()['choices'][0]['message']['content']
            parsed = parse_response(content)
            
            return {
                'suggestions': parsed['improvements'],
                'analysis': parsed['explanation'],
                'metadata': {
                    'agent': self.role['name'],
                    'tokens': response.json()['usage']['total_tokens'],
                    'model': self.model
                }
            }
