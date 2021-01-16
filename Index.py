from Calculadora import Calculadora

calculadora = Calculadora()

numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))
resposta= int(input('Digite 1  para somar, 2 para dividir 3 para multiplcar, ou 4 subtrair'))
if resposta== 1 :
    print(calculadora.Soma(numero1,numero2))
if resposta== 2 :
    print(calculadora.Divisao(numero1,numero2))
if resposta== 3 :
    print(calculadora.Multiplicacao(numero1,numero2))
if resposta== 4 :
    print(calculadora.Subtracao(numero1,numero2))




