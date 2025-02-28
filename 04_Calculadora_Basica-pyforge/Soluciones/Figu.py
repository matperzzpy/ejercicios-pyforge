num1=int(input("ingrese el primer numero :"))
num2=int(input("ingrese el segundo numero :"))
operacion = input("que operacion desea realizar :")
result = "El resultado es :"
suma= num1 + num2
resta= num2 - num1
multiplicacion= num1 * num2
division = num1 / num2 

if operacion == "suma":
    print(result,suma)
elif operacion == "resta":
    print(result,resta)
elif operacion == "multiplicacion":
    print(result,multiplicacion)
elif operacion == "division" and operacion  != 0 :
    print(result,division)
else :
    print("operacion invalida")

