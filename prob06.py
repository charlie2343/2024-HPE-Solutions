with open("input.txt", "r") as file: 
    data = [i for i in file.read().strip().split('\n')]
    data.pop(0)
    
    for line in data:
        name, year, month = line.split(" ")
        year = int(year)
        month = int(month)
        
        months = year * 12 + month
        
        hours = 300 - months
        
        print(f"{name} {hours}")