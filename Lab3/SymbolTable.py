class Element:
    def __init__(self,key,value):
        self.value = value
        self.key = key

    def __str__(self) -> str:
        return (f"<key:{self.key} value:{self.value}>")

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table=[]
        for i in range(capacity):
            l=[]
            self.table.append(l)

    def __str__(self) -> str:
        lists=[]
        for i in range(self.capacity):
            list=[]
            for j in range(len(self.table[i])):
                list.append(str(self.table[i][j]))
            lists.append(list)
        return str(lists)
                
    def hash(self, key):
        sum=0
        for letter in key:
            sum=sum+ord(letter)
        return sum % self.capacity
    
    def insert(self,key,value):
        #if self.check_if_already_exists(key)==-1:
        self.table[self.hash(key)].append(Element(key,value))
        #else:
        #self.table[self.hash(key)][self.check_if_already_exists((key))].value=value

    def delete(self,key):
        i = self.hash(key)
        for index in range(len(self.table[i])):
            if self.table[i][index].key==key:
               self.table[i].remove(index)

    
    def check_if_already_exists(self,key):
        i=self.hash(key)
        found=-1
        for index in range(len(self.table[i])):
            if key==self.table[i][index].key:
                found=index
        return found
    
    def get_value(self,key):
        for j in range (len(self.table[self.hash(key)])):
            if self.table[self.hash(key)][j].key==key:
                return self.table[self.hash(key)][j].value
    
'''sc=HashTable(3)
sc.insert("a",1)
sc.insert("ac",2)
sc.insert("ca",3)
print(sc.get_value("a"))'''