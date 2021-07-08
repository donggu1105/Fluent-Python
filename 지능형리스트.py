

symbols = 'ABCDE'
symbols2 = '123456'
dummy = [ord(s) for s in symbols]

print(dummy)


lambda_dummy = list(filter(lambda c : c < 127, map(ord, symbols)))

lambda_dummy2 = list(map(lambda x : ord(x), symbols))

lambda_dummy3 = list(filter(lambda x : int(x) > 3, symbols2))
print(lambda_dummy)
print(lambda_dummy2)
print(lambda_dummy3)