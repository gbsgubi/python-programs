def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Breno Coltro da Costa                                       |')
    print('| Gustavo Barbosa Silva                                       |')
    print('| Pedro de Oliveira Gomes Carneiro                            |')
    print('|                                                             |')
    print('| Versão 3.0 de 20/abril/2022                                 |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    nroDaOpc=1
    for opc in mnu:
        print (nroDaOpc,') ',opc,sep='')
        nroDaOpc+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', [str(opc) for opc in range(1,len(mnu)+1)])

def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
   
    while inicio<=final:
        meio=(inicio+final)//2
       
        if nom==agd[meio][0]:
            return [True,meio]
        elif nom<agd[meio][0]:
            final=meio-1
        else: # nom>agd[meio][0]
            inicio=meio+1
           
    return [False,inicio]

def incluir (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
           
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')
   
    contato=[nome,aniversario,endereco,telefone,celular,email]
   
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar (agd):
    if agd==[]:
        print ('A agenda não possui pessoas cadastradas!')
    else:
        digitouDireito=False
        while not digitouDireito:
            nome=input('Nome.......: ')
       
            resposta=ondeEsta(nome,agd)
            achou   = resposta[0]
            posicao = resposta[1]
       
            if not achou:
                print ('\nPessoa inexistente - Favor redigitar...\n')
            else:
                digitouDireito=True
   
        print('Aniversario:',agd[posicao][1])
        print('Endereco...:',agd[posicao][2])
        print('Telefone...:',agd[posicao][3])
        print('Celular....:',agd[posicao][4])
        print('e-mail.....:',agd[posicao][5])

def atualizar (agd):
    if agd==[]:
        print ('A agenda não possui pessoas cadastradas!')
    else:
        digitouDireito=False
        while not digitouDireito:
            nome=input('Nome.......: ')
       
            resposta=ondeEsta(nome,agd)
            achou   = resposta[0]
            posicao = resposta[1]
       
            if not achou:
                print ('\nPessoa inexistente - Favor redigitar...\n')
            else:
                digitouDireito=True
   
        print('Aniversario:',agd[posicao][1])
        print('Endereco...:',agd[posicao][2])
        print('Telefone...:',agd[posicao][3])
        print('Celular....:',agd[posicao][4])
        print('e-mail.....:',agd[posicao][5])
           
        menu=['Atualizar Aniversario',\
              'Atualizar Endereço',\
              'Atualizar Telefone',\
              'Atualizar Celular',\
              'Atualizar e-mail',\
              'Encerrar a atualizacao'];

        op=None
        contato = agd[posicao]
        while op!=6:
            op = int(opcaoEscolhida(menu))
            
            if op==1:
                agd[posicao][1]=input('Aniversário: ')
            elif op==2:
                agd[posicao][2]=input('Endereço...: ')
            elif op==3:
                agd[posicao][3]=input('Telefone...: ')
            elif op==4:
                agd[posicao][4]=input('Celular....: ')
            elif op==5:
                agd[posicao][5]=input('e-mail.....: ')
      
        print('Recadastramento realizado com suceso!')

def listar (agd):
    if agd==[]:
        print ('A agenda não possui pessoas cadastradas!')
    else:
        for contato in agd:
            print('\nNome.......:',contato[0])
            print('Aniversário:',contato[1])
            print('Endereço...:',contato[2])
            print('Telefone...:',contato[3])
            print('Celular....:',contato[4])
            print('e-mail.....:',contato[5])

def excluir (agd):
    if agd==[]:
        print ('A agenda não possui pessoas cadastradas!')
    
    else:
        print()
       
        digitouDireito=False
        while not digitouDireito:
            nome=input('Nome.......: ')
           
            resposta=ondeEsta(nome,agd)
            achou   = resposta[0]
            posicao = resposta[1]
           
            if not achou:
                print ('\nPessoa inexistente - Favor redigitar...\n')
            else:
                digitouDireito=True
       
        print('Aniversario:',agd[posicao][1])
        print('Endereco...:',agd[posicao][2])
        print('Telefone...:',agd[posicao][3])
        print('Celular....:',agd[posicao][4])
        print('e-mail.....:',agd[posicao][5])
    
        resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
       
        if resposta in ['s','S']:
            del agd[posicao]
            print('Remoção realizada com sucesso!')
        else:
            print('Remoção não realizada!')

# daqui para cima, definimos subprogramas
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa'];

opcao=None
while opcao!=6:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
       
print('OBRIGADO POR USAR ESTE PROGRAMA!')