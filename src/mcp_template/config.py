from fastmcp.server import FastMCP
from dotenv import load_dotenv

def initialize_fastmcp_server() -> FastMCP:
    """Create and return a configured MCP server instance."""
    load_dotenv()
    
    return FastMCP(
        name="MCP Server Template",
        version="1.0.0",
        instructions="This is an MCP server template. Customize me to suit your needs!",
    )