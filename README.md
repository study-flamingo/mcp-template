# FastMCP Server Template

This template provides a basic structure for a FastMCP server. It includes examples of how to define and register tools, resources, and prompts.

**Features:**

*   Template tool: `hello_world`
*   Template resource: `resource://template`
*   Template prompt: `template_prompt` (currently commented out)
*   Basic configuration and logging

**Getting Started:**

1.  Install dependencies (assuming `uv` is used):
    ```bash
    uv sync
    ```
2.  Run the server:
    ```bash
    uv run src/mcp_template
    ```

**Customization:**

*   Modify [`config.py`](src/mcp_template/config.py) to change server name, version, and instructions.
*   Add new tools in [`tools.py`](src/mcp_template/tools.py).
*   Add new resources in [`resources.py`](src/mcp_template/resources.py).
*   Add new prompts in [`prompts.py`](src/mcp_template/prompts.py) and uncomment the registration in [`server.py`](src/mcp_template/server.py).