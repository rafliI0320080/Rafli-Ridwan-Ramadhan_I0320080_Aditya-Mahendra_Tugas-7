def panggil(func):
	return func
def helloworld():
	return "HELLO WORLD"
def main():
	s = panggil(helloworld())
	print(s)
	if __name__ == '__main__':
		main()