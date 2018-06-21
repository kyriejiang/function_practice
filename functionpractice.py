#question 1 
def f(x):
    return 6 * x - 4
print(f(4))
print(f(5))
print(f(6))
print(f(7))

#question 2
def f(n) :
	return 1 / (3**n-1)
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))

#question 3
def f(n):
	return (-1**n) * (3)
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))

#question 4
def f(x):
	return 250 * 0.07 * x + 250
print(f(1))
print(f(3))
print(f(7))
print(f(20))

#question 5
def f(n):
	return 325 * (1.04 ** n)
print(f(1))
print(f(3))
print(f(7))
print(f(20))

#question6  sorry, Mr.kalu, i don't know how to do this one 

	

#function worksheet

# Question 1
def m(h):
	return 1000 + (100 * h)


# Question 2
def b(m):
	return m / 20

#quetion3
def b(m, k):
    return lambda k: b(m(k))
def double(m):
    return 1000 + (100 * m)
def inc(k):
    return k / 20

#quetion 4    
def m(h):
	return 1000 + (100 * h)/20
print(m(5))
#quetion 5
def m(h):
	return ((h * 20) - 1000)/100
print(m(100))