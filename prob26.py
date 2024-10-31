escape = False
caught = False
time_interval = 0
h_pos = 0
a_pos = 0
with open('input.txt') as f: 
    for line in f: 
        items = line.split(",")
        print(items)
        for item in items: 
            item = item.strip()
        data = {item.split(":")[0].strip(): item.split(":")[1].strip() for item in items}
        
        a_pos = data["Start"]
        #print(a_pos)
        while not escape or not caught: 
            time_interval += 1
            h_pos += int(data["Run"])
            print(h_pos)
        if h_pos >= data["Exit"]: 
            print("MADE IT!")
            escape = True
        
        #print(data)