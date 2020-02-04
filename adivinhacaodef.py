def adivinhacao():


	print("***** JOGO DA ADIVINHAÇÃO ***** ")
	print(" ADIVINHE O NUMERO DE 0 a 100")


	numero = 42
	numero_tentativas = 3
	rodada = 1 


	while rodada <= numero_tentativas:
		print("Tentativa {} de {}".format(rodada, numero_tentativas))
		


		numero_digitado = int(input("Descubra o numero, digite: "))
		igual = numero == numero_digitado
		errado = numero_digitado >= 101 or numero_digitado < 0
		maior = numero_digitado > numero
		menor = numero_digitado < numero


		if igual:
			print("Você acertou, o numero é " + str(numero))
			break
		elif errado:
			print("Numero digitado invalido!")

		elif maior:
			print("Você errou o numero digitado é maior que o numero secreto")

		elif menor:
			print("Você errou o numero digitado é menor que o numero secreto")	


		rodada = rodada +1

	print("Fim do Jogo")