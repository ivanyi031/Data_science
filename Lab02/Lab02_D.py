class MyEnumerate():
    def __init__(self, data, label):
        #TODO_D
        self.data = data
        self.label = label
        self.end=len(label)
    def __iter__(self):
        #TODO_D
        self.num=0
        return self
        

    def __next__(self):
        #TODO_D
        if (self.num >= self.end):
            raise StopIteration
        
        #print(index)
        data=(self.num,self.data[self.num],self.label[self.num])
        self.num +=1
        return data

def main():

    data = [[174, 63], [165, 45], [168, 61], [180, 85], [163, 52]]
    label = ['male', 'female', 'male', 'male', 'female']

    for index, info, target in MyEnumerate(data, label):
        print(f"id:{index} | height:{info[0]} weight:{info[1]} -> {target}")

    # the output should look like the following:
    # id:0 | height:174 weight:63 -> male
    # id:1 | height:165 weight:45 -> female
    # id:2 | height:168 weight:61 -> male
    # id:3 | height:180 weight:85 -> male
    # id:4 | height:163 weight:52 -> female


if __name__ == "__main__":
    main()