#Condiçãod e igualdade
var = 0 # Atribuindo 0 a var
print(var == 0)

var = 1 # Atribuindo 1 a var
print(var == 0)

#outros tipos:  != : diferente,  >: Maior, <:Menor, >=: maior ou igual, <=:Menor ou igual

#Condição If Else
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
# Escolha o número maior
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprimir o resultado
print("O maior número é:", larger_number)

#Verificação de Ano
year = int(input("Digite um ano: "))

if year < 1582:
 print("Não dentro do período do calendário gregoriano")
else:
   if year % 4 != 0:
     print("ano comum")
   elif year % 100 != 0:
     print("Ano bissexto")
   elif year % 400 != 0:
     print("ano comum")
   else:
     print("Ano bissexto") 
 
 

