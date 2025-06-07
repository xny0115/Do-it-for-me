import tkinter as tk
from tkinter import ttk
from core.command_manager import CommandManager
from core.automator import Automator
from ui.widgets import CommandItemFrame

class CommandApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Do it for me (difm)")
        self.cm = CommandManager()
        self.automator = Automator()
        self.commands = self.cm.get_all()

        self.tab_control = ttk.Notebook(self.root)
        self.tab_main = tk.Frame(self.tab_control)
        self.tab_setting = tk.Frame(self.tab_control)

        self.tab_control.add(self.tab_main, text="실행")
        self.tab_control.add(self.tab_setting, text="설정")
        self.tab_control.pack(expand=1, fill="both")

        self.build_main_tab()
        self.build_setting_tab()

    def build_main_tab(self):
        for widget in self.tab_main.winfo_children():
            widget.destroy()
        # 최신 commands.json에서 항상 다시 불러오기 (동기화 핵심)
        self.commands = self.cm.get_all()
        for idx, cmd in enumerate(self.commands):
            row = tk.Frame(self.tab_main)
            row.pack(fill="x", padx=5, pady=2)
            tk.Label(row, text=f"{idx + 1}.").pack(side="left", padx=5)
            tk.Button(row, text="실행", command=lambda c=cmd.copy(): self.automator.run_command(c)).pack(side="left")

    def build_setting_tab(self):
        for widget in self.tab_setting.winfo_children():
            widget.destroy()
        for cmd in self.commands:
            item = CommandItemFrame(
                master=self.tab_setting,
                command=cmd,
                on_update=self.update_command,
                on_add=self.add_command,
                on_delete=self.delete_command,
                on_execute=self.automator.run_command
            )
            item.pack(fill="x", padx=3, pady=2)
        save_frame = tk.Frame(self.tab_setting)
        save_frame.pack(fill="x", padx=3, pady=5)
        tk.Button(save_frame, text="저장", command=self.save_changes).pack(side="right", padx=5)

    def update_command(self, old_cmd, new_cmd):
        for i, cmd in enumerate(self.commands):
            if cmd == old_cmd:
                self.commands[i] = new_cmd
                break
        self.refresh_tabs()

    def add_command(self, new_cmd):
        self.commands.append(new_cmd)
        self.refresh_tabs()

    def delete_command(self, target_cmd):
        self.commands = [cmd for cmd in self.commands if cmd != target_cmd]
        self.refresh_tabs()

    def refresh_tabs(self):
        self.build_main_tab()
        self.build_setting_tab()

    def save_changes(self):
        new_commands = []
        for child in self.tab_setting.winfo_children():
            if isinstance(child, CommandItemFrame):
                new_commands.append(child.get_command_data())
        self.commands = new_commands
        self.cm.commands = new_commands
        self.cm.save_commands()
        print("[INFO] 명령어 저장됨")
        # 저장 후 바로 동기화
        self.build_main_tab()

def run_app(root):
    CommandApp(root)
    root.mainloop()
