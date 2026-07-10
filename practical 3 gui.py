import tkinter as tk
from tkinter import messagebox


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                raise IndexError("Position out of bounds")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds")

        new_node.next = temp.next
        temp.next = new_node

    def delete_node_by_value(self, key):
        temp = self.head

        if temp is not None and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    def delete_node_by_index(self, position):
        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            return

        for _ in range(position - 1):
            if temp is None:
                raise IndexError("Position out of bounds")
            temp = temp.next

        if temp is None or temp.next is None:
            raise IndexError("Position out of bounds")

        temp.next = temp.next.next

    def display(self):
        temp = self.head
        elements = []

        while temp:
            elements.append(str(temp.data))
            temp = temp.next

        return " -> ".join(elements) if elements else "Linked List is Empty"


ll = LinkedList()


def insert_begin():
    try:
        ll.insert_at_beginning(int(data_entry.get()))
        output.config(text=ll.display())
    except:
        messagebox.showerror("Error", "Enter valid data")


def insert_end():
    try:
        ll.insert_at_end(int(data_entry.get()))
        output.config(text=ll.display())
    except:
        messagebox.showerror("Error", "Enter valid data")


def insert_position():
    try:
        ll.insert_at_position(int(data_entry.get()), int(pos_entry.get()))
        output.config(text=ll.display())
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_value():
    try:
        ll.delete_node_by_value(int(data_entry.get()))
        output.config(text=ll.display())
    except:
        messagebox.showerror("Error", "Enter valid value")


def delete_index():
    try:
        ll.delete_node_by_index(int(pos_entry.get()))
        output.config(text=ll.display())
    except Exception as e:
        messagebox.showerror("Error", str(e))


def display():
    output.config(text=ll.display())


root = tk.Tk()
root.title("Singly Linked List")
root.geometry("500x450")

tk.Label(root, text="Singly Linked List", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Data").pack()
data_entry = tk.Entry(root)
data_entry.pack()

tk.Label(root, text="Position").pack()
pos_entry = tk.Entry(root)
pos_entry.pack()

tk.Button(root, text="Insert at Beginning", width=25, command=insert_begin).pack(pady=5)
tk.Button(root, text="Insert at End", width=25, command=insert_end).pack(pady=5)
tk.Button(root, text="Insert at Position", width=25, command=insert_position).pack(pady=5)
tk.Button(root, text="Delete by Value", width=25, command=delete_value).pack(pady=5)
tk.Button(root, text="Delete by Index", width=25, command=delete_index).pack(pady=5)
tk.Button(root, text="Display List", width=25, command=display).pack(pady=5)

output = tk.Label(root, text="Linked List is Empty", font=("Arial", 12), fg="blue")
output.pack(pady=20)

root.mainloop()
