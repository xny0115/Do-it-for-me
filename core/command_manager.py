# core/command_manager.py
import json
import threading
from utils.file_io import load_json, save_json

class CommandManager:
    def __init__(self, file_path="commands.json"):
        self.file_path = file_path
        self.lock = threading.Lock()
        self.commands = self.load_commands()

    def load_commands(self):
        return load_json(self.file_path) or []

    def save_commands(self):
        with self.lock:
            save_json(self.file_path, self.commands)

    def get_all(self):
        return self.commands

    def add(self, cmd):
        with self.lock:
            self.commands.append(cmd)
            self.save_commands()

    def update(self, index, new_cmd):
        with self.lock:
            if 0 <= index < len(self.commands):
                self.commands[index] = new_cmd
                self.save_commands()
                return True
            return False

    def delete(self, index):
        with self.lock:
            if 0 <= index < len(self.commands):
                self.commands.pop(index)
                self.save_commands()
                return True
            return False
