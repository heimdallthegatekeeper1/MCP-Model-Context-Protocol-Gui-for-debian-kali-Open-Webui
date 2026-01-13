import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import subprocess
import threading
import webbrowser
import os
import signal
import time

class MCPGuiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FastMCP Server Manager (2026)")
        self.root.geometry("1000x700")

        self.process_mcp = None
        self.process_mcpo = None
        self.venv_path = os.path.expanduser("~/mcp-server/.venv/bin/activate")
        self.script_path = os.path.expanduser("~/mcp-server/server.py")
        self.shell_command = "bash -c 'source {} && exec {}'"
        
        self.create_widgets()
        self.create_documentation_tab()

    def create_widgets(self):
        # --- Control Frame ---
        control_frame = tk.Frame(self.root, padx=10, pady=10)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Button(control_frame, text="Start Servers", command=self.start_servers, bg='green', fg='white').pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Stop All Servers", command=self.stop_servers, bg='red', fg='white').pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Open Inspector", command=lambda: webbrowser.open("http://localhost:6274/")).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Open OpenAPI Docs", command=lambda: webbrowser.open("http://localhost:8000/docs")).pack(side=tk.LEFT, padx=5)

        # --- Terminal Output Tabs ---
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tab_mcp = tk.Frame(self.notebook)
        self.tab_mcpo = tk.Frame(self.notebook)
        
        self.notebook.add(self.tab_mcp, text="FastMCP Server")
        self.notebook.add(self.tab_mcpo, text="mcpo Proxy (OpenAPI)")

        self.output_mcp = scrolledtext.ScrolledText(self.tab_mcp, wrap=tk.WORD, bg='black', fg='white')
        self.output_mcp.pack(fill=tk.BOTH, expand=True)
        self.output_mcpo = scrolledtext.ScrolledText(self.tab_mcpo, wrap=tk.WORD, bg='black', fg='white')
        self.output_mcpo.pack(fill=tk.BOTH, expand=True)

    def create_documentation_tab(self):
        tab_docs = tk.Frame(self.notebook, padx=10, pady=10)
        self.notebook.add(tab_docs, text="Quick Guide")
        
        doc_text = scrolledtext.ScrolledText(tab_docs, wrap=tk.WORD, padx=5, pady=5)
        doc_text.pack(fill=tk.BOTH, expand=True)
        
        docs_content = """
        --- 2026 CONNECTION GUIDE ---
        
        1. Click 'Start Servers'.
        2. Wait for the 'mcpo Proxy' tab to show it is running on port 8000.
        3. Go to Open WebUI -> Admin Settings -> External Tools.
        4. Add a tool with:
           - Type: OpenAPI
           - URL: http://localhost:8000/openapi.json
        """
        doc_text.insert(tk.INSERT, docs_content)
        doc_text.config(state=tk.DISABLED)

    def run_process_in_thread(self, command, output_widget, process_var_name):
        full_command = self.shell_command.format(self.venv_path, command)
        try:
            process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                                     text=True, shell=True, preexec_fn=os.setsid)
            setattr(self, process_var_name, process)
            
            for line in iter(process.stdout.readline, ''):
                output_widget.insert(tk.END, line)
                output_widget.see(tk.END)
            process.stdout.close()
            process.wait()
        except Exception as e:
            output_widget.insert(tk.END, f"Error: {e}\n")

    def start_servers(self):
        if self.process_mcp or self.process_mcpo:
            messagebox.showinfo("Status", "Servers are already running!")
            return

        self.output_mcp.delete('1.0', tk.END)
        self.output_mcpo.delete('1.0', tk.END)
        
        mcp_cmd = f"fastmcp dev {self.script_path}"
        mcpo_cmd = f"mcpo --port 8000 -- python {self.script_path}"

        threading.Thread(target=self.run_process_in_thread, args=(mcp_cmd, self.output_mcp, 'process_mcp'), daemon=True).start()
        threading.Thread(target=self.run_process_in_thread, args=(mcpo_cmd, self.output_mcpo, 'process_mcpo'), daemon=True).start()
        messagebox.showinfo("Status", "Starting servers... Check the tabs for logs.")

    def stop_servers(self):
        for attr in ['process_mcp', 'process_mcpo']:
            process = getattr(self, attr)
            if process:
                try:
                    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                except:
                    pass
                setattr(self, attr, None)
        messagebox.showinfo("Status", "Servers stopped.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MCPGuiApp(root)
    root.mainloop()
