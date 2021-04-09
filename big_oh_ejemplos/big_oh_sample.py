import os, random

uid_counter = 0

def update_uid_counter():
        global uid_counter
        uid_counter =   uid_counter + 1
        return

def get_uid_counter():
    global uid_counter

    return uid_counter

class Box:
    
    name = "Box"#class variable
    def __init__(self, price, name=0):
        '''instance variable'''
        self.name = name
        self.value = price
        self.uid = get_uid_counter()
        update_uid_counter()
        return

    def __str__(self):
        return "Box {}: \t value stored: {}".format(self.get_uid(), self.get_value())
    
    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value
        return
    
    def get_uid(self):
        return self.uid

    def set_uid(self, new_value):
        self.uid = new_value
        return 
    
    

def box_example():

    max_boxes = 4
    boxes = []
    for i in range(max_boxes):
        boxes.append(Box(random.randint(0,10_000)))

    # for box in boxes:
    #     print(box)
    

    print(boxes[0])

    # len(boxes) -> n
    print(str(boxes[0]))
    return

def main(n=10_000):

    #O(1)
    a=10
    #O(1)
    if a < 20:
        #O(1)
        print(a)
    # total O(3) -> O(1)
    
    #O(n)
    for i in range(n * n):

    # lim 0 -> (n * (n-1))

        print(i)

        # n**2 - n 
        # O(n ** 2) - O(n)


    #O(n) + O(3)
    # Simplifies ->O(n)

if __name__ == "__main__":

    box_example()