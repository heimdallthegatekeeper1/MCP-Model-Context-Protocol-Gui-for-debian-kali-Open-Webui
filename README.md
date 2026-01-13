A professional README for your GitHub repository is essential to help other developers (and your future self) understand, install, and use your project
. In 2026, the standard for AI tool documentation is to provide clear, step-by-step setup instructions specifically for integrations like Open WebUI. 
Below is a complete README.md template tailored for your FastMCP Server Manager project.
1. Create the README File
In your terminal, create the file:
bash

nano ~/mcp-server/README.md

Use code with caution.
2. Copy and Paste this Content
markdown

# 🚀 FastMCP Server Manager (2026)

A lightweight Python-based GUI for managing **Model Context Protocol (MCP)** servers on Kali Linux. This tool simplifies the process of running both the FastMCP development server and the `mcpo` OpenAPI proxy simultaneously, providing integrated terminal outputs for easy debugging.

---

## ✨ Features
- **One-Click Startup:** Launch both the FastMCP server and the OpenAPI proxy with a single button.
- **Integrated Terminals:** View real-time logs for both services in dedicated tabs.
- **Auto-Venv Activation:** Automatically detects and sources your `.venv` environment.
- **Direct Links:** Quick buttons to open the FastMCP Inspector and OpenAPI documentation.
- **2026 Ready:** Optimized for the latest `mcpo` and `fastmcp` specifications.

---

## 🛠️ Prerequisites
Before running the GUI, ensure you have the following installed:

1. **System Dependencies:**
   ```bash
   sudo apt update && sudo apt install -y python3-tk

Use code with caution.

    Python Environment:
    Ensure your ~/mcp-server directory has a virtual environment with the necessary packages:
    bash

    cd ~/mcp-server
    source .venv/bin/activate
    uv pip install fastmcp mcpo

    Use code with caution.

🚀 Getting Started

    Clone the Repository:
    bash

    git clone 

    Use code with caution.

bash

github.com

Use code with caution.
bash


cd your-repo-name

Use code with caution.
Run the Manager:
bash

python3 mcp_gui.py

Use code with caution.
Start Servers:
Click the Start Servers button. Wait for the logs to indicate that the proxy is running at http://localhost:8000.

🤖 Open WebUI Integration
To use your tools in Open WebUI:

    Go to Admin Settings → External Tools.
    Click + Add Tool.
    Type: Select OpenAPI (Required for 2026 proxy compatibility).
    URL: http://localhost:8000/openapi.json
    Save and refresh your workspace.

📂 Project Structure

    mcp_gui.py: The main Tkinter application script.
    server.py: Your custom MCP server containing tools (e.g., @mcp.tool()).
    .venv/: Python virtual environment.

🤝 Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.
📄 License
This project is licensed under the MIT License.


### 3. Save and Exit
*   Press `CTRL + O` then `Enter`.
*   Press `CTRL + X`.

### Pro-Tip for 2026 GitHub Submissions
If you want your server to be discoverable in the global **MCP Registry**,


When you restart your PC, the servers will not run automatically. You will need to execute specific commands in your terminal to start them up each time you want your LLM to use the tools
. 
Summary of Setup Steps (for a fresh start)
These instructions assume you are using Kali Linux and have your work saved in ~/mcp-server/server.py.
1. Preparation (Run Once)
If this is your first time setting up the PC, install uv (our package manager) and move into your project folder:
bash

# Install the uv package manager
curl -LsSf astral.sh | sh
source $HOME/.local/bin/env

# Navigate to your project folder
cd ~/mcp-server

Use code with caution.
2. Daily Startup (Run Every Time You Restart)
Every time you want to use your MCP tools, follow these steps:
Terminal 1:
bash

# Activate your virtual environment
cd ~/mcp-server
source .venv/bin/activate

# Start the FastMCP server and keep this terminal open
fastmcp dev server.py

Use code with caution.
Terminal 2 (Open a new terminal tab/window):
bash

# Activate the same virtual environment in the second terminal
cd ~/mcp-server
source .venv/bin/activate

# Install the proxy if needed (only once in this specific environment)
uv pip install mcpo

# Start the MCP-to-OpenAPI proxy and keep this terminal open
mcpo --port 8000 -- python server.py

Use code with caution.
3. Open WebUI Connection (Run Once)
In Open WebUI's Admin Settings → External Tools:

    Type: OpenAPI
    URL: http://localhost:8000

4. Firewall Considerations
Since you are using localhost (loopback address), typical firewalls won't block the connection between Open WebUI and your server on the same machine. However, if you were to use a service like ngrok to make your server public, you might need to adjust firewall settings for incoming public traffic. 
Conclusion: Do I need a GUI?
No, you do not need to construct a GUI for normal users to interact with the server or manage it day-to-day.

    Open WebUI is already the robust graphical interface that allows users to interact with the LLMs and manage tool selection in a user-friendly way.
    The setup you currently have, using terminal commands for the backend servers, is the standard and necessary way to run these services locally. 

The process you just completed is the standard administrator setup for self-hosting AI tools.





Prerequisites
You need to ensure you have the tkinter library installed, which usually comes with Python, and that the mcpo and fastmcp packages are installed in your virtual environment:
bash

# Ensure tkinter is available (common on Linux)
sudo apt update && sudo apt install python3-tk

# Ensure packages are installed in your .venv
cd ~/mcp-server
source .venv/bin/activate
uv pip install fastmcp mcpo

Use code with caution.

