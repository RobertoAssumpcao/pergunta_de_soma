#import
import random

#iniciando variavel
acertos = 0

#gerando numero
numero_a = random.randrange(1, 100)
numero_b = random.randrange(1, 100)

# soma numero
resultado = numero_a + numero_b

#pergunta
resposta = int(input(f"Quanto é {numero_a} + {numero_b} ? \n"))

#resposta
print(f"A resposta é {resultado}")

#contando acerto
if resposta == resultado:
    acertos = acertos + 1
    
    
# ---------------------------------------------------------------- 2 -------------------------------

#gerando numero
numero_a = random.randrange(1, 100)
numero_b = random.randrange(1, 100)

# soma numero
resultado = numero_a + numero_b

#pergunta
resposta = int(input(f"Quanto é {numero_a} + {numero_b} ? \n"))

#resposta
print(f"A resposta é {resultado}")

#contando acerto
if resposta == resultado:
    acertos = acertos + 1
    
print(f"Voce acertou {acertos} vezes")


