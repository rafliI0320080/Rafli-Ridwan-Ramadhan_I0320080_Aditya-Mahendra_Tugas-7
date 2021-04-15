import time
def hitungmundur(n):
	li = (n)
	def next():
		r= li(0)
		li[0] -= 1
		return r
	return next
def main():
	next = hitungmundur(3)
	while true :
		val = next()
		if val == 0:
			print("Go!")
			break
		print(val, end="")
		time.sleep(1)
		main()
