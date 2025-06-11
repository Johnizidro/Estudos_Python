#Exemplo de uso de input
anything = input("Conta-me qualquer coisa...")
print("Hum...", anything, "...Realmente?")

#Conversão de String para inteiro
anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)

#Exemplode aplicação
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("O comprimento da hipotenusa é", hypo)

#Concatenação de String
fnam = input("Posso ter seu primeiro nome, por favor? ")
lnam = input("Posso ter seu sobrenome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é " + fnam + " " + lnam + ".")

#Modelo utilizando contas aritimeticas com entrada de dados
a = float(input("Entre com o primeiro valor: "))
b = float(input("Entre com o segundo valor: "))
print("Adição:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("\nIsso é tudo, pessoal!")