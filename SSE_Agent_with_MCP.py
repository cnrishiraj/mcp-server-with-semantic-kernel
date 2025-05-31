#!/usr/bin/env python3
# MCP server with SSE transport for calculator functions

from mcp.server.fastmcp import FastMCP

# Instantiate an MCP server instance with a name
mcp = FastMCP("CalculatorServerSSE")

# Define a tool function using a decorator
@mcp.tool()
def add_numbers(x: float, y: float) -> float:
    """Add two numbers and return the result."""
    print(f"📝 Calculating: {x} + {y}")
    return x + y

# Additional calculator functions to show extensibility
@mcp.tool()
def subtract_numbers(x: float, y: float) -> float:
    """Subtract the second number from the first number."""
    print(f"📝 Calculating: {x} - {y}")
    return x - y

@mcp.tool()
def multiply_numbers(x: float, y: float) -> float:
    """Multiply two numbers together."""
    print(f"📝 Calculating: {x} * {y}")
    return x * y

@mcp.tool()
def divide_numbers(x: float, y: float) -> float:
    """Divide the first number by the second number."""
    if y == 0:
        error_msg = "Cannot divide by zero"
        print(f"❌ Error: {error_msg}")
        raise ValueError(error_msg)
    print(f"📝 Calculating: {x} / {y}")
    return x / y

if __name__ == "__main__":
    print("┌───────────────────────────────────────┐")
    print("│ MCP Calculator Server (SSE Mode)      │")
    print("└───────────────────────────────────────┘")
    print("Server available at: http://localhost:8000")
    print("Connect to this server from the MCP SSE client agent")
    print("Run the client with: python 05_agent_with_mcp_sse.py")
    print("Press Ctrl+C to exit")
    
    # Run the MCP server with HTTP/SSE transport
    mcp.run(transport="sse")  # This starts an HTTP server with SSE transport 