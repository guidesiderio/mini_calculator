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