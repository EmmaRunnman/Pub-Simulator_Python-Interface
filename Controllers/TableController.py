#for seeing if there are empty seats or available space in the pub

from Models import TableModel
from Views import BartenderView

class TableController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_table(self, table_id, number_of_seats, status="free"):
        """Adds a new table to the model."""
        self.model.add_table(table_id, number_of_seats, status)
        self.update_view()

    def remove_table(self, table_id):
        """Removes a table from the model by ID."""
        self.model.remove_table(table_id)
        self.update_view()

    def update_table_status(self, table_id, status):
        """Updates the status of a table."""
        self.model.update_table_status(table_id, status)
        self.update_view()

    def assign_customers(self, table_id, customers):
        """Assigns customers to a table."""
        self.model.assign_customers(table_id, customers)
        self.update_view()

    def add_order_to_table(self, table_id, order_id):
        """Adds an order to a table."""
        self.model.add_order_to_table(table_id, order_id)
        self.update_view()

    def update_view(self):
        """Fetches the latest table data and updates the view."""
        tables = self.model.get_all_tables()
        self.view.display_tables(tables)
