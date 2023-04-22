import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(10)]
generator = (n for n in range(10))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))
