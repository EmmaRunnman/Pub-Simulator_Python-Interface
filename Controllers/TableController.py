#for seeing if there are empty seats or available space in the pub
from Models.TableModel import TableModel


class TableController:
    def __init__(self, model):
        """ Kopplar modellen till controllern """
        self.model = model

    def get_tables(self):
        """ Hämtar alla bord från modellen """
        return self.model.get_tables()

    def update_table_status(self, table_id, new_status):
        """ Uppdaterar status på ett bord """
        return self.model.update_table_status(table_id, new_status)

    def get_orders_by_table(self, table_id):
        """ Hämtar beställningar för ett bord """
        return self.model.get_orders_by_table(table_id)


# Testkod
if __name__ == "__main__":
    model = TableModel()
    controller = TableController(model)
    print("Initial tables:", controller.get_tables())

    # Ändra status på ett bord
    controller.update_table_status(1, "occupied")
    print("Updated tables:", controller.get_tables())

