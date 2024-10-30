socks = []
line = ""
paired = True
with open("input.txt") as f: 
    flag = False
    for line in f: 
        socks.append(line)
    socks.pop()
    for j in socks: 
        if socks.count(j) == 1:
            print(j, end="")
            paired = False
    if paired: 
        print("No lost socks")
            
        
    #     sock = line.split(" ")
    #     if sock != ['END', 'END', 'END\n']: 
    #      socks.append(sock)
    # for j in socks: 
    #     if socks.count(j) == 1: 
    #         for f in j: 
    #             line += f + " "
    #         print(line)
    #         line = ""
    #         flag = True
    # if not flag: 
    #     print("No lost socks")
        
        
   # print(socks)