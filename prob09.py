with open("input.txt", "r") as file: 
    data = [i for i in file.read().strip().split('\n')]
    data.pop()
    
    for line in data:
        text = ""
        i = 0
        while (i <= len(line)-2):
            if line[i] == " ":
                text += line[i]
            if line[i].isalpha:
                if line[i] == line[i+1]:
                    text += line[i]
                    i += 2
                else:
                    i += 1
            else:
                text += line[i]
                i += 1
                
        print(text)