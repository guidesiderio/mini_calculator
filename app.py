# Crie uma função para cada operação matemática
def soma(x, y):
    return x + y

def subtrai(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    resultado = 0
    try:
        resultado =  x / y
    except:         
        print('Error! Não é possível dividir por zero!')

    return resultado     
   
# Crie uma função que dado dois valores reais, chame e execute as 4 funções matemáticas criadas anteriormente   
def executa_operacoes(x, y):
    print(f'{valor1_float} + {valor2_float} = {soma(x, y):.2f}')           
    print(f'{valor1_float} - {valor2_float} = {subtrai(x, y):.2f}')           
    print(f'{valor1_float} * {valor2_float} = {multiplica(x, y):.2f}')           
    print(f'{valor1_float} / {valor2_float} = {divide(x, y):.2f}')           

# Solicite dois valores reais para o usuário
valor1 = input('Digite o primeiro valor: ')           
valor2 = input('Digite o segundo valor: ')   

valor1_float = float(valor1)
valor2_float = float(valor2)

executa_operacoes(valor1_float, valor2_float)
