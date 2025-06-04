import asyncio
import src.template_mcp.server as server

server.logger.info("Starting FastMCP server...")
asyncio.run(server.mcp.run_stdio_async())
