with open("input.txt", "r") as file: 
    data = [i for i in file.read().strip().split('\n')]
    data.pop()
    
    for i in range(len(data)):
        name, street, city, state, postalCode = data[i].split(", ")
        
        print(name)
        print(street)
        print(f"{city}, {state} {postalCode}")
        
        if (i != len(data)-1):
            print()