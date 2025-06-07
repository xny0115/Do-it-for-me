import tkinter as tk

class CommandItemFrame(tk.Frame):
    def __init__(self, master, command, on_update, on_add, on_delete, on_execute):
        super().__init__(master, bd=1, relief="ridge", padx=3, pady=2)
        self.command = command
        self.on_update = on_update
        self.on_add = on_add
        self.on_delete = on_delete
        self.on_execute = on_execute
        self.build_ui()

    def build_ui(self):
        x = self.command.get("click_x", 0)
        y = self.command.get("click_y", 0)
        self.coord_var = tk.StringVar(value=f"{x},{y}")
        self.count_var = tk.StringVar(value=str(self.command.get("click_count", 1)))
        self.msg_var = tk.StringVar(value=self.command.get("message", ""))
        self.enter_var = tk.BooleanVar(value=self.command.get("enter_key", False))

        self.coord_entry = tk.Entry(self, textvariable=self.coord_var, width=10)
        self.count_entry = tk.Entry(self, textvariable=self.count_var, width=2)
        self.msg_entry = tk.Entry(self, textvariable=self.msg_var, width=40)

        self.coord_entry.pack(side="left", padx=2)
        self.count_entry.pack(side="left", padx=2)
        self.msg_entry.pack(side="left", padx=2)
        tk.Checkbutton(self, variable=self.enter_var).pack(side="left", padx=2)

        tk.Button(self, text="수정", command=self.handle_update).pack(side="left")
        tk.Button(self, text="추가", command=self.handle_add).pack(side="left")
        tk.Button(self, text="삭제", command=self.handle_delete).pack(side="left")
        tk.Button(self, text="실행", command=self.handle_execute).pack(side="left")

    def parse_coord(self):
        try:
            x_str, y_str = self.coord_var.get().split(",")
            return int(x_str.strip()), int(y_str.strip())
        except Exception:
            return 0, 0

    def get_command_data(self):
        coord = self.coord_entry.get()
        count = self.count_entry.get()
        msg = self.msg_entry.get()
        x, y = self.parse_coord()
        return {
            "click_x": x,
            "click_y": y,
            "click_count": int(count) if count.isdigit() else 1,
            "message": msg,
            "enter_key": self.enter_var.get()
        }

    def handle_update(self):
        self.on_update(self.command, self.get_command_data())

    def handle_add(self):
        self.on_add(self.get_command_data())

    def handle_delete(self):
        self.on_delete(self.command)

    def handle_execute(self):
        self.after(50, lambda: self.on_execute(self.get_command_data()))
