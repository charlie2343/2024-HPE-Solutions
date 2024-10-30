stocks = {}

with open("input.txt") as f: 
    for line in f: 
        if (int(line) not in stocks): 
            stocks[int(line)] = 1
        else: 
            stocks[int(line)] += 1
    max = 0
    for stock in stocks: 
        count = stocks[stock]
        if count > max: 
            max = count 
            
    for stock in stocks: 
        if stocks[stock] == max: 
            print(f"Trending: {stock} [{stocks[stock]} count]")
            stocks.pop(stock)
        break
            
    for stock in stocks: 
        count = stocks[stock]
        if count > max: 
            max = count 
            
    for stock in stocks: 
        if stocks[stock] == max: 
            print(f"Second Place: {stock} [{stocks[stock]} count]")
            
        
        
   