from mcp.server.fastmcp import FastMCP


def register_prompts(mcp: FastMCP) -> None:
    """Register all prompts with the provided MCP server instance."""
    @mcp.prompt(
        name="template_prompt",
        description="A template prompt that uses the provided arguments.",
    )
    async def template_prompt(arg1: str, arg2: str):
        """A template prompt that uses the provided arguments."""
        system_message = "This is a system message"
        user_message = f"Hello {arg1}, how are you?"
        assistant_message = f"I'm fine {arg2}."
        """This is a prompt"""
        return f"{system_message}\n{user_message}\n{assistant_message}"
