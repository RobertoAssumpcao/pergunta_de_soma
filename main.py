#import
import random

#iniciando variavel
acertos = 0

#gerando numero
numero_a = random.randrange(1, 100)
numero_b = random.randrange(1, 100)

#pergunta
resposta = int(input(f"Quanto é {numero_a} + {numero_b} ? \n"))

# soma numero
resultado = numero_a + numero_b

#resposta
print(f"A resposta é {resultado}")

#contando acerto
if resposta == resultado:
    acertos = acertos + 1
else:
    print("Resposta errada\n")
    
# ---------------------------------------------------------------- 2 -------------------------------

#gerando numero
numero_a = random.randrange(1, 100)
numero_b = random.randrange(1, 100)

#pergunta
resposta = int(input(f"Quanto é {numero_a} + {numero_b} ? \n"))

# soma numero
resultado = numero_a + numero_b

#resposta
print(f"A resposta é {resultado}")

#contando acerto
if resposta == resultado:
    acertos = acertos + 1
else:
    print("resposta errada")
    
print(f"Voce acertou {acertos} vezes")


