# Crie uma função para cada operação matemática

def soma(x, y):
    return x + y

def subtrai(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except:         
        return print('Error! Não pode pode dividir por zero!')    

valor1 = input('Digite o primeiro valor: ')           
valor2 = input('Digite o segundo valor: ')   

valor1_float = float(valor1)
valor2_float = float(valor2)
