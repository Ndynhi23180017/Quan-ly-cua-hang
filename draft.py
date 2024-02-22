import tkinter as tk
from tkinter import ttk

class BillApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bill Entry")
        self.master.geometry("400x400")

        self.product_label = ttk.Label(self.master, text="Product:")
        self.product_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.product_entry = ttk.Entry(self.master)
        self.product_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.quantity_label = ttk.Label(self.master, text="Quantity:")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.quantity_entry = ttk.Entry(self.master)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.price_label = ttk.Label(self.master, text="Price:")
        self.price_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.price_entry = ttk.Entry(self.master)
        self.price_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.add_button = ttk.Button(self.master, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.bill_text = tk.Text(self.master, height=10, width=40)
        self.bill_text.grid(row=4, column=0, columnspan=2, pady=10)

        self.calculate_button = ttk.Button(self.master, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.total_label = ttk.Label(self.master, text="Total:")
        self.total_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

        self.total_var = tk.StringVar()
        self.total_entry = ttk.Entry(self.master, textvariable=self.total_var, state="readonly")
        self.total_entry.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)

        self.items = []

    def add_item(self):
        product = self.product_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        if product and quantity and price:
            item_text = f"{product} - Quantity: {quantity}, Price: {price}\n"
            self.bill_text.insert(tk.END, item_text)

            item_total = int(quantity) * float(price)
            self.items.append(item_total)

            self.product_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)

    def calculate_total(self):
        total = sum(self.items)
        self.total_var.set(f"{total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillApp(root)
    root.mainloop()
