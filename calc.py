import tkinter as tk

class AutoCalcNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Calc")

        # Modes for operations
        self.modes = ["Add", "Subtract", "Multiply", "Divide"]
        self.current_mode = tk.StringVar(value=self.modes[0])  # Default mode: Sum

        # Buttons for modes
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill='x', padx=10, pady=(10, 0))

        for mode in self.modes:
            button = tk.Button(
                self.button_frame,
                text=mode,
                command=lambda m=mode: self.change_mode(m),
                width=10
            )
            button.pack(side='left', padx=5)

        # Text widget for input
        self.text_area = tk.Text(root, wrap='word', font=('Arial', 14), undo=True)
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)

        # Label to display the result
        self.result_label = tk.Label(root, text="Result: 0", font=('Arial', 12), anchor='e')
        self.result_label.pack(fill='x', padx=10, pady=(0, 10))

        # Event binding for real-time processing
        self.text_area.bind('<KeyRelease>', self.update_result)

    def change_mode(self, mode):
        """Change the current calculation mode and update the result."""
        self.current_mode.set(mode)
        self.update_result()

    def update_result(self, event=None):
        """Calculate the result based on the selected mode."""
        content = self.text_area.get("1.0", "end-1c")
        # Extract numbers from the text
        numbers = [float(num) for num in content.split() if num.replace('.', '', 1).isdigit()]

        if not numbers:
            result = 0
        elif self.current_mode.get() == "Add":
            result = sum(numbers)
        elif self.current_mode.get() == "Subtract":
            result = numbers[0] - sum(numbers[1:])
        elif self.current_mode.get() == "Multiply":
            result = 1
            for num in numbers:
                result *= num
        elif self.current_mode.get() == "Divide":
            try:
                result = numbers[0]
                for num in numbers[1:]:
                    result /= num
            except ZeroDivisionError:
                result = "Error (Division by Zero)"

        self.result_label.config(text=f"Result: {result}")

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = AutoCalcNotepad(root)
    root.mainloop()
