import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from pathlib import Path
import sys
import os
import webbrowser
from datetime import datetime

class ResumeFormatterApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_menu()
        self.create_main_interface()
        self.create_status_bar()
        
    def setup_window(self):
        """Configure the main window settings"""
        self.root.title("Resume Formatter Pro")
        self.root.geometry("800x500")
        self.root.minsize(600, 400)
        self.root.configure(bg="#ffffff")
        
        # Set icon if available
        #try:
        #    self.root.iconbitmap(self.resource_path('icon.ico'))
        #    except:
        #    pass
            
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use 'clam' theme for modern look
        self.style.configure("Accent.TButton",
                           font=("Segoe UI", 11),
                           padding=10,
                           background="#007bff")
        self.style.configure("Title.TLabel",
                           font=("Segoe UI", 24),
                           foreground="#2c3e50")
        self.style.configure("Status.TLabel",
                           font=("Segoe UI", 9),
                           foreground="#666666")

    def create_menu(self):
        """Create the application menu bar"""
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Resume", command=self.browse_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Help Menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Documentation", command=self.open_documentation)
        help_menu.add_command(label="About", command=self.show_about)

    def create_main_interface(self):
        """Create the main application interface"""
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(
            self.main_frame,
            text="Resume Formatter Pro",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)

        # Description
        description = ttk.Label(
            self.main_frame,
            text="Transform your resume into a professional format",
            font=("Segoe UI", 11)
        )
        description.pack(pady=(0, 20))

        # File selection frame
        file_frame = ttk.LabelFrame(self.main_frame, text="Resume Selection", padding="10")
        file_frame.pack(fill=tk.X, pady=20)

        self.file_path = tk.StringVar()
        self.file_entry = ttk.Entry(
            file_frame,
            textvariable=self.file_path,
            width=60
        )
        self.file_entry.pack(side=tk.LEFT, padx=(10, 10), fill=tk.X, expand=True)

        browse_btn = ttk.Button(
            file_frame,
            text="Browse",
            command=self.browse_file
        )
        browse_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Format Options Frame
        options_frame = ttk.LabelFrame(self.main_frame, text="Formatting Options", padding="10")
        options_frame.pack(fill=tk.X, pady=20)

        # Template Selection
        self.template_var = tk.StringVar(value="professional")
        ttk.Label(options_frame, text="Template:").pack(side=tk.LEFT, padx=(10, 5))
        template_combo = ttk.Combobox(
            options_frame,
            textvariable=self.template_var,
            values=["Professional", "Modern", "Academic", "Creative"],
            state="readonly",
            width=20
        )
        template_combo.pack(side=tk.LEFT, padx=(0, 20))

        # Format button
        format_btn = ttk.Button(
            self.main_frame,
            text="Format Resume",
            command=self.format_resume,
            style="Accent.TButton"
        )
        format_btn.pack(pady=20)

    def create_status_bar(self):
        """Create the status bar"""
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(
            self.root,
            textvariable=self.status_var,
            style="Status.TLabel",
            relief=tk.SUNKEN,
            padding=(10, 5)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def browse_file(self):
        """Handle file selection"""
        filename = filedialog.askopenfilename(
            title="Select Resume",
            filetypes=(
                ("Word Documents", "*.doc;*.docx"),
                ("PDF Files", "*.pdf"),
                ("All files", "*.*")
            )
        )
        if filename:
            self.file_path.set(filename)
            self.status_var.set(f"Selected file: {Path(filename).name}")

    def format_resume(self):
        """Handle resume formatting"""
        if not self.file_path.get():
            messagebox.showwarning(
                "No File Selected",
                "Please select a resume file first."
            )
            return

        # Log the formatting attempt
        self.log_action(f"Formatting attempted: {Path(self.file_path.get()).name}")
        
        # Placeholder for actual formatting logic
        self.status_var.set("Processing...")
        self.root.update()
        
        # Simulate processing
        self.root.after(1000, self.show_format_complete)

    def show_format_complete(self):
        """Show completion message"""
        self.status_var.set("Ready")
        messagebox.showinfo(
            "Success",
            "Resume formatting complete!\n\nTemplate: " + 
            f"{self.template_var.get()}\nFile: {Path(self.file_path.get()).name}"
        )

    def open_documentation(self):
        """Open documentation in web browser"""
        # Replace with your actual documentation URL
        webbrowser.open("https://github.com/yourusername/resume-formatter")

    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo(
            "About Resume Formatter Pro",
            "Resume Formatter Pro v1.0.0\n\n" +
            "A professional tool for formatting resumes.\n\n" +
            "© 2024 Your Company Name"
        )

    def log_action(self, message):
        """Log user actions"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_path = Path("resume_formatter.log")
        
        try:
            with open(log_path, "a") as log_file:
                log_file.write(f"[{timestamp}] {message}\n")
        except:
            pass

    @staticmethod
    def resource_path(relative_path):
        """Get absolute path to resource"""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

def main():
    root = tk.Tk()
    app = ResumeFormatterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 