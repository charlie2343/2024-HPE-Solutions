nums = input().split(" ")
text = ""
for num in nums:
    num = int(num)
    text += chr(num)
    
print(text)