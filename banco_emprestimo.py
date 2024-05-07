print(f"programa de emprestimo"
      f"responda: (0-nao ou 1-sim)")
nome_negativando=int(input('possui nome negativado?: '))
if nome_negativado == 1:
    print('nao pode realizar emprestimo')
else:
    carteira_asssinada=int(input('possui carteira assinada?: '))
    if carteria_assinada == 0:
        print('nao pode realizar emprestimo')
    else:
        casa_propria=int(input('possui casa propria?:'))
        if casa_propria == 0:
            print('nao pode realizar emprestimo')
        else:
           print('concedor emprestimo')