class Connection:
    
    @classmethod
    def insert(cls, name):
        with open('hello.txt', 'w') as myFile:
             myFile.write(name)
             
        return name