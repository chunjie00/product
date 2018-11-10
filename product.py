import os
product =[]

#读取档案
if os.path.isfile('product.csv'): #测试档案存不存在
	print('已找到档案!')
	with open('product.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name, price])
	print(product)
else:
	print('找不到档案...')

#让使用者输入
while True:
	name = input('请输入商品名称:')
	if name == "q":
		break
	price = input('请输入价格:')
	product.append([name,price])
print(product)

#印出所有购买记录
for p in product:
	print(p[0],'的价格是', p[1])

#写入档案
with open ('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品,价格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')