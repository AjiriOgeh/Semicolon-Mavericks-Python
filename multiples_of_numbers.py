four = 4
onethousandandtwentyfour = 1024
two = 2
ten = 10

remainder1 = 1024 % 4
remainder2 = 2 % 10

if remainder1 == 0:
	print(onethousandandtwentyfour,"is a multiple of", four)
else:
	print(onethousandandtwentyfour,"is a not multiple of", four)	

if remainder2 == 0:
	print(two,"is a multiple of", ten)
else:
	print(two,"is not a multiple of", ten)