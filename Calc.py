# main.py - Calculadora Básica

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por 0 no permitida."

def main():
    print("Bienvenido a la calculadora básica")
    print("Opciones: sumar, restar, multiplicar, dividir")
    
    operacion = input("¿Qué operación deseas realizar? (sumar, restar, multiplicar, dividir): ").lower()
    
    if operacion in ["sumar", "restar", "multiplicar", "dividir"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if operacion == "sumar":
            resultado = sumar(num1, num2)
        elif operacion == "restar":
            resultado = restar(num1, num2)
        elif operacion == "multiplicar":
            resultado = multiplicar(num1, num2)
        elif operacion == "dividir":
            resultado = dividir(num1, num2)
        
        print(f"Resultado: {resultado}")
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    main()
