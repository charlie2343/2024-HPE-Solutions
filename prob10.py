with open("input.txt", "r") as file: 
    data = [i for i in file.read().strip().split('\n')]
    data.pop()
    
    for line in data:
        addend, sum = line.split("=")
        add1, add2 = addend.split("+")
        
        add1 = int(add1)
        add2 = int(add2)
        sum = int(sum)
        
        if (add1 + add2 == sum):
            print("CORRECT")
        else:
            sumReal = add1 + add2
            print(f"WRONG: {add1}+{add2}={sumReal}")
        