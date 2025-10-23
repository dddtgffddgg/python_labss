def f():
	a = 'hello'
	def q():
		nonlocal a 
		a = 30 
	q()
	print(a)
f()

