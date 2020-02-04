import random
def forca():
	""" Executa toda a logica do jogo da forca"""


	print("JOGO DA FORCA!!")

	palavra_secreta = "banana"
	letras_acertadas = []
	erros = 0
	ganhou = False
	enforcou = False
	frutas = []


	arquivo = open("arquivo.txt")


	#para cada linha do arquivo
	for linha in arquivo:
	#adiciona cada linha na variavel fruta	
		fruta = linha.strip()
	#adiciona cada fruta na lista de frutas que foi criada vazia
		frutas.append(fruta)

	arquivo.close()

	#cria uma variavel partindo de uma linha randomica da lista de frutas
	indice_aleatorio = random.randrange(0, len(frutas))

    # cria uma variavel com o indice aleatorio da lista de frutas
	palavra_secreta = frutas[indice_aleatorio]


 	#adiciona _para cada letra da palavra secreta 
	letras_acertadas = ["_" for letra in palavra_secreta]

	while (not ganhou and not enforcou):
		#pega a letra que o usuario chutou
		chute = input("chute uma letra: ")
		#verifica se o chute esta na palavra
		if chute.lower() in palavra_secreta:
			posicao = 0
			for letra in palavra_secreta:
				if chute.lower() == letra.lower():
					letras_acertadas[posicao] = letra
				posicao = posicao +1

		#para cada erro adiciona 1 a variavel erros quando chegar no 6 enforca
		else:
			erros += 1

		ganhou = "_" not in letras_acertadas
		enforcou = erros == 6

		print(letras_acertadas)
		
		

	if ganhou == True:
		print(f"Você ganhou a palavra é {palavra_secreta}!!!")
	else:
		print(f"Você perdeu, a palavra era {palavra_secreta}!!!")