from time import sleep

menu = """
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_formatado = 0.0

while True:

    opcao = input(menu).lower()


    if opcao == 'd':
        # Operação de deposito 

        print('\nFunção Deposito')

        while True:
            deposito = input("\nValor do deposito: R$ ").strip()
            try:
                deposito = float(deposito)
                
            except:
                print("\nErro Valor invalido!!")
                print("Tente Novamente")

            aux = f"{deposito:.2f}"
            deposito = float(aux)

            if deposito <= 0:
                print("\nErro Valor invalido!!")
                print("Tente Novamente")
            
            else:
                saldo += deposito
                break
        
        deposito_formatado = str(f"{deposito:.2f}").replace("." , ",")

        print(f"\nO valor de R$ {deposito_formatado} foi depositado com sucesso! ")

        extrato += f"deposito: R${deposito_formatado}\n"

    elif opcao == 's':
    
        if numero_saques != LIMITE_SAQUES:

            limite_formatado = str(f"{limite:.2f}").replace("." , ",")

            print("\nFunção Saque")        
            print(f"\nValor limite de saque R${limite_formatado} ")    
            print(f"Limite de saques diarios disponiveis ({LIMITE_SAQUES - numero_saques})")
            print(f"Limite diario ({LIMITE_SAQUES})")

            while True:
                resposta = ""
                saque = input('\nValor no qual deseja sacar: R$ ').strip()

                try:
                    saque = float(saque)
                
                except:
                    print("\nErro Valor invalido!!")
                    print("Tente Novamente...")

                aux = f"{saque:.2f}"
                saque = float(aux)

                saque_formatado = str(f"{saque:.2f}").replace("." , ",")
                saldo_formatado = str(f"{saldo:.2f}").replace("." , ",")

                if saque <= 0:
                    print("\nErro Valor invalido!!")
                    print("O valor digitado é menos que 0!!")
                    
                    while True:
                        resposta = input(f"Deseja tentar novamente?  ").strip().lower()[0]  
                            
                        if resposta == "s":
                            resposta == None
                            break

                        elif resposta == "n":
                            break

                        else:
                            print("Error!")
                            print("Resposta invalida!!")

                elif saque > limite:
                    print("\nValor limite para saques exedido")
                    print("Tente Novamente...")

                elif saque > saldo:
                    print("\nError!")
                    print("valor solicitado maior do que o salda da conta") 
                    print(f"Você solicitou R${saque_formatado}, mas possui um saido de R${saldo_formatado}")

                    while True:
                        resposta = input(f"Deseja sacar os R${saldo_formatado} que você tem disponivel? ").strip().lower()[0]

                        if resposta == "s":
                            saque = saldo
                            continue

                        elif resposta == "n":
                            print('Não sera possivel realizar o saque por falta de saldo!')
                            break

                        else:
                            print("Error!")
                            print("Resposta invalida!!")

                else:
                    break


            saldo -= saque
            numero_saques += 1

            print(f"\nO valor de R${saque_formatado} foi sacado com sucesso! ")

            extrato += f"saque: R${saque_formatado}\n"


        
        else:
            print("\nLimite diario de saque atingindo!")
            print("Tente novamente amanhã...")

    elif opcao == 'e':
        saldo_formatado = str(f"{saldo:.2f}").replace("." , ",")
        if extrato != "":

            print("Gerando Extrato Bancario...")

            sleep(2)

            print(f"\nSaldo Bancario: R${saldo_formatado}")
            print(f"\n{extrato}")

        else:
            print("\nNão foram feitas movimentações bancarias...")

        
    
    elif opcao == 'q':
        print("Encerando o sistema...")
        break

    else:            
        print('\nOPÇÃO INVALIDA!')
        print('Por favor, selecione um opção valida!')