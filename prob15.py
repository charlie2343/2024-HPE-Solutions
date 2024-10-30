molecules = input().split("(")[0]
molescules = molecules.rstrip()


index1 = 0
index2 = 0
output = ""
output2 = ""
for char in molecules: 
    
    if char.isalpha(): 
        output += " "
    else: 
        output += char
        
for char in molecules: 
    
    if char.isdigit(): 
       
       output2 += " "
    else: 
        output2 += char
        
print(output2)      
print(output)
