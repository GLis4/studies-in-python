from src.connector import Connection

class Data:
    def __init__(self, name):
        self.name = name

class CreateTxt:
    
    @classmethod
    def insert_name_in_txt(cls):
        data = Data('hi')
        
        Connection.insert(data.name)
        