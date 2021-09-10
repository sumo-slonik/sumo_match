from PyQt5.QtWidgets import QTableWidget


class QtTableWrapper:
    def __init__(self, table: QTableWidget,columns):
        self.table = table
        

    def load_data(self,data):
        pass