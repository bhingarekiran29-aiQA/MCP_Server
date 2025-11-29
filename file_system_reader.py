import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP

BASE_DIR = Path(os.getenv("FILE_READER_DIRECTORY", "./documents"))

mcp = FastMCP("file-system-reader")


@mcp.tool()
def read_file(filename: str) -> str:
    """Read a file from the document or any given directory."""
    try:
        file_path = BASE_DIR / filename

        # Prevent directory traversal
        if not str(file_path.resolve()).startswith(str(BASE_DIR.resolve())):
            return "Error: Access denied – invalid path"

        content = file_path.read_text(encoding="utf-8")
        return f"File: {filename}\n\n{content}"

    except Exception as e:
        return f"Error reading the given file: {e}"


@mcp.tool()
def list_files() -> str:
    """List files in directory."""
    try:
        files = [f.name for f in BASE_DIR.iterdir() if f.is_file()]
        files_text = "\n".join(sorted(files)) if files else "No files found"
        return f"Files:\n\n{files_text}"

    except Exception as e:
        return f"Error listing files: {e}"


if __name__ == "__main__":
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    mcp.run()



# {
# 	"mcpServers": {
# 		"simple-calculator": {
#       			"command": "python",
#       			"args": ["C:\\Users\\Lenovo\\Downloads\\MCP_Server\\simple-calculator.py"]
#     	},
# 		"file_reader": {
#       			"command": "python",
#       			"args": ["C:\\Users\\Lenovo\\Downloads\\MCP_Server\\file_system_reader.py"],
# 			        "env": {
# 				            "FILE_READER_DIRECTORY": "C:\\Users\\Lenovo\\Downloads" --> Giving access only to this path. 
# 			        }
#     	}
#   }
# }

# Question: What are the folders exist in my directory.
# What is the context of .json file. 