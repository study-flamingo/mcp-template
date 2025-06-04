from mcp.server.fastmcp import FastMCP


def register_tools(mcp: FastMCP) -> None:
    """Register all tools with the provided MCP server instance."""
    
    # Tool definitions
    @mcp.tool(
        name="hello_world",
        description="Will the world say hello back?",
    )
    async def template_tool(arg1: str, arg2: float, arg3: bool):
        """A simple tool that greets the world with provided arguments."""
        return(f"Hello world: {arg1},{arg2},{arg3}")
