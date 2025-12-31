"""
API Configuration for 3 AI providers
"""
import os

# --- CONFIGURATION FLAGS ---
DEBUG_MODE = False  # Set to False to use real APIs

# API Keys
API_KEYS = {
    'glm': 'YOUR GLM API KEY',
    'gemini': 'AIza........',
    'groq': 'gsk_......'
}

# API Endpoints
API_ENDPOINTS = {
    'groq': 'https://api.groq.com/openai/v1/chat/completions',
    'gemini': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent',
    'glm': 'https://api.z.ai/api/paas/v4/chat/completions'
}

# Model Selection
MODELS = {
    'groq': 'llama-3.3-70b-versatile',  # Fast Llama 3.3 model, good for drafts
    'gemini': 'gemini-2.5-flash',         # Fast Gemini 2.5, good for analysis
    'glm': 'glm-4.5'                      # GLM-4.5 for polish
}

# Agent Roles & Personalities
AGENT_ROLES = {
    'groq': {
        'name': 'SpeedCoder',
        'role': 'Quick draft generator',
        'priority': 'Speed & creativity',
        'temperature': 0.7
    },
    'gemini': {
        'name': 'Reviewer',
        'role': 'Code quality analyst',
        'priority': 'Correctness & optimization',
        'temperature': 0.3
    },
    'glm': {
        'name': 'Polisher',
        'role': 'Best practices expert',
        'priority': 'Clean code & documentation',
        'temperature': 0.5
    }
}

# Request Settings
REQUEST_SETTINGS = {
    'max_tokens': 4000,
    'timeout': 60,  # seconds (increased for slower APIs)
    'max_retries': 3,
    'retry_delay': 5  # seconds (increased for rate limits)
}

# Feature Flags
FEATURES = {
    'show_all_versions': True,      # Show outputs from all 3 AIs
    'enable_consensus': True,        # Only show if 2+ AIs agree
    'enable_voting': True,           # AIs vote on best approach
    'parallel_requests': True,       # Call APIs simultaneously
    'stream_responses': False,       # Stream responses (future)
    'save_history': True,            # Save conversation to file
    'enable_caching': True           # Cache similar requests
}

# Cost Tracking (Estimates)
COST_PER_TOKEN = {
    'groq': 0.0000002,
    'gemini': 0.00000025,
    'glm': 0.00000015  # GLM-4.5 pricing
}

# --- MOCK RESPONSES ---
MOCK_RESPONSES = {
    'groq': {
        'draft': """Here's a quick draft:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

This is a basic recursive implementation.""",
        'upgrade': {
            'suggestions': ['Add memoization for performance', 'Handle negative inputs', 'Add type hints'],
            'analysis': "The code uses simple recursion which is inefficient for large n."
        }
    },
    'gemini': {
        'review': """Improved version with error handling:

```python
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

Added input validation and type checking.""",
        'upgrade': {
            'suggestions': ['Use iterative approach instead of recursion', 'Add docstring', 'Consider using lru_cache'],
            'analysis': "Recursive solution has exponential time complexity. Iterative or memoized is O(n)."
        }
    },
    'deepseek': {
        'polish': """Production-ready version:

```python
from functools import lru_cache
from typing import Union

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    \"\"\"
    Calculate the nth Fibonacci number using memoization.
    
    Args:
        n: Non-negative integer index in Fibonacci sequence
        
    Returns:
        The nth Fibonacci number
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
        
    Example:
        >>> fibonacci(10)
        55
    \"\"\"
    if not isinstance(n, int):
        raise TypeError(f"n must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

Added comprehensive documentation, type hints, and memoization for O(n) performance.""",
        'upgrade': {
            'suggestions': ['Consider iterative implementation for deep recursion', 'Add unit tests', 'Add performance benchmarks'],
            'analysis': "The memoized recursive solution is good, but python has a recursion limit. For extremely large n, iterative is safer."
        }
    }
}
