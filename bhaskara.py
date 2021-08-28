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
        a = float(a)
        b = float(b)
        c = float(c)
        delta = b**2-4*a*c
        print(f"Δ = {delta:.2f}")

        #bhaskara
        if delta > 0:
            raiz_delta = math.sqrt(delta)
            x1 = (-b + raiz_delta) / 2*a
            x2 = (-b - raiz_delta) / 2*a
            print(f"x' = {x1:.2f}")
            print(f"x'' = {x2:.2f}")

        elif delta < 0:
            raiz_delta_neg = delta * -1
            raiz_delta_neg = math.sqrt(raiz_delta_neg)
            x1 = (-b + raiz_delta_neg) / 2*a
            x2 = (-b - raiz_delta_neg) / 2*a
            print(f"x' = {x1:.2f}i")
            print(f"x'' = {x2:.2f}i")
    except:
        print('Nao foi possivel calcular a conta com o valor recebido ;(')

baskara()
