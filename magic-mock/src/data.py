from src.connector import Connection

class Data:
    def __init__(self, name):
        self.name = name

class CreateTxt:
    conn = Connection()
    
    @classmethod
    def insert_name_in_txt(cls):
        data = Data('hi')
        
        CreateTxt.conn.insert(data.name)
        