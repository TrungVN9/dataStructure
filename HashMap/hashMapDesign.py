class hashMap:
    def __init__(self, hashMapSize = 10):
        self.hash_data = [None] * hashMapSize
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.hash_data)
        return my_hash
    
    def print_hashTable(self):
        for key, value in enumerate(self.hash_data):
            print('Key {}: {}'.format(key, value))

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.hash_data[index] == None:
            self.hash_data[index] = []
        self.hash_data[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.hash_data[index] is not None:
            for i in range(len(self.hash_data[index])):
                #Traverse through the list at that index of the hashtable
                if self.hash_data[index][i][0] == key:
                    return self.hash_data[index][i][1]
                    #Look at the hash_data of the index of the hashtable 
                    #Traverse through the position of that list
                    #Get the first index (0) of the key
        return None

my_hash_table = hashMap()

# my_hash_table.set_item('Sam', 10)
# my_hash_table.set_item('Tom', 30)
# my_hash_table.set_item('Luis', 300)
# my_hash_table.set_item('Abe', 40)
# my_hash_table.set_item('Jack', 50)
# my_hash_table.set_item('Cruise', 100)

# my_hash_table.print_hashTable()
# print(my_hash_table.get_item('Tom'))
# print(my_hash_table.get_item('Abe'))
# print(my_hash_table.get_item('Cruise'))
# print(my_hash_table.get_item('ABC'))

num = int(input())
for index in range(num):
    name, phoneNum = input().split()
    my_hash_table.set_item(name, phoneNum)
name = input()
for index in range(name):
    name = input()

my_hash_table.print_hashTable()
