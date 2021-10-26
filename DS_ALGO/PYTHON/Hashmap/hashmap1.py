

# def get_hash(key):
#     h=0
#     for i in key:
#         h+=ord(i)
#     return h%100

# m=get_hash("mu")
# print(m)

class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.MAX

    def add(self,key,value):
        key=self.get_hash(key)
        self.arr[key]=value

    def get(self,key):
        key=self.get_hash(key)
        return self.arr[key]

    def delete(self,key):
        key=self.get_hash(key)
        self.arr[key]=None


t=HashTable()

t.add("march 6",8)
print(t.get("march 6"))

print(t.arr)
print(t.get_hash("march 6"))

t.delete("march 6")
print(t.arr)