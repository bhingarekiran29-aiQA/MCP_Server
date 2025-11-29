from mcp.server.fastmcp import FastMCP

mcp = FastMCP("simple-calculator")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Adding two numbers and return the results"""
    return int(a) + int(b)

@mcp.tool()
def sub_numbers(a: int, b: int) -> int:
    """Subtract two numbers and return the results"""
    return int(a) - int(b)

@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers and return the results"""
    return int(a) * int(b)

@mcp.tool()
def divide_numbers(a: int, b: int) -> int:
    """Divide two numbers and return the results"""
    return int(a) / int (b)

if __name__ == "__main__":
    mcp.run()


    """
    Content of cloude_desktop_config: 

    {
        "mcpServers": {
            "simple-calculator": {
            "command": "python",
            "args": ["C:\\Users\\Lenovo\\Downloads\\MCP_Server\\simple-calculator.py"]
            }
        }
    }

    """

    # Question: What is the sum of 50 and 70