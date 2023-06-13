matriz = [ 

    ["*", "*", "*"], 

    ["*", "*", "*"], 

    ["*", "*", "*"] 

] 

 
 

jogador_atual = "X" 

 
 

while True: 

    for linha in range(3): 

        print(matriz[linha]) 

 
 

    if jogador_atual == "X": 

        jogador = "Jogador X" 

        marca = "X" 

    else: 

        jogador = "Jogador O" 

        marca = "O" 

 
 

    escolha = int(input(f"{jogador}, escolha a posição (1-9): ")) 

 
 

    if escolha >= 1 and escolha <= 9: 

        if escolha == 1: 

            matriz[0][0] = marca 

        elif escolha == 2: 

            matriz[0][1] = marca 

        elif escolha == 3: 

            matriz[0][2] = marca 

        elif escolha == 4: 

            matriz[1][0] = marca 

        elif escolha == 5: 

            matriz[1][1] = marca 

        elif escolha == 6: 

            matriz[1][2] = marca 

        elif escolha == 7: 

            matriz[2][0] = marca 

        elif escolha == 8: 

            matriz[2][1] = marca 

        elif escolha == 9: 

            matriz[2][2] = marca 

    else: 

        print("Escolha inválida. Tente novamente.") 

        continue 

 
 

    # Verificar vitória 

    # Verifica linhas 

    for linha in matriz: 

        if linha.count(marca) == 3: 

            print(f"O {jogador} venceu!") 

            exit() 

 
 

    # Verifica colunas 

    for coluna in range(3): 

        if matriz[0][coluna] == marca and matriz[1][coluna] == marca and matriz[2][coluna] == marca: 

            print(f"O {jogador} venceu!") 

            exit() 

 
 

    # Verifica diagonais 

    if matriz[0][0] == marca and matriz[1][1] == marca and matriz[2][2] == marca: 

        print(f"O {jogador} venceu!") 
        print(matriz)
        exit() 

    if matriz[0][2] == marca and matriz[1][1] == marca and matriz[2][0] == marca: 

        print(f"O {jogador} venceu!") 
        print(matriz)
        exit() 
    
 
 

    jogador_atual = "O" if jogador_atual == "X" else "X"