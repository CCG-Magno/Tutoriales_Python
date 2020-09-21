def while_loop_example():
    print("This is a while loop example...\n")
    i=0
    while i  < 5:
        print(f"[{i}] Hello world!")
    print()
    return

def for_loop_example():
    print('This is a for loop example...\n')
    for i in range(5):
        print(f"[{i}] Hello World!")
    print()
    return

def loop_sample():

    # i=0
    # while i <= 5:
    #     print(i)
    #     i+= 1
    # print("Termina loop")
    # key_pressed = False
    # while  not key_pressed :
    #     if i == 5:
    #         # key_pressed = True
    #         break
    #     print(f"[{i}] Hello World")
    #     i += 1
    # print("Game Start!")


    # names = ["a","b", "c"]
    # for i in names:
        
    #     print(f" Hello: [{i}]")
    #     if i == 'b':
    #         continue
        
        
            
        # i = i + 1
    #  Esto es un foreach -> un iterador para atravesar una coleccion de objetos
    # [0, 4]
    # # names = ["a","b", "c"]
    # for i in range(0,5, 2):
        
    #     print(f" Hello : [{i}]")
    #     # if i == 'b':
    #         # break
    while_loop_example()
    for_loop_example()
    return

def main():
    # print("Hello world!")
    loop_sample()
    pass

if __name__ == "__main__":
    main()