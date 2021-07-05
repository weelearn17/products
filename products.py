products = []

while True: #不確定存幾次 用while loop
	name = input('請輸入商品名稱：')
	if name == 'q': 
		break
	price = input('請輸入商品價格:')
	products.append([name, price]) #大清單裡裝小清單 二維清單
print(products)

for p in products:
	print(p[0], '的價格是', p[1])