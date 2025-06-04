import asyncio
from .server import mcp, logger

async def main():
    """Main function to run the FastMCP server."""
    logger.info("Starting FastMCP server...")
    try:
        await mcp.run_async(transport="stdio")
    except Exception as e:
        logger.error(e)

def cli():
    asyncio.run(main())

if __name__ == "__main__":
    cli()