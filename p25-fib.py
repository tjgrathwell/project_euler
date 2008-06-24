def fib():
  fibs = [1,1]
  yield 1
  while(1):
    yield fibs[-1]
    fibs.append(fibs[-1]+fibs[-2])
    
fibmaker = fib()
i = 0
current = fibmaker.next()
while (len(str(current)) < 1000 ):
  current = fibmaker.next()
  i += 1
print i+1