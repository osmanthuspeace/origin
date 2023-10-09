import sys
def cat():
	print("Meow")
def fun():
	print("hello")
def main():
	if sys.argv[1] == 'cat':
		cat()
	else:
		fun()
if __name__== "__main__":
	main()
