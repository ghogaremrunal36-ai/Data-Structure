import tkinter as tk
from tkinter import messagebox


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(position):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds.")

        new_node.next = temp
        new_node.prev = temp.prev

        if temp.prev:
            temp.prev.next = new_node
        temp.prev = new_node

    def delete_node_at_beginning(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_node_at_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None

    def delete_node_at_position(self, position):
        if self.head is None:
            return

        temp = self.head

        for _ in range(position):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds.")

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    def search_node(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def length_of_list(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def display(self):
        temp = self.head
        elements = []

        while temp:
            elements.append(str(temp.data))
            temp = temp.next

        if not elements:
            return "Doubly Linked List is Empty"

        return " <-> ".join(elements)


dll = DoublyLinkedList()


def update_display():
    output.config(text=dll.display())


def insert_begin():
    try:
        data = int(data_entry.get())
        dll.insert_at_beginning(data)
        update_display()
    except:
        messagebox.showerror("Error", "Enter valid data")


def insert_end():
    try:
        data = int(data_entry.get())
        dll.insert_at_end(data)
        update_display()
    except:
        messagebox.showerror("Error", "Enter valid data")


def insert_position():
    try:
        data = int(data_entry.get())
        pos = int(position_entry.get())
        dll.insert_at_position(data, pos)
        update_display()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_begin():
    dll.delete_node_at_beginning()
    update_display()


def delete_end():
    dll.delete_node_at_end()
    update_display()


def delete_position():
    try:
        pos = int(position_entry.get())
        dll.delete_node_at_position(pos)
        update_display()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def search():
    try:
        data = int(data_entry.get())
        if dll.search_node(data):
            messagebox.showinfo("Search", "Node Found")
        else:
            messagebox.showinfo("Search", "Node Not Found")
    except:
        messagebox.showerror("Error", "Enter valid data")


def length():
    messagebox.showinfo("Length", f"Length of List: {dll.length_of_list()}")


root = tk.Tk()
root.title("Doubly Linked List")
root.geometry("550x550")

title = tk.Label(root, text="Doubly Linked List", font=("Arial", 18, "bold"))
title.pack(pady=10)

tk.Label(root, text="Enter Data").pack()
data_entry = tk.Entry(root, width=25)
data_entry.pack()

tk.Label(root, text="Enter Position").pack()
position_entry = tk.Entry(root, width=25)
position_entry.pack(pady=5)

tk.Button(root, text="Insert at Beginning", width=25, command=insert_begin).pack(pady=3)
tk.Button(root, text="Insert at End", width=25, command=insert_end).pack(pady=3)
tk.Button(root, text="Insert at Position", width=25, command=insert_position).pack(pady=3)

tk.Button(root, text="Delete at Beginning", width=25, command=delete_begin).pack(pady=3)
tk.Button(root, text="Delete at End", width=25, command=delete_end).pack(pady=3)
tk.Button(root, text="Delete at Position", width=25, command=delete_position).pack(pady=3)

tk.Button(root, text="Search Node", width=25, command=search).pack(pady=3)
tk.Button(root, text="Length of List", width=25, command=length).pack(pady=3)

tk.Button(root, text="Display List", width=25, command=update_display).pack(pady=3)

output = tk.Label(
    root,
    text="Doubly Linked List is Empty",
    font=("Arial", 12),
    fg="blue",
    wraplength=500
)
output.pack(pady=20)

root.mainloop()
