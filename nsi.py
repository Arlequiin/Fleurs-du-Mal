import sys
a=1
while a!=0.0:
    a=a/10
    print(a)
print(a<sys.float_info.epsilon)