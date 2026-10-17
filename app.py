from colorama import Fore, Style

Niveis = [1, 2, 3, 4, 5]

for nivel in Niveis:
    if nivel == 1:
        print(Fore.RED + "Nível 1 - Muito baixo (crítico)")
        print(Style.RESET_ALL)

    elif nivel == 2:
        print(Fore.YELLOW + "Nível 2 - Baixo")
        print(Style.RESET_ALL)

    elif nivel == 3:
        print(Fore.GREEN + "Nível 3 - Médio")
        print(Style.RESET_ALL)

    elif nivel == 4:
        print(Fore.CYAN + "Nível 4 - Alto")
        print(Style.RESET_ALL)

    elif nivel == 5:
        print(Fore.BLUE + "Nível 5 - Muito alto (alerta)")
        print(Style.RESET_ALL)