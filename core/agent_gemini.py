"""
Gemini Agent - Code quality & optimization specialist
"""

import httpx
import logging
import asyncio
from typing import Dict, Any
from config import API_KEYS, API_ENDPOINTS, MODELS, AGENT_ROLES, REQUEST_SETTINGS, DEBUG_MODE, MOCK_RESPONSES
from utils.code_parser import parse_response
from utils.error_handler import retry_with_backoff

class GeminiAgent:
    def __init__(self):
        self.api_key = API_KEYS['gemini']
        self.endpoint = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent'
        self.model = 'gemini-2.5-flash'
        self.role = AGENT_ROLES['gemini']
        self.last_request_time = 0
        self.min_request_interval = 2.0  # Rate limiting
        
    async def _rate_limit(self):
        current_time = asyncio.get_event_loop().time()
        elapsed = current_time - self.last_request_time
        if elapsed < self.min_request_interval:
            await asyncio.sleep(self.min_request_interval - elapsed)
        self.last_request_time = asyncio.get_event_loop().time()
        
    @retry_with_backoff(retries=REQUEST_SETTINGS['max_retries'])
    async def generate(self, prompt: str) -> Dict[str, Any]:
        """Review & improve code"""
        if DEBUG_MODE:
            await asyncio.sleep(0.5)
            content = MOCK_RESPONSES['gemini']['review']
            parsed = parse_response(content)
            return {
                'code': parsed['code'],
                'explanation': parsed['explanation'],
                'improvements': parsed['improvements'],
                'metadata': {'agent': self.role['name'], 'tokens': 120, 'model': self.model}
            }

        await self._rate_limit()
        
        system_instruction = f"""You are {self.role['name']}, a {self.role['role']}. Your priority: {self.role['priority']}. Analyze code systematically: correctness, performance, security, maintainability, type safety, error handling, edge cases, resource management, best practices. Provide detailed analysis with specific improvements prioritizing critical issues first. Include actionable concrete changes. Output must be thorough and immediately actionable.
        
        CRITICAL RULES:
        - Output ONLY ONE single Python file
        - NO explanations, NO documentation text
        - NO markdown code blocks (no ```)
        - Just the final polished raw Python code
        - Keep ALL code in ONE single file
        - Do NOT create multiple files or suggest file structure"""

        url = f"{self.endpoint}?key={self.api_key}"
        
        async with httpx.AsyncClient(timeout=REQUEST_SETTINGS['timeout']) as client:
            response = await client.post(
                url,
                json={
                    'contents': [{
                        'parts': [{
                            'text': f"{system_instruction}\n\n{prompt}"
                        }]
                    }],
                    'generationConfig': {
                        'temperature': self.role['temperature'],
                        'maxOutputTokens': REQUEST_SETTINGS['max_tokens']
                    }
                }
            )
            response.raise_for_status()
            
            data = response.json()
            try:
                content = data['candidates'][0]['content']['parts'][0]['text']
            except (KeyError, IndexError) as e:
                logging.error(f"Gemini response parsing error: {data}")
                raise e

            parsed = parse_response(content)
            
            return {
                'code': parsed['code'],
                'explanation': parsed['explanation'],
                'improvements': parsed['improvements'],
                'metadata': {
                    'agent': self.role['name'],
                    'tokens': 0,
                    'model': self.model
                }
            }

    @retry_with_backoff(retries=REQUEST_SETTINGS['max_retries'])
    async def analyze(self, prompt: str) -> Dict[str, Any]:
        """Analyze code for upgrades"""
        if DEBUG_MODE:
            await asyncio.sleep(0.5)
            mock_data = MOCK_RESPONSES['gemini']['upgrade']
            return {
                'suggestions': mock_data['suggestions'],
                'analysis': mock_data['analysis'],
                'metadata': {'agent': self.role['name'], 'tokens': 60, 'model': self.model}
            }
            
        await self._rate_limit()
        
        system_instruction = f"You are {self.role['name']}. Analyze code for performance and optimization."
        url = f"{self.endpoint}?key={self.api_key}"
        
        async with httpx.AsyncClient(timeout=REQUEST_SETTINGS['timeout']) as client:
            response = await client.post(
                url,
                json={
                    'contents': [{
                        'parts': [{
                            'text': f"{system_instruction}\n\n{prompt}"
                        }]
                    }],
                    'generationConfig': {
                        'temperature': self.role['temperature'],
                        'maxOutputTokens': REQUEST_SETTINGS['max_tokens']
                    }
                }
            )
            response.raise_for_status()
            data = response.json()
            content = data['candidates'][0]['content']['parts'][0]['text']
            parsed = parse_response(content)
            
            return {
                'suggestions': parsed['improvements'],
                'analysis': parsed['explanation'],
                'metadata': {
                    'agent': self.role['name'],
                    'tokens': 0,
                    'model': self.model
                }
            }
