print('Bem-vindo ao jogo de adivinhação')

numero_secreto = 28
chute = int(input('Adivinhe o número: '))
print("Você digitou:", chute)

if (chute == numero_secreto):
    print('Parabéns, você acertou!!!')

else:
    print('Tente novamente.')

print('Fim do jogo!')
