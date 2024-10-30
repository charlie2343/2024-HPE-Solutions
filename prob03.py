with open("input.txt", "r") as file: 
    data = [i for i in file.read().strip().split('\n')]
    data.pop()
    for num in data: 
        if int(num) != 1: 
            print(f"You, {num} minutes ago.")
        else: 
            print(f"You, {num} minute ago.")
            