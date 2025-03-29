class Connection:
    def insert(self, name):
        with open('hello.txt', 'w') as myFile:
             myFile.write(name)
             
        return name