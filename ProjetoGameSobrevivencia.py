import os, random, time
os.system("cls")
os.system("color 2")
while True:
    print("""
     ____                         _           _        __   __             
    | __ )  ___ _ __ ___   __   _(_)_ __   __| | ___  / /__ \ \            
    |  _ \ / _ \ '_ ` _ \  \ \ / / | '_ \ / _` |/ _ \| |/ _` | |           
    | |_) |  __/ | | | | |  \ V /| | | | | (_| | (_) | | (_| | |           
    |____/ \___|_| |_| |_|   \_/ |_|_| |_|\__,_|\___/| |\__,_| |           
                     __ _  ___  ___                   \_\   /_/            
                    / _` |/ _ \/ __|                                    
                    | (_| | (_) \__\                                      
                    \__,_|\___/|___/                                      
        _  ___   ____  ___  ____    __  __  ___  ____ _____  _    ___ ____  
       | |/ _ \ / ___|/ _ \/ ___|  |  \/  |/ _ \|  _ \_   _|/ \  |_ _/ ___| 
    _  | | | | | |  _| | | \___ \  | |\/| | | | | |_) || | / _ \  | |\___ \ 
   | |_| | |_| | |_| | |_| |___) | | |  | | |_| |  _ < | |/ ___ \ | | ___) |
    \___/ \___/ \____|\___/|____/  |_|  |_|\___/|_| \_\|_/_/   \_\___|____/ 
    """)
    print("""
        === JOGOS MORTAIS ===

    Você não deveria estar aqui.

    Cada escolha será observada.

    Cuidado...

    Alguns jogadores não chegam ao fim.""")

    time.sleep(1000)
    os.system("cls")
    os.system("color 4")
    print("=== FASE 1: JOGO DE AZAR ===")
    numeroSorteado1=random.randint(1,3)
    print("Escolha um número de 1 a 3, pense bem no número que você vai escolher.......")
    respostaFase1=int(input("Tente adivinhar o número sorteado: "))
    if respostaFase1 == numeroSorteado1:
        print("""
    [PROCESSANDO...]""")
        time.sleep(4)
        print("""
    Resultado validado.
    ...Interessante. Você sobreviveu por enquanto.

    Preparando próxima fase...

    Boa sorte.""")
        time.sleep(4)
        os.system("cls")
    else:
        print("""
                === JOGOS MORTAIS ===

    HAHAHAHA... sério mesmo?

    Você conseguiu errar na PRIMEIRA FASE.
    Logo a opção MAIS simples.

    Que tipo de azar é esse?
    Ou será que é só falta de inteligência mesmo?

    Enquanto você pensava que tinha chance...
    o jogo já tinha decidido seu destino.

    Fim de jogo.

    Mais um azarado eliminado.""")
        perdeu_Game=True
        print("")
        jogarNovamente=input("Gostaria de jogar novamente? (s/n): ")
        if jogarNovamente=="s":
            os.system("cls")
            continue
        else:
            break
    print("")
    print("=== FASE 2: POTÊNCIA MORTAL ===")
    valorSorteado1=random.randint(1,10)
    valorSorteado2=random.randint(1,10)
    resultadoPotencia=int(valorSorteado1**valorSorteado2)
    print(resultadoPotencia) # RETIRAR ISSO DPS
    print(f"Qual o resultado de {valorSorteado1} na potência {valorSorteado2}") 
    respostaFase2=int(input("Digite sua resposta apenas com números: "))
    if respostaFase2==resultadoPotencia:
        print("")
        print("    [PROCESSANDO...]")
        time.sleep(4)
        print("")
        print("""
    === JOGOS MORTAIS ===

    Correto...

    Você resolveu.

    Impressionante...
    ou apenas sorte mais uma vez?

    Não importa.

    Você continua vivo.

    Mas não se engane.

    Cada acerto só torna sua queda...
    ainda mais interessante.
    Prepare-se para a próxima fase.""")
    else:
        print("")
        print("    [PROCESSANDO...]")
        time.sleep(4)
        print(f"""
    === JOGOS MORTAIS ===
            
    Curioso...

    Você não errou por pouco.
    Você errou completamente.
                
    Nenhuma surpresa.

    A diferença entre sobreviver e desaparecer
    era apenas um número.

    E você escolheu o errado.

    Você não faz mais parte do cálculo.

    [REMOVENDO ELEMENTO INVÁLIDO]

    ...

    Processo concluído.""")
        perdeu_Game=True
        print("")
        jogarNovamente=input("Gostaria de jogar novamente? (s/n): ")
        if jogarNovamente=="s":
            os.system("cls")
            continue
        else:
            break
    os.system("cls")
    print("Aguarde...")
    time.sleep(5)
    print("""
    === JOGOS MORTAIS ===

    [PROGRESSO...]

    Fase 3 alcançada.

    Você chegou à metade.

    Agora... começa a parte difícil

    Continue... se conseguir hahahahaha.""")
    time.sleep(5)
    os.system("cls")
    print("")    
    print("=== FASE 3: FÓRMULA DO DESESPERO ===")
    print("")
    print("Resolva a seguinte fórmula:")
    print("(respostaFase1 + respostaFase2) ^ respostaFase1 - respostaFase2")
    respostaFormula=((respostaFase1+respostaFase2)**respostaFase1)-respostaFase2
    print(respostaFormula) # RETIRAR DEPOIS
    respostaFase3=int(input("Digite sua resposta apenas com números: "))
    os.system("cls")
    if respostaFase3==respostaFormula:
        print("Avaliando suas chances de sobrevivência...")
        time.sleep(4)
        print("""
    === JOGOS MORTAIS ===

    ...

    Resposta correta.

    Interessante.

    Você manteve a calma,
    mesmo com a pressão aumentando.

    Poucos chegam até aqui.

    Mas não confunda isso com vitória.

    O jogo ainda não terminou.

    E a próxima fase...
    vai exigir ainda mais de você.

    Continue.""")
        os.system("cls")
    else:
        print("Avaliando suas chances de sobrevivência...")
        time.sleep(4)
        print(f"""
    === JOGOS MORTAIS ===

    ...

    Resposta incorreta.

    Você chegou longe.
    Mais longe do que muitos.

    Mas não o suficiente.

    Um cálculo.
    Um único erro.
    E tudo desmorona.


    O jogo não perdoa falhas.

    Fim de jogo.""")
        perdeu_Game=True
        print("")
        jogarNovamente=input("Gostaria de jogar novamente? (s/n): ")
        if jogarNovamente=="s":
            os.system("cls")
            continue
        else:
            break
    print("")
    print("=== FASE 4: JOGO DA MEMÓRIA ===")
    print("""
    === JOGOS MORTAIS ===

    Impressionante...

    Você atravessou as fases anteriores
    e ainda está de pé.

    Agora o jogo começa a ficar interessante.

    Não comemore ainda.

    É aqui que a maioria falha.""")
    time.sleep(4)
    os.system("cls")
    primeiroNumeroSorteado=random.randint(1,5)
    segundoNumeroSorteado=random.randint(1,5)
    terceiroNumeroSorteado=random.randint(1,5)
    quartoNumeroSorteado=random.randint(1,5)
    quintoNumeroSorteado=random.randint(1,5)
    print("RÁPIDO! DECORE ESSES NÚMEROS!!")
    print(f"{primeiroNumeroSorteado} - {segundoNumeroSorteado} - {terceiroNumeroSorteado} - {quartoNumeroSorteado} - {quintoNumeroSorteado}")
    time.sleep(2)
    os.system("cls")
    print(f"{primeiroNumeroSorteado} - {segundoNumeroSorteado} - {terceiroNumeroSorteado} - {quartoNumeroSorteado} - {quintoNumeroSorteado}") # TIRAR DEPOIS
    respostaPrimeiroNumero=int(input("Digite o primeiro número que apareceu: "))
    respostaSegundoNumero=int(input("Digite o segundo número que apareceu: "))
    respostaTerceiroNumero=int(input("Digite o terceiro número que apareceu: "))
    respostaQuartoNumero=int(input("Digite o quarto número que apareceu: "))
    respostaQuintoNumero=int(input("Digite o quinto número que apareceu: "))
    os.system("cls")
    if respostaPrimeiroNumero == primeiroNumeroSorteado and respostaSegundoNumero == segundoNumeroSorteado and respostaTerceiroNumero == terceiroNumeroSorteado and respostaQuartoNumero == quartoNumeroSorteado and respostaQuintoNumero == quintoNumeroSorteado:
        print("Decidindo seu destino...")
        time.sleep(4)
        print("""
    === JOGOS MORTAIS ===

    Correto...

    Boa.

    Você viu, guardou...
    e sobreviveu.

    Nem todos conseguem.

    Mas não se acostume.

    O próximo erro pode ser o último.
    """)
        time.sleep(4)
    else:
        print("Decidindo seu destino...")
        time.sleep(4)
        print("""
    === JOGOS MORTAIS ===

    Você falhou.

    Eles estavam ali...
    claros, simples.

    Mas sua mente te traiu.

    Alguns segundos de atenção
    eram tudo o que você precisava.

    Agora é tarde.

    Fim de jogo para você.""")
        perdeu_Game=True
        print("")
        jogarNovamente=input("Gostaria de jogar novamente? (s/n): ")
        if jogarNovamente=="s":
            os.system("cls")
            continue
        else:
            break
    os.system("cls")
    print("Processando... a etapa final está sendo preparada.")
    time.sleep(5)
    print("")
    print("""
    #  ___ _   ___ ___   ___ _                                         
    # | __/_\ / __| __| | __(_)                                        
    # | _/ _ \\__ \ _|  |__ \_                                         
    # |_/_/ \_\___/___| |___(_)                                        
    #   ___    ___ _  _ ___ ___ __  __   _     ___ ___ _  _   _   _    
    #  / _ \  | __| \| |_ _/ __|  \/  | /_\   | __|_ _| \| | /_\ | |   
    # | (_) | | _|| .` || | (_ | |\/| |/ _ \  | _| | || .` |/ _ \| |__ 
    #  \___/  |___|_|\_|___\___|_|  |_/_/ \_\ |_| |___|_|\_/_/ \_\____|""")
    print("")
    print("""
        === JOGOS MORTAIS — FASE FINAL ===

        Um programador encontra um nano computador
        que trabalha apenas com bits.

        O computador possui exatamente:
        41.943.040 bits de memória.

        Quantos Megabytes isso representa?

        Dica:
        1 byte = 8 bits
        1024 bytes = 1 KB
        1024 KB = 1 MB""")

    respostaFase5 = int(input("Sua resposta (em MB): "))
    os.system("cls")
    if respostaFase5==5:
        print("Analisando resposta final.....")
        time.sleep(5)
        print("""
    === JOGOS MORTAIS ===

    ...
        🎉 YOU WIN !! 🎉
    Resposta correta.

    5 MB.

    Incrível.

    Você sobreviveu a todas as fases.
    Cada desafio.
    Cada armadilha.

    Você venceu.

    Mas lembre-se...

    Nem todo jogo termina quando parece.

    Parabéns!!""")
        time.sleep(6)
        print("""
                    .                .     .          .                        .                .       .     .  
        .             .      .                                                    .   .               
                        .                    .  .         ..   .          .        .                    
                .    .               ..................    .    .  .           . .                
        .                          ......:-===========:...... .    .                        .       
        .   .          .         ....:-=------:::::::-------==-...                          .     .  .
                    .         ...----:::::::::::::::::=****+=====....                  .  .          
                ......      .....:=-=########%+:::::::::#%%######%+-==-....         .                   
    ........ ...:=-. .    ...:--::=%%%@%=-:::::::::::::::::-==%%-----==...         .                  
    ....-++.....-*@.. .  ...=-:::::::::::::::::::::::::::::-----------=+-..    .      .               
    .-:-=#%..:+*%@-.......---:::::::::------:::::::::::-----------------=+...              .          
    ..-:-==*-::=*@.....:=.---::::::------::::----::::--::::-=***++=-------=*..                  .  .  .
    ..---=+%-.-*%....-...-*-::::-*%@@@@@@@@@%*----::--=#@@@@@@@@@@@@@@@%#####-..              .        
    ..-::-=#:.=#.:*%@#**%@@@@@@@@@@%%%%%%%@@@@@@@%@@@@@@%%%%%%%%%%@@@@@@@@@@@@-           .           
    ..-::=*%+*@++%:.##::+%@@@@@@%%%%%%%%%%%%@@@@@@@@@%%%%%%%%%%%%%%@@@#---=+@#.                      
        .-::=*#@@%###..@::-#+:%@@@%%%%%%%%%%%%%%@@@%@@@%%%%%%%%%%%%%%%@@@-----=#@... .                  
    .   .-::=*#@@%#=...:.-=#=:=@@@%%%%%%%%%%%%%%@@@%%@@%%%%%%%%%%%%%%%@@#-:---=*@+.               .     
        :-:-=*%@+--.....-#%::::%@@@%%%%%%%%%%%%%@@@--@@@%%%%%%%%%%%%@@@@--:---=++..          .   .      
      .:=--+#@%--=-::-+##-:::::#@@@@%%%%%%%%%@@@@=::-@@@@%%%%%%%%@@@@%---:---=++..                      
      .:++*#@@*=*#%*-:-=--::::::-%@@@@@@@@@@@@@%-:::::+@@@@@@@@@@@@@=--------=+*..  .                 .
     .:-:.:=**+......:+=-::---:---*@@@@@@@@@#--:::::::--*%@@@@@#=----------=+**.. .......     .  .    
        ....:::..   ..:+=--------:::::::-:::::::::::::::::------==+##@#*=---=+*=...-:...-.             
                    ...*+=---=+-=%*++####*++===++++++**#######--+*=*-:------=*#:...+=...-..           .
                    ...=+=---:::::-+-*-::=-:::-:::--:::-=::-=+-=**=---------+#*. ..+=:::-.      .   . .
        .  .   .    ..*+=-----::::-=+++#+===*=-=+%+==+%**+=+.:-:--------==*#=.  .+-...-:             
                    ..-*+=--------::--.::...:...:-...:-..:-=:---===---===+#*.   .*+--:.:.            
    .              ....**+=----------::--:.:::..:-:..:-:::----=++=--====+*%:. . .+%=:..::.           
                        ..+*+==-----===----::---:--=----------=+*==-====++*%:.  .  =###-......::...    
                        ..+*+===-----=++=-----------------==*#+======+++*%...   .=*@+:..  ....--.    
                            .:*++====-----=*+==---------==+*#*=======+++*#+..   ..-**%#=-::::::-+=.    
                    .      ...=*+++===========+*********+========+++**#*...     ..:-**+=-----+*=+..    
                        .     ...+#*+++=============+++++++++++++++**##... .   . .::=#*+=:.......:-..   
    . .                        ...:****++++++++++++++++++++++****##=...         ..=##%#+-........-..   
    .            .        .   ......###*****++++++********##%#:..               .:%#+=*#**#*++=.     
                .                    ....:=+*#%#####%%%*+=:.....                 ..#=........::.      
    .                       . .     .      ................. .                .    ..=*-.......:-.      
                            .                                 .                   ..:-====+==..  .   
        ..      .                                       .              .   .            ......        
                .                  .                                                                .  
                            .   .           .                            .                          .    
                """)
        print("")
        jogarNovamente=input("Gostaria de jogar novamente? (s/n): ")
        if jogarNovamente=="s":
            os.system("cls")
            continue
        else:
            break
    else:
        print("Analisando resposta final.....")
        time.sleep(5)
        print(f"""
    === JOGOS MORTAIS ===

    Resposta incorreta.

    Você chegou até o fim...
    e falhou no último desafio.

    Veja o cálculo correto:

    41.943.040 bits ÷ 8 = 5.242.880 bytes
    5.242.880 ÷ 1024 = 5.120 KB
    5.120 ÷ 1024 = 5 MB

    Resposta correta: 5 MB

    E mesmo assim...
    você errou.

    Como consequência...

    SEU COMPUTADOR SERÁ FORMATADO.""")
        time.sleep(1)
        print("""
Começando processo de formatação em 3....""")
        time.sleep(1)
        print("")
        print("2....")
        time.sleep(1)
        print("")
        print("1....")
        time.sleep(1)
        print("")
        print("Sistema sendo apagado...")
        time.sleep(2)
        print("")
        perdeu_Game=True
        jogarNovamente=input("Gostaria de jogar novamente? (s/n): ")
        print("")
        if jogarNovamente=="s":
            os.system("cls")
            continue
        else:
            break