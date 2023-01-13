#	lambda arguments : expression

'''
x = lambda a: a + 10
print(x(5))
'''

'''
x = lambda a, b : a * b
print(x(5, 6))
'''

'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))
'''


'''def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
'''

'''store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_rs = lambda data: (data[0], data[1]*0.82)

store_rs = list(map(to_rs, store))


for i in store_rs:
    print(i)