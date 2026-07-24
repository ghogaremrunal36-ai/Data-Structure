import tkinter as tk
from tkinter import messagebox, simpledialog


class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            return "Queue is full!"
        self.queue.append(item)
        return f"Enqueued: {item}"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        return f"Dequeued: {self.queue.pop(0)}"

    def peek(self):
        if self.is_empty():
            return "Queue is empty!"
        return f"Front Item: {self.queue[0]}"

    def traverse(self):
        if self.is_empty():
            return "Queue is empty!"
        return " -> ".join(self.queue)



root = tk.Tk()
root.title("Queue Operations")
root.geometry("500x450")
root.config(bg="lightblue")

max_size = simpledialog.askinteger("Queue Size", "Enter Maximum Queue Size:")
q = Queue(max_size)



output = tk.Text(root, height=10, width=50, font=("Arial", 12))
output.pack(pady=10)


def show(msg):
    output.delete(1.0, tk.END)
    output.insert(tk.END, msg)


def enqueue():
    if q.is_full():
        messagebox.showerror("Error", "Queue is Full!")
        return

    item = simpledialog.askstring("Enqueue", "Enter Item:")
    if item:
        show(q.enqueue(item))


def dequeue():
    show(q.dequeue())


def peek():
    show(q.peek())


def traverse():
    show(q.traverse())


def display():
    if q.is_empty():
        show("Queue is Empty!")
    else:
        s = ""
        for i, item in enumerate(q.queue, 1):
            s += f"{i}. {item}\n"
        show(s)


def empty():
    if q.is_empty():
        messagebox.showinfo("Queue", "Queue is Empty")
    else:
        messagebox.showinfo("Queue", "Queue is Not Empty")


def full():
    if q.is_full():
        messagebox.showinfo("Queue", "Queue is Full")
    else:
        messagebox.showinfo("Queue", "Queue is Not Full")


def clear():
    output.delete(1.0, tk.END)


tk.Button(root, text="Enqueue", width=15, bg="green", fg="white", command=enqueue).pack(pady=3)

tk.Button(root, text="Dequeue", width=15, bg="red", fg="white", command=dequeue).pack(pady=3)

tk.Button(root, text="Peek", width=15, bg="blue", fg="white", command=peek).pack(pady=3)

tk.Button(root, text="Traverse", width=15, bg="purple", fg="white", command=traverse).pack(pady=3)

tk.Button(root, text="Display Queue", width=15, bg="orange", command=display).pack(pady=3)

tk.Button(root, text="Check Empty", width=15, bg="cyan", command=empty).pack(pady=3)

tk.Button(root, text="Check Full", width=15, bg="yellow", command=full).pack(pady=3)

tk.Button(root, text="Clear Output", width=15, bg="gray", fg="white", command=clear).pack(pady=3)

tk.Button(root, text="Exit", width=15, bg="black", fg="white", command=root.destroy).pack(pady=5)

root.mainloop()
