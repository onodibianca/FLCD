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
     
    def check_if_already_exists(self,key):
        i=self.hash(key)
        found=-1
        for index in range(len(self.table[i])):
            if key==self.table[i][index].key:
                found=index
        return found   

    def insert(self,key,value):
        if self.check_if_already_exists(key)==-1:
            self.table[self.hash(key)].append(Element(key,value))
        else:
            self.table[self.hash(key)][self.check_if_already_exists((key))].value=value

    def delete(self,key):
        i = self.hash(key)
        deleted=0
        for index in range(len(self.table[i])):
            if self.table[i][index].key==key:
               self.table[i].remove(self.table[i][index])
               deleted=1
        return deleted

def main():
    ST=HashTable(10)
    ST.insert('a1b0A',12)
    ST.insert('ab',10)
    ST.insert('a0b1A',3)
    print(ST.check_if_already_exists('a0b1A'))
    print(ST.check_if_already_exists('ab10A'))
    ST.delete('a0b1A')
    print(ST)

main()

