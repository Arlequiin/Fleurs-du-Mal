def intdectobin(n):
  leftovers=[]
  while n//2!=0:
    leftovers.append(str(n%2))
    n=n//2
  leftovers.append(str(n%2))
  return ''.join(leftovers[::-1])
def fractionaltobin(n):
    l=[]
    for i in range(52):
       if n*2!=1:
        n*=2
        l.append(str(n)[0])
        if n>1:
            n-=1
    l.append('1')
    return ''.join(l)
def float2iee754_64(n):
  n=str(float(n)).split('.')
  n[0]=str(intdectobin(int(n[0])))
  n[1]=str(fractionaltobin(float('0.'+n[1])))
  return '.'.join(n)
print(float2iee754_64(10.2))
