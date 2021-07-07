import  os # operating system 作業系統

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
				for line in f:
					if '商品,價格' in line:
						continue # 繼續 跳到下一個迴圈 不執行7-8行
					name, price = line.strip().split(',') #先刪除換行符號 再以逗號切割字串
					products.append([name, price]) 
	return products # 有改變數值 所以要return


# 讓使用者輸入
def user_input(products):
	while True: #不確定存幾次 用while loop
		name = input('請輸入商品名稱：')
		if name == 'q': 
			break
		price = input('請輸入商品價格:')
		price = int(price)
		products.append([name, price]) #大清單裡裝小清單 二維清單
	print(products)
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename , products):
	with open(filename, 'w', encoding = 'utf-8') as f: #read(r) write(w) 避免語文編碼跑掉
		f.write('商品,價格\n') #在for loop前先加入欄位
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')  #使用加法來將字串合併 

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案存在
		print('yeah!找到檔案囉')	
		products = read_file(filename) 	
	else:
		print('找不到檔案QQ')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
