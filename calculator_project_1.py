from tkinter import *
import ast

root = Tk()
root.title("Python Calculator")

# Global index tracker
i = 0

# Function Definitions
def insert_text(text):
    """Insert any text (number or operator) into the display."""
    global i
    display.insert(i, text)
    i += len(str(text))

def clear_all():
    """Clear the entire input display."""
    global i
    display.delete(0, END)
    i = 0

def calculate():
    """Evaluate the expression in the display."""
    global i
    try:
        expression = display.get()
        node = ast.parse(expression, mode="eval")  # Safe parsing
        result = eval(compile(node, "<string>", "eval"))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def undo():
    """Remove the last character from the display."""
    global i
    expression = display.get()
    if expression:
        new_expr = expression[:-1]
        clear_all()
        display.insert(0, new_expr)
        i = len(new_expr)
    else:
        clear_all()

# Display
display = Entry(root, width=25, font=("Arial", 14))
display.grid(row=0, column=0, columnspan=6, pady=10)

# Number Buttons
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for idx, number in enumerate(numbers):
    row = (idx // 3) + 1
    col = idx % 3
    Button(root, text=str(number), width=5, height=2,
           command=lambda num=number: insert_text(num)).grid(row=row, column=col)

# Zero Button
Button(root, text="0", width=5, height=2, command=lambda: insert_text(0)).grid(row=4, column=1)

# Operation Buttons
operations = ["+", "-", "*", "/", "*3.14", "%", "(", "**", ")", "**2"]
for idx, op in enumerate(operations):
    row = (idx // 3) + 1
    col = (idx % 3) + 3
    Button(root, text=op, width=5, height=2,
           command=lambda oper=op: insert_text(oper)).grid(row=row, column=col)

# Function Buttons
Button(root, text="AC", width=5, height=2, command=clear_all).grid(row=4, column=0)
Button(root, text="=", width=5, height=2, command=calculate).grid(row=4, column=2)
Button(root, text="<-", width=5, height=2, command=undo).grid(row=4, column=4)

root.mainloop()
