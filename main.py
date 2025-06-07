import tkinter as tk
import pyautogui
import pyperclip
from ui.app import run_app

def bind_f11_clipboard(root):
    def copy_mouse_position(event=None):
        x, y = pyautogui.position()
        coord_str = f"{x},{y}"
        pyperclip.copy(coord_str)
        print(f"좌표 복사됨: {coord_str}")
    root.bind("<F11>", copy_mouse_position)

if __name__ == "__main__":
    root = tk.Tk()
    bind_f11_clipboard(root)
    run_app(root)
