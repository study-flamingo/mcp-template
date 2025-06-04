from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

def initialize_fastmcp_server() -> FastMCP:
    """Create and return a configured MCP server instance."""
    load_dotenv()
    
    return FastMCP(
        name="QBO MCP",
        version="1.0.0",
        instructions="This is an MCP server. Use it to...",
    )