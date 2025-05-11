def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    
    return a / b

def calculadora():
    print("=== Calculadora Python ===")
    print("Operações disponíveis:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    
    escolha = input("Escolha uma operação (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Use apenas números.")
            return

        if escolha == '1':
            resultado = somar(num1, num2)
            operador = '+'
        elif escolha == '2':
            resultado = subtrair(num1, num2)
            operador = '-'
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
            operador = '*'
        elif escolha == '4':
            resultado = dividir(num1, num2)
            operador = '/'

        print(f"\nResultado: {num1} {operador} {num2} = {resultado}")
    else:
        print("Opção inválida!")

# Executar a calculadora
calculadora()
