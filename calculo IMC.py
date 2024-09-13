#Calculo do IMC
#Formula: peso / altura²
#Passo 1: Pedir pro usuario digitar seu peso (colocar numa variavel chamada p)
#Passo 2: Pedir pro usuario digitar sua altura (colocar numa variavel chamada "a")
#Passo 3: Criar uma variavel chamada "imc" onde irá conter o calculo do imc
#Passo 4:Criar if  que defina se esta abaixo do peso, acima do peso ou peso normal
print("Calculo de IMC")
p= float(input('Digite seu peso: '))
a= float(input('Digite sua altura: '))
imc= p / (a * a)
if imc < 18.5:
    print('{}, Você está abaixo do peso! '.format (imc))
if imc >= 18.5 and imc <= 24.9:
    print('{}, Você está no peso normal! '.format (imc))
if imc >= 25 and imc <= 29.9:
    print('{}, Você está acima do peso! '.format (imc))
    


