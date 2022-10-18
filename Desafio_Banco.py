from time import sleep


saldo = 400.00
LIMITE_DIARIO = 3
qtd_saques = 0

vez = 0
f = 1
cont_pos = 0
cont_neg = 0
valores = []

while f == 1:

    print(f"""
=========Banco========

    Saldo: {saldo:.2f}
    1 - Depositar
    2 - Sacar
    3 - Extrato
    """)

    selecionar = int(input())

    while selecionar < 1 or selecionar > 3:
        selecionar = int(input())

    if selecionar == 1:
        n = float(input("Digite '0' para voltar ao menu\nDigite o valor do Deposito: "))
        while n < 0:
            n = input("Valor invalido, insira novamente: ")

        if n == 0:
            f = 0

        if n > 0:
            valores.append(n)
            cont_pos += 1
            saldo += n
            vez = 1
        sleep(1)

    if selecionar == 3:
        if vez == 0:
            print("Não foram relizadas movimentações")
            sleep(2)
        else:
            for i in range(0,cont_pos):
                if valores[i] > 0:
                    print(f"Deposito: R$ {valores[i]:.2f}")
                elif valores[i] < 0:
                    print(f"Saque: R$ {valores[i]:.2f}")
            
            sleep(1)
            print("\nDigite 0 para voltar: ")        
            while selecionar != 0:
                selecionar = int(input())
    if qtd_saques == LIMITE_DIARIO:
            print("Limite de saques diarios excedido")
            sleep(3)
    elif selecionar == 2 and qtd_saques != LIMITE_DIARIO:
            qtd_saques +=1
            n = float(input("Digite '0' para voltar ao menu\nDigite o valor do Saque: "))
            if n > saldo:
                print("Saldo insuficiente")
                qtd_saques -=1
                sleep(2)
            if n > 500:
                print("Saque deve ser menor que R$ 500.00")
                qtd_saques -=1
                sleep(2)
            elif n == 0:
                f = 0
                
            elif n > 0:
                saldo -= n
                n *=-1
                valores.append(n)
                cont_pos += 1
                vez = 1
