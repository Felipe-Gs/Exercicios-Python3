#fibonacci
def fibonacci(a):
    if a==1:
        return 0
    elif a==2:
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)
def menu():
    a = int(input('Exibir ate o termo (maior que 2): '))
    for c in range(1,a+1):
        print(fibonacci(c))
menu()    

#a. Crie a versão não recursiva da mesma função.
def fibo(n):
  if n == 1:
    return 0
  elif n == 2:
      return 1
  else:
    return fibo(n-1) + fibo(n-2)
n = int(input(' digite o numero: '))
print(fibo(n))