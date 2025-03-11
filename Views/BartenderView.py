#for table view + expanding with order when pressing a table
import tkinter as tk
from tkinter import messagebox, ttk
from Controllers.TableController import TableController
from Models.TableModel import TableModel


class BartenderView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Bartender View - Table Management")
        self.geometry("800x600")  # Adjusted window size
        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack(fill="both", expand=True)
        self.draw_tables()

    def draw_tables(self):
        """Draw all tables on the canvas."""
        self.canvas.delete("all")  # Clear canvas
        tables = self.controller.get_tables()

        print("Loaded tables:", tables)  # Debugging print

        if not tables:
            self.canvas.create_text(400, 300, text="No tables available", font=("Arial", 16))
            return

        for index, table in enumerate(tables):
            x = 150 + (index % 4) * 150  # Adjust positioning
            y = 150 + (index // 4) * 150

            color = "lightgreen" if table["status"] == "free" else "orange" if table["status"] == "reserved" else "red"

            self.canvas.create_rectangle(x - 40, y - 20, x + 40, y + 20, fill=color, outline="black",
                                         tags=f"table_{table['table_id']}")
            self.canvas.create_text(x, y,
                                    text=f"Table {table['table_id']}\nSeats: {table['number_of_seats']}\nStatus: {table['status']}",
                                    font=("Arial", 10), tags=f"table_{table['table_id']}")

            self.canvas.tag_bind(f"table_{table['table_id']}", "<Button-1>",
                                 lambda event, t=table: self.show_status_popup(t))

    def show_status_popup(self, table):
        """Show a popup window to change table status."""
        popup = tk.Toplevel(self)
        popup.title(f"Change Status - Table {table['table_id']}")
        popup.geometry("300x150")

        tk.Label(popup, text=f"Change status for Table {table['table_id']}").pack(pady=10)

        status_var = tk.StringVar(value=table["status"])
        status_dropdown = ttk.Combobox(popup, textvariable=status_var, values=["free", "reserved", "occupied"])
        status_dropdown.pack(pady=5)

        tk.Button(popup, text="Update Status", command=lambda: self.update_status(table, status_var.get(), popup)).pack(
            pady=10)

    def update_status(self, table, new_status, popup):
        """Update table status and redraw tables."""
        self.controller.update_table_status(table["table_id"], new_status)
        self.draw_tables()
        popup.destroy()
        messagebox.showinfo("Status Updated", f"Table {table['table_id']} is now {new_status}")


if __name__ == "__main__":
    model = TableModel()
    controller = TableController(model)
    app = BartenderView(controller)
    app.mainloop()
