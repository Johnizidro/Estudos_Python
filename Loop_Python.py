#Exemplo iniciald e um loop
for i in range(10):
   print("O valor de i é atualmente", i)

#Utilizaçãod do loop com expressões aritimeticas
power = 1
for expo in range(16):
  print("2 à potência de", expo, "é", power)
  power *= 2


#Utilização do Break para quebra do loop
print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")

#Programa que análisa qual é o maior número
largest_number = -99999999
counter = 0

while True:
    number = int(input("Digite um número ou digite -1 para terminar o programa: "))
    if number == -1:
        break
    counter += 1
    if number > maior_numero:
        maior_numero = number

if counter != 0:
    print("TO maior número é", maior_numero)
else:
    print("Você não inseriu nenhum número.")

#While e for utilizando Else

for i in range(5):
 print(i)
else:
 print("else:", i)

 i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
