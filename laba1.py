#a^x**2+b^x+c=0
a=int(input())
b=int(input())
c=int(input())
print("Квадратное уравнение->"+str(a)+"*x^2+"+'('+str(b)+')'+"*x+"+'('+str(c)+')'+"=0")
D=b**2-4*a*c
if D<0:
    print("Нет корней")
elif D==0:
    print(-b/(2*a))
else:
    print((-b+D**0.5)/2*a,(-b-D**0.5)/2*a)