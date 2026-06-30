import tkinter as tk
from tkinter import messagebox, simpledialog


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Invalid Position")
        self.items.insert(position, item)

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid Position")
        return self.items.pop(position)

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def traverse(self):
        if self.is_empty():
            return "Stack is Empty"
        return " <- ".join(self.items)

    def __str__(self):
        if self.is_empty():
            return "Stack is Empty"
        return " <- ".join(reversed(self.items))


stack = Stack()


def update_stack():
    stack_label.config(text="Current Stack: " + str(stack))


def insert_item():
    item = simpledialog.askstring("Insert", "Enter Item:")
    if item is None:
        return

    try:
        pos = simpledialog.askinteger("Insert", "Enter Position (0-based):")
        if pos is None:
            return

        stack.insert(item, pos)
        update_stack()
        messagebox.showinfo("Success", "Item Inserted Successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_item():
    try:
        pos = simpledialog.askinteger("Delete", "Enter Position:")
        if pos is None:
            return

        item = stack.delete(pos)
        update_stack()
        messagebox.showinfo("Deleted", f"{item} Deleted Successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def peek_item():
    try:
        messagebox.showinfo("Top Item", stack.peek())
    except Exception as e:
        messagebox.showerror("Error", str(e))


def check_empty():
    if stack.is_empty():
        messagebox.showinfo("Stack", "Stack is Empty")
    else:
        messagebox.showinfo("Stack", "Stack is Not Empty")


def stack_size():
    messagebox.showinfo("Size", f"Stack Size = {stack.size()}")


def traverse_stack():
    messagebox.showinfo("Traverse", stack.traverse())


root = tk.Tk()
root.title("Stack Operations")
root.geometry("450x500")
root.configure(bg="lightblue")

title = tk.Label(root,
                 text="STACK OPERATIONS",
                 font=("Arial", 18, "bold"),
                 bg="lightblue")
title.pack(pady=10)

stack_label = tk.Label(root,
                       text="Current Stack: Stack is Empty",
                       font=("Arial", 12),
                       bg="white",
                       width=40,
                       height=2)
stack_label.pack(pady=10)

tk.Button(root, text="Insert", width=20, command=insert_item).pack(pady=5)

tk.Button(root, text="Delete", width=20, command=delete_item).pack(pady=5)

tk.Button(root, text="Peek", width=20, command=peek_item).pack(pady=5)

tk.Button(root, text="Check Empty", width=20, command=check_empty).pack(pady=5)

tk.Button(root, text="Size", width=20, command=stack_size).pack(pady=5)

tk.Button(root, text="Traverse", width=20, command=traverse_stack).pack(pady=5)

tk.Button(root,
          text="Exit",
          width=20,
          bg="red",
          fg="white",
          command=root.destroy).pack(pady=20)

root.mainloop()
