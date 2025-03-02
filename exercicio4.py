import random 

done = False

while not done:
    print ("O que você deseja fazer?")
    print ("1. Adivinhar um numero")
    print ("2. Sair")

    choice = input(">")

    if choice == "1":
        print("===Adivinhe um numero de 1 a 10===")
        number = int(input("Digite um numero de 1 a 10: "))
        result = random.randint(1,10)
        if number == result:
            print("Parabéns, você acertou!")
        else:
            print(f"Tente novamente. O numero sorteado foi {result}\n\n")
    elif choice == "2":
        done = True
    else:
        print("Opção inválida. Escolha uma opção entre 1 e 2")
        