products = []

while True: #不確定存幾次 用while loop
	name = input('請輸入商品名稱：')
	if name == 'q': 
		break
	price = input('請輸入商品價格:')
	price = int(price)
	products.append([name, price]) #大清單裡裝小清單 二維清單
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w') as f: #read(r) write(w)
	f.write('商品,價格\n') #在for loop前先加入欄位
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  #使用加法來將字串合併 