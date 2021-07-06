import  os # operating system 作業系統

# 讀取檔案
products = []

if os.path.isfile('products.csv'): # 檢查檔案存在
	print('yeah!找到檔案囉')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續 跳到下一個迴圈 不執行7-8行
			name, price = line.strip().split(',') #先刪除換行符號 再以逗號切割字串
			products.append([name, price]) 
	print(products)

else:
	print('找不到檔案QQ')


# 讓使用者輸入
while True: #不確定存幾次 用while loop
	name = input('請輸入商品名稱：')
	if name == 'q': 
		break
	price = input('請輸入商品價格:')
	price = int(price)
	products.append([name, price]) #大清單裡裝小清單 二維清單
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f: #read(r) write(w) 避免語文編碼跑掉
	f.write('商品,價格\n') #在for loop前先加入欄位
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  #使用加法來將字串合併 