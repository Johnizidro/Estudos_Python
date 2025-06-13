
#Exemplos de listas
numbers = [10, 5, 7, 2, 1]
print("Conteúdo da lista original:", numbers) # Imprimindo conteúdo da lista de originais.

numbers[0] = 111
print("\nConteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

numbers[1] = numbers[4] # Copiando o valor do quinto elemento para o segundo.
print("Conteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

print ("\nComprimento da lista:", len (numbers)) # Imprimindo comprimento de lista anterior.


#Uso do delete para romeção de itens de uma lista

del numbers[1] # Removendo o segundo elemento da lista.
print ("Comprimento da nova lista:", len (numbers)) # Imprimindo novo comprimento da lista.
print ("\nNova lista de conteúdo:", numbers) # Imprimindo conteúdo da lista atual.

#Utilização do append e insert para inserção de numeros, e len para leitura do comprimento da lista

numbers = [111, 7, 2, 1]

print(len(numbers))

print(numbers)


numbers.append (4)


print(len(numbers))

print(numbers)


numbers.insert (0, 222)

print(len (numbers))
print(numbers)

#Utilização de loop para soma dos elementos de uma lista
my_list = [10, 1, 8, 3, 5]

total = 0

for i in range(len(my_list)):

  total += my_list[i]

print(total)




