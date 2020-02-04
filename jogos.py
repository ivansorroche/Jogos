import forcadef
import adivinhacaodef

print("1 - Jogo da adivinhação")
print("2 - Jogo da forca")

escolha = int(input("Digite sua escolha: "))

if escolha == 1:
	adivinhacaodef.adivinhacao()

elif escolha == 2:
	forcadef.forca()


