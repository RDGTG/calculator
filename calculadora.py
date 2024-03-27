def calcular(a,b,operador):
    if operador=='+':
        return a+b
    elif operador =='-':
        return a-b
    elif operador == '*':
        return a*b
    elif operador == '/':
        if a!=0 and b!=0:
            return a/b
        else:
            return "erro na divisão"

while True:   
    num1 =float(input("digite o primeiro numero ou (-1) para sair: "))
    if num1 < 0:
        break
    op= input("digite o operador (+, - , *, /) ")

    num2 =float(input("digite o segundo numero (-1) para sair: "))
    if num2 < 0:
        break
    

    print("reultado do calculo: ", calcular(num1,num2,op))