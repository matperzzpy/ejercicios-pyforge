""""
✨ Ejercicio de Lógica en Python: FizzBuzz ✨

✍️ Enunciado del Ejercicio

El programa pide al usuario que ingrese un número entero positivo y luego genera una secuencia de números desde 1 hasta el número ingresado. Para cada número de la secuencia se aplicará la siguiente lógica:

⚫ Si el número es múltiplo de 3, se imprimirá: Fizz.

⚫ Si el número es múltiplo de 5, se imprimirá: Buzz.

⚫ Si el número es múltiplo de ambos (3 y 5), se imprimirá: FizzBuzz.

⚫ Si el número no es múltiplo de 3 ni de 5, se imprimirá el número tal cual.

✨ Reglas del Programa

Pedir al usuario que ingrese un número entero positivo.

Validar que la entrada sea un número válido y mayor que 0.

Generar la secuencia de números y aplicar la lógica mencionada anteriormente.

⚡ Ejemplo de Salida

Si el usuario ingresa el número 15, el programa debería imprimir:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13  
14
FizzBuzz

"""

word_3 = "Fizz" #variable que guarda la palabra impresa si el número es múltiplo de 3
word_5 = "Buzz" #variable que guarda la palabra impresa si el número es múltiplo de 5


def input_number():
    """
    Solicita un número entero positivo al usuario.

    Returns:
        int: Número entero positivo ingresado por el usuario.

    Raises:
        ValueError: Si el usuario no introduce un número entero positivo.
    """
    
    
    while True:
        try:
            n = int(input("Introduce un número entero positivo: ")) #numero introducido por el usuario
            
            if n > 0:
                return n
            else:
                print("Introduce un número mayor que cero. Prueba otra vez")
        except ValueError as e:
            print(f"Entrada no válida: {e} Debe insertar un número entero positivo.")


def fizzbuzz(num):
    """ Imprime la secuencia FizzBuzz hasta el número dado. 
    Arguments:
        num (int): numero introducido por el usuario 
    """
    for n in range(1, num + 1):
        if not n % 3 == 0 and not n % 5 == 0:
            print(n)
        elif n % 3 == 0 and n % 5 == 0:
            print(f'{word_3}{word_5}')
        elif n % 3 == 0:
            print(f'{word_3}')
        elif n % 5 == 0:
            print(f'{word_5}')
        
        
if __name__ == '__main__':
    n = input_number()
    fizzbuzz(n)
    
