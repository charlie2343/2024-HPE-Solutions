line = input()
count = 0
data = []
newd =[]

String = ""
for char in line: 
    data.append(char)
    
for num in range(0,len(data)-1): 
    c1 = data[num]
    if c1 == data[num+1]:
        count += 1
    else: 
        newd.append([data[num],count])
        count = 0


for data in newd: 
    if data[1] == 3: 
        String += data[0]
    
if String == "" :
    print("No Four of a Kind")
else:
    print(String)
