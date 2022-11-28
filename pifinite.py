def intdectobin(n):
  
  leftovers=[]
  while n//2!=0:
    leftovers.append(str(n%2))
    n=n//2
  leftovers.append(str(n%2))
  return ''.join(leftovers[::-1])
def fractionaltobin(n,bits=64):
  if bits==64:
    mantisse=52
    expo=11
  else:
    mantisse=24
    expo=8
    l=[]
    for i in range(mantisse):
       if n*2!=1:
        n*=2
        l.append(str(n)[0])
        if n>1:
            n-=1
    l.append('1')
    return ''.join(l)
def float2iee754(n,bits=64):
  if bits==64:
    mantisse=52
    expo=11
  else:
    mantisse=24
    expo=8
  n=str(float(n)).split('.')
  p=0
  if n[0].isdigit():
    sign='+'
    sign2='0'
  else:
    sign='-'
    sign2='1'
  n[0]=str(intdectobin(abs(int(n[0]))))
  n[1]=str(fractionaltobin(float('0.'+n[1])))
  while len(n[0])!=1:
    n[1]=n[0][-1]+n[1]
    n[0]=n[0][:-1]
    p+=1
  return [(sign+'.'.join(n)+f"{(mantisse-len(n))*'0'} IEE({p})").replace('None',''),sign2+' '+f"{intdectobin(p)+(expo-len(intdectobin(p)))*'0'} {''.join(n)+(mantisse-len(n))*'0'}".replace('None','')]

print(float2iee754(3.5,32))