import pyautogui
import pyperclip
import time

class Automator:
    def run_command(self, command: dict):
        try:
            x = command.get("click_x", 0)
            y = command.get("click_y", 0)
            count = command.get("click_count", 1)
            message = command.get("message", "")
            enter_key = command.get("enter_key", False)

            print(f"[DEBUG] 실행 좌표: ({x},{y})")
            print(f"[DEBUG] 클릭 횟수: {count}")
            print(f"[DEBUG] 메시지: '{message}'")

            pyautogui.moveTo(x, y)
            for _ in range(count):
                pyautogui.click()
                time.sleep(0.1)

            if message:
                pyperclip.copy(message)
                time.sleep(0.05)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.05)

            if enter_key:
                pyautogui.press("enter")

        except Exception as e:
            print("[ERROR] 실행 실패:", str(e))
