from fastmcp.server import FastMCP
from fastmcp.prompts import Message, PromptMessage
from typing import Literal, Optional
from pydantic import Field

def register_prompts(mcp: FastMCP) -> None:
    """Register all prompts with the provided MCP server instance."""
    @mcp.prompt(
        name="template_prompt",
        description="A prompt that uses the provided arguments.",
    )
    def template_prompt(
        arg1: str = Field(description="First argument for the template prompt."),
        arg2: str = Field(description="Second argument for the template prompt. Optional.", default="PAL")
        ) -> list[PromptMessage | str]:
        """A prompt that uses the provided arguments."""
        user_message: PromptMessage = Message(f"Hello {arg1}, how are you?", role="user")
        assistant_message: PromptMessage = Message(f"I'm fine {arg2}.")
        return [user_message, assistant_message]
