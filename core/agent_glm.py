"""
GLM Agent - Code polish & best practices specialist
Uses Zhipu AI GLM-4.5 API with Gemini fallback for rate limits
"""

import httpx
import logging
import asyncio
from typing import Dict, Any
from config import API_KEYS, AGENT_ROLES, REQUEST_SETTINGS, DEBUG_MODE, MOCK_RESPONSES
from utils.code_parser import parse_response
from utils.error_handler import retry_with_backoff

class GLMAgent:
    def __init__(self):
        # Primary: GLM API
        self.api_key = API_KEYS['glm']
        self.endpoint = 'https://api.z.ai/api/paas/v4/chat/completions'
        self.model = 'glm-4.5'
        
        # Fallback: Gemini API (when GLM is rate limited)
        self.gemini_key = API_KEYS['gemini']
        self.gemini_endpoint = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent'
        
        self.role = AGENT_ROLES['glm']
        self.last_request_time = 0
        self.min_request_interval = 3.0
        self.use_fallback = False  # Switch to Gemini if GLM fails
        
    async def _rate_limit(self):
        current_time = asyncio.get_event_loop().time()
        elapsed = current_time - self.last_request_time
        if elapsed < self.min_request_interval:
            await asyncio.sleep(self.min_request_interval - elapsed)
        self.last_request_time = asyncio.get_event_loop().time()
        
    async def _call_glm(self, system_prompt: str, prompt: str) -> dict:
        """Call GLM API"""
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
                    'max_tokens': REQUEST_SETTINGS['max_tokens'],
                    'temperature': self.role['temperature']
                }
            )
            response.raise_for_status()
            data = response.json()
            return data['choices'][0]['message']['content']
            
    async def _call_gemini(self, system_prompt: str, prompt: str) -> str:
        """Call Gemini API as fallback"""
        url = f"{self.gemini_endpoint}?key={self.gemini_key}"
        async with httpx.AsyncClient(timeout=REQUEST_SETTINGS['timeout']) as client:
            response = await client.post(
                url,
                json={
                    'contents': [{
                        'parts': [{'text': f"{system_prompt}\n\n{prompt}"}]
                    }],
                    'generationConfig': {
                        'temperature': self.role['temperature'],
                        'maxOutputTokens': REQUEST_SETTINGS['max_tokens']
                    }
                }
            )
            response.raise_for_status()
            data = response.json()
            return data['candidates'][0]['content']['parts'][0]['text']

    @retry_with_backoff(retries=REQUEST_SETTINGS['max_retries'])
    async def generate(self, prompt: str) -> Dict[str, Any]:
        """Polish code to perfection"""
        if DEBUG_MODE:
            await asyncio.sleep(0.5)
            content = MOCK_RESPONSES['jules']['polish']
            parsed = parse_response(content)
            return {
                'code': parsed['code'],
                'explanation': parsed['explanation'],
                'documentation': parsed['documentation'],
                'metadata': {'agent': self.role['name'], 'tokens': 150, 'model': self.model}
            }
            
        await self._rate_limit()
        
        system_prompt = f"""You are {self.role['name']}, a {self.role['role']}. Your priority: {self.role['priority']}. Polish code to production-grade quality. Apply PEP 8 style, clear naming, type annotations, proper structure, consistent formatting, organized imports, focused functions, robust error handling, input validation, defensive programming, and resource cleanup. Deliver production-ready code. CRITICAL RULES: - Output ONLY ONE single Python file - NO explanations, NO documentation text - NO markdown code blocks (no ```)
        - Just the final polished raw Python code
        - Keep ALL code in ONE single file
        - Do NOT create multiple files or suggest file structure"""

        try:
            if not self.use_fallback:
                content = await self._call_glm(system_prompt, prompt)
                model_used = self.model
            else:
                content = await self._call_gemini(system_prompt, prompt)
                model_used = 'gemini-2.5-flash (fallback)'
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                logging.warning("GLM rate limited, switching to Gemini fallback")
                self.use_fallback = True
                content = await self._call_gemini(system_prompt, prompt)
                model_used = 'gemini-2.5-flash (fallback)'
            else:
                raise
                
        parsed = parse_response(content)
        
        return {
            'code': parsed['code'],
            'explanation': parsed['explanation'],
            'documentation': parsed['documentation'],
            'metadata': {
                'agent': self.role['name'],
                'tokens': 0,
                'model': model_used
            }
        }

    @retry_with_backoff(retries=REQUEST_SETTINGS['max_retries'])
    async def analyze(self, prompt: str) -> Dict[str, Any]:
        """Analyze code for upgrades"""
        if DEBUG_MODE:
            await asyncio.sleep(0.5)
            mock_data = MOCK_RESPONSES['jules']['upgrade']
            return {
                'suggestions': mock_data['suggestions'],
                'analysis': mock_data['analysis'],
                'metadata': {'agent': self.role['name'], 'tokens': 70, 'model': self.model}
            }
            
        await self._rate_limit()
        
        system_prompt = f"You are {self.role['name']}. Analyze code for quality and best practices."

        try:
            if not self.use_fallback:
                content = await self._call_glm(system_prompt, prompt)
            else:
                content = await self._call_gemini(system_prompt, prompt)
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                logging.warning("GLM rate limited, switching to Gemini fallback")
                self.use_fallback = True
                content = await self._call_gemini(system_prompt, prompt)
            else:
                raise
                
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
