"""
Entry point for Multi-AI Code Assistant
"""
import asyncio
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.WARNING, # Only show warnings/errors in console
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(sys.stderr)
    ]
)

from ui.cli import CLI

if __name__ == "__main__":
    cli = CLI()
    try:
        asyncio.run(cli.run())
    except KeyboardInterrupt:
        pass
