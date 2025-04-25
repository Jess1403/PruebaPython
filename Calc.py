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
    
    operacion = "sumar"  # Establece la operación de forma predeterminada
    num1 = 5  # Número de prueba
    num2 = 3  # Número de prueba
    
    if operacion in ["sumar", "restar", "multiplicar", "dividir"]:
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
