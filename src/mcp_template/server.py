from .config import initialize_fastmcp_server
from .tools import register_tools
# from .resources import register_resources
from .prompts import register_prompts
import logging

logging.basicConfig(
    level=logging.INFO,
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

# try:
#     register_resources(mcp)
# except Exception as e:
#     logger.error(f"Failed to register resources: {e}")
#     raise
# logger.debug("Resources registered successfully.")

@mcp.resource("other://input/{input}")
def template_resource(input: str) -> str:
    """A template resource that returns a message based on the input string."""
    response = f"Hello world! {input} - LOL"
    return response

logger.debug("Registered template resource: template_resource")


@mcp.resource("resource://fixed")
def fixed_resource() -> str:
    """A fixed resource that always returns the same content."""
    return "Hello world!"

logger.debug("Registered fixed resource: fixed_resource")

@mcp.resource("time://now")
def current_time() -> str:
    """A fixed resource that always returns the same content."""
    return "The time is 4:20 PM"

logger.debug("Registered fixed resource: current_time")

@mcp.resource("time://later")
def later_time() -> str:
    """A fixed resource that always returns the same content."""
    return "The time is 4:21 PM"

logger.debug("Registered fixed resource: later_time")

    
try:
    register_prompts(mcp)
except Exception as e:
    logger.error(f"Failed to register prompts: {e}")
    raise
logger.debug("Prompts registered successfully.")


if __name__ == "__main__":
    mcp.run()