import os
import time
from colorama import init, Fore


init(autoreset=True)


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
            print(Fore.RED + "Queue is full. Cannot enqueue.")
        else:
            self.queue.append(item)
            print(Fore.GREEN + f"Enqueued: {item}")
        time.sleep(0.5)

    def dequeue(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty. Cannot dequeue.")
        else:
            item = self.queue.pop(0)
            print(Fore.YELLOW + f"Dequeued: {item}")
        time.sleep(0.5)

    def peek(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty.")
        else:
            print(Fore.BLUE + f"Front item: {self.queue[0]}")
        time.sleep(0.5)

    def traverse(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty.")
        else:
            print(Fore.CYAN + "Queue:", end=" ")
            for item in self.queue:
                print(item, end=" ")
                time.sleep(0.2)
            print()
        time.sleep(0.5)

    def display_list(self):
        if self.is_empty():
            print(Fore.RED + "Queue is empty.")
        else:
            print(Fore.MAGENTA + "\nCurrent Queue:")
            for i, item in enumerate(self.queue, start=1):
                print(f"{i}. {item}")
        time.sleep(0.5)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    max_size = int(input(Fore.YELLOW + "Enter maximum size of queue: "))
    q = Queue(max_size)

    while True:
        clear_screen()

        print(Fore.CYAN + "========== QUEUE MENU ==========")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Traverse")
        print("5. Display Queue")
        print("6. Check Empty")
        print("7. Check Full")
        print("8. Exit")
        print("=" * 30)

        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == "1":
            item = input("Enter item: ")
            q.enqueue(item)

        elif choice == "2":
            q.dequeue()

        elif choice == "3":
            q.peek()

        elif choice == "4":
            q.traverse()

        elif choice == "5":
            q.display_list()

        elif choice == "6":
            if q.is_empty():
                print(Fore.RED + "Queue is empty.")
            else:
                print(Fore.GREEN + "Queue is not empty.")
            time.sleep(0.5)

        elif choice == "7":
            if q.is_full():
                print(Fore.RED + "Queue is full.")
            else:
                print(Fore.GREEN + "Queue is not full.")
            time.sleep(0.5)

        elif choice == "8":
            print(Fore.MAGENTA + "Exiting program... Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice! Try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
