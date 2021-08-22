import math

def baskara():
    #discriminante
    print('Nao digite o "x" nos valores pedidos, somente numeros (numeros flutuantes use ".")\n')
    a = input('Digite o valor de "A": ')
    b = input('Digite o valor de "B": ')
    c = input('Digite o valor de "C": ')
    print()

    try:
        delta = 0
        a = int(a)
        b = int(b)
        c = int(c)
        delta = b**2-4*a*c
        print(f"Δ = {delta}")

        #bhaskara
        if delta > 0:
            raiz_delta = math.sqrt(delta)
            x1 = (-b + math.sqrt(delta)) / 2*a
            x2 = (-b - math.sqrt(delta)) / 2*a
            print(f"x' = {x1}")
            print(f"x'' = {x2}")

        elif delta < 0:
            raiz_delta_neg = delta * -1
            raiz_delta_neg = math.sqrt(raiz_delta_neg)
            x1 = (-b + raiz_delta_neg) / 2*a
            x2 = (-b - raiz_delta_neg) / 2*a
            print(f"x' = {x1}i")
            print(f"x'' = {x2}i")
    except:
        print('Nao foi possivel calcular a conta com o valor recebido ;(')

baskara()