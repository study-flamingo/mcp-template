from .config import initialize_fastmcp_server
from .tools import register_tools
# from .prompts import register_prompts
from .resources import register_resources
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

mcp = initialize_fastmcp_server()

try:
    register_tools(mcp)
except Exception as e:
    logger.error(f"Failed to register tools: {e}")
    raise
logger.info("Tools registered successfully.")

try:
    register_resources(mcp)
except Exception as e:
    logger.error(f"Error during tool registration: {e}")
    raise
logger.info("Resources registered successfully.")

# try:
    # register_prompts(mcp)
# except Exception as e:
#     logger.error(f"Failed to register resources: {e}")
#     raise
# logger.info("Prompts registered successfully.")


if __name__ == "__main__":
    mcp.run()