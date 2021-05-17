stock = {'pommes':18, 'bananes':7, 'tomates':12}

stock1 = dict()
stock2 = {}

alphabet = "abcdefghijklmnopqrstuvwxyz"
dictalph = {x:alphabet[x] for x in range(len(alphabet))}
print(dictalph)

fonction = {x:((x**2)+4*x+1) for x in range(-5,2)}

fruits = [("pommes",18),("bananes",7),("poires",12)]
stockList = {element[0]:element[1] for element in fruits}

stock['pommes'] = 10
stock['oranges'] = 25
del(stock['tomates'])

print(stock)
