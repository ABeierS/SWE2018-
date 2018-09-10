import sys


def rle_encoder(txt):

	c = txt[0]
	i = 1
	res = []
	for x in txt[1:]:
		if x == c:
			i += 1
		else:
			res.append(f'{c}{i}')
			c = x
			i = 1
	res.append(f'{c}{i}')
	return ''.join(res)

def rle_decoder(txt):
	res = []
	c = txt[0]
	counter = 1
	for x in txt[1:]:
		ic = 0
		if x.isdigit() and (counter %2 == 1):
			i = int(x)
			while ic < i :
				res.append(f'{c}')
				ic += 1
		else:
			c = x
		counter += 1
	return ''.join(res)
	
if __name__ == "__main__":
	args = sys.argv
	if len(args) > 2:
		if args[1] == '-d':
			print(rle_decoder(args[2]))
		elif args[1] == '-e':
			print(rle_encoder(args[2]))
	
