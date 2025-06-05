from fastmcp.server import FastMCP
import logging

logger = logging.getLogger(__name__)


def register_resources(mcp: FastMCP) -> None:
    """Register all resources with the provided MCP server instance."""
    
    # Resource definitions
    @mcp.resource("resource://fixed")
    def fixed_resource() -> str:
        """A fixed resource that always returns the same content."""
        return "Hello world!"

    logger.info("Registered fixed resource: my_resource")


    @mcp.resource("other://template/{input}")
    def template_resource(input: str) -> str:
        """A template resource that returns a message based on the input string."""
        response = f"Hello world! {input} - LOL"
        return response

    logger.info("Registered template resource: my_other_resource")
    
    return None