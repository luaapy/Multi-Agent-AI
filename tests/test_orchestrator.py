import pytest
from core.orchestrator import Orchestrator
from config import MOCK_RESPONSES

@pytest.mark.asyncio
async def test_code_generation():
    """Test basic code generation"""
    orchestrator = Orchestrator()
    
    result = await orchestrator.generate_code(
        "Create a function to calculate fibonacci"
    )
    
    assert 'final_code' in result
    assert 'explanation' in result
    # Check if we got the mock response content
    assert "fibonacci" in result['final_code'].lower()

@pytest.mark.asyncio
async def test_code_upgrade():
    """Test code upgrade"""
    orchestrator = Orchestrator()
    
    # Set initial code
    orchestrator.current_code = """
def add(a, b):
    return a + b
"""
    
    result = await orchestrator.upgrade_code(orchestrator.current_code)
    
    assert 'upgraded_code' in result
    assert 'prioritized_upgrades' in result
    # In mock mode, we expect suggestions
    assert len(result['prioritized_upgrades']) > 0
