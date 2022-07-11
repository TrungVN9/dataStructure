class hashMap:
    #Initialize hashMap as a dict
    def __init__(self):
        self.hashMap = {} #HashMap contains a key and value
    
    #Pass key and value to hashMap
    def put(self, key, value):
        self.hashMap[key]= value
    
    def get(self, key):
        if key in self.hashMap:
            return self.hashMap[key]
        return -1
    
    def remove(self, key):
        if key in self.hashMap:
            return self.hashMap.pop(key)

if __name__=="__main__":
    myHashMap = hashMap()
    myHashMap.put(3, 30)
    myHashMap.put("Hello", 10)
    # print(myHashMap.get("Hello"))
    my_dict = {'sam': '123', 'luis': '11233', 'bob': '1093'}
    print(my_dict.values())