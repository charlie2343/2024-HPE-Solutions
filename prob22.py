with open("input.txt") as f: 
    def draw_grid(): 
        size = input[2]
        for i in range(0,size): 
            if i < 10: 
                print("0" + str(i))
            else: 
                print("10")
    
    for line in f: 
        input = line.split(" ")
        for i in range(0,len(input)): 
            input[i] = int(input[i])
        print(input)
        draw_grid()
        
        

        
        
        