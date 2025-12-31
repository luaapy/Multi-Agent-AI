"""
Utility for error handling
"""
import asyncio
import logging
import functools

logger = logging.getLogger(__name__)

def retry_with_backoff(retries=3, delay=1, backoff=2):
    """
    Decorator for async functions to retry on failure
    """
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None
            
            for attempt in range(retries):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1}/{retries} failed for {func.__name__}: {e}")
                    if attempt < retries - 1:
                        await asyncio.sleep(current_delay)
                        current_delay *= backoff
            
            logger.error(f"All {retries} attempts failed for {func.__name__}")
            raise last_exception
        return wrapper
    return decorator
