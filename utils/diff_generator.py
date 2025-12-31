"""
Utility for generating diffs between code versions
"""
import difflib

def generate_diff(old_code: str, new_code: str) -> str:
    """
    Generate a git-style unified diff
    """
    old_lines = old_code.splitlines(keepends=True)
    new_lines = new_code.splitlines(keepends=True)
    
    diff = difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile='Original',
        tofile='Upgraded',
        n=3
    )
    
    return ''.join(diff)
