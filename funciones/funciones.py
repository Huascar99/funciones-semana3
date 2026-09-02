#sumar dos numeros y mostrar el resultado.
def getSum(number1, number2):
    return number1  + number2

def show(message, result):
    return f"{message} {result}"

num1 = float(input("elige el primer numero: "))
num2 = float(input("elige el segundo numero: "))

sum = getSum(num1, num2)
print(show("La suma total es: ", {sum}))

