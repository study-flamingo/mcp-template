from fastmcp.server import FastMCP


def register_resources(mcp: FastMCP) -> None:
    """Register all resources with the provided MCP server instance."""
    
    # Resource definitions
    @mcp.resource(
        uri="resource://template",
        name="my_resource",
        description="A template resource for demonstration purposes.",
        mime_type="text/plain",
    )
    async def template_resource():
        return "Hello world!"
