
def decimalToBinary(n):

	if(n > 1):
		decimalToBinary(n//2)

	
	print(n%2, end=' ')
	
	
if __name__ == '__main__':
	decimalToBinary(int(input('Введите десятичное число: ' "\n")))

print()


# binary to decimal
def binaryToDecimal(n):
	num = n;
	dec_value = 0;
	base1 = 1;
	len1 = len(num);
	for i in range(len1 - 1, -1, -1):
		if (num[i] == '1'):	
			dec_value += base1;
		base1 = base1 * 2;
	
	return dec_value;

num = input("Введите двоичное число: " "\n");
print(binaryToDecimal(num));