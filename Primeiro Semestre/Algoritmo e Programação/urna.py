def mostrarMenu():

    print('''    ============ MENU ============
    1 - Cadastrar candidato
    2 - Cadastrar eleitor
    3 - Votar
    4 - Apurar resultados
    5 - Relatório e Estatísticas
    6 - Encerrar
    ==============================
    ''')

# cadastra um candidato e insere uma lista com seus dados (nome, numero, partido, cargo e quantidade de votos) em uma lista global l
def cadastrarCandidato(l, lpartidos): 

    while True:

        nome = input("Insira o nome do candidato : ").upper()
        numero = int(input("Insira o número do candidato : "))
        partido = input("Insira o partido do candidato : ").upper()
        cargo = input("Insira o cargo do candidato : ").upper()

        lAux = list()
        lAux.append(nome)
        lAux.append(numero)
        lAux.append(partido)
        lAux.append(cargo)
        lAux.append(0)
        l.append(lAux)

        for i, p in enumerate(lpartidos): # cria uma nova posição na lista de partidos (se não existir)
            if p[0] == partido:
                break
            if i == len(lpartidos)-1:
                auxPartidos = list()
                auxPartidos.append(partido)
                auxPartidos.append(0)
                lpartidos.append(auxPartidos)

        print()
        op = input("Deseja continuar? [sim/nao] : ").lower()
        print()

        if op == "sim":
            continue
        break

'''cadastra um eleitor e insere uma lista com seus dados 
(nome, cpf, mais 3 valores booleanos para caso tenha votado já para determinado cargo) em uma lista global l'''
def cadastrarEleitor(l):

    while True:

        nome = input("Insira seu nome : ").title()
        cpf = input("Insira seu CPF : ")

        podeDarContinue = False

        for i in range(len(l)): # checa se o cpf já existe
            if l[i][1] == cpf:
                print()
                print("\033[0;31mNúmero de CPF existente!\033[m")
                print()
                podeDarContinue = True
                break
            if i == len(l)-1:
                lAux = list()
                lAux.append(nome)
                lAux.append(cpf)
                for i in range(3):
                    lAux.append(False)
                l.append(lAux)

        if podeDarContinue:
            continue

        print()
        op = input("Deseja continuar? [sim/nao] : ").lower()
        print()

        if op == "sim":
            continue
        break

''' função para votação, parametros : lista dos candidadtos(l), lista dos eleitores(e), lista de votos brancos(b),
lista de votos nulos(n), total de votos(tv), lista de partidos(lp)
'''
def votar(l, e, b, n, tv, lp):

    for el in range(1,len(e)): # percorre a lista de eleitores
        print()
        if len(l) != 0: # verifica se há candidatos para serem votados
            listaCargos = ["PREFEITO","GOVERNADOR","PRESIDENTE"]
            for i in range(3): # percorrerá 3 vezes (1ºvez para prefeito se tiver), (2ºvez para governador se tiver), (3ºvez para presidente se tiver)
                podeContinuar = False # variavel para permitir que o programa avançe
                for j in range(len(l)): # para cada candidato
                    if l[j][3] == listaCargos[i] and e[el][i+2] == False: # verifica se o cargo do candidato foi digitado corretamente de acordo com a listaCargos e se o eleitor não votou ainda
                        podeContinuar = True # o programa pode continuar
                        break
                if podeContinuar:
                    print("-"*55)
                    print("Vez de votar : {} | CPF : {}\n".format(e[el][0],e[el][1]))
                    print("Vote para ", listaCargos[i], " !\n")
                    podeBreak = False # variavel criada para se tornar True e sair do while quando a votação do eleitor finalizar corretamente
                    while True:
                        if podeBreak:
                            break
                        op = int(input("Digite o número de seu candidato : "))
                        print()
                        if op == -1: # voto branco
                            b[i] += 1 # incrementa uma unidade na lista de votos brancos para certo cargo
                            tv[i] += 1 # incrementa o total de votos para certo cargo
                            e[el][i+2] = True # eleitor votou
                            print("Voto em branco!\n")
                            break
                        elif op == -2: # voto nulo
                            n[i] += 1 # incrementa uma unidade na lista de votos nulos para certo cargo
                            tv[i] += 1 # incrementa o total de votos para certo cargo
                            e[el][i+2] = True # eleitor votou
                            print("Voto nulo!\n")
                            break
                        else: # o eleitor digitou algum numero sem ser -1 ou -2
                            count = 0 # contador dos candidatos para no final verificar se é o ultimo candidato a ser verificado no for loop
                            for k in range(len(l)):
                                if l[k][1] == op: # se o numero do candidato corresponder a opção digitada
                                    op2 = input("\033[0;33mCandidato : {} - {} | Confirma? [sim/nao] : \033[m".format(l[k][0],l[k][2])).lower()
                                    print() # op2 mostra o candidato segundo a posição do for e quer confirmar a escolha
                                    if op2 == "sim":
                                        for a in range(len(lp)):
                                            if lp[a][0] == l[k][2]:
                                                lp[a][1] += 1
                                        l[k][4] += 1 # mais um voto para este candidato
                                        tv[i] += 1 # total de votos incrementado
                                        e[el][i+2] = True # eleitor votou
                                        print("\033[0;32mSucesso | Seu voto para {} foi confirmado!\033[m\n".format(listaCargos[i]))
                                        podeBreak = True # pode dar o break do while
                                        break
                                    else:
                                        print("\033[0;31mVoto não confirmado! Tente novamente : \033[m\n")
                                        break # volta para a escolha de um candidato (mesmo eleitor)
                                count += 1
                                if count == len(l): # percorreu toda a lista e não achou o numero digitado
                                    print("\033[0;31mNúmero de candidato inválido!\033[m\n")
        else:
            print("\033[0;33m\nNão há candidatos para serem votados!\033[m\n")
        print("-"*55)
        print()

def separarCargos(l, pref, gov, pres): # adiciona cada candidato em sua respectiva lista
    
    for i in l:
        if i[3] == "PREFEITO":
            pref.append(i)
        elif i[3] == "GOVERNADOR":
            gov.append(i)
        else:
            pres.append(i)

def ordenarListaVotosCandidatos(lista): # ordenar por quantidade de votos

    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][4] < lista[j][4]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def criarMenuParaApuracao(cargo, lista, vb, vn, pos, tv): # cria a interface das apurações
    
    if len(lista) != 0:
        v = 15
        print("="*v+" "+cargo+" "+"="*v)
        print(("Vencedor : {}".format(lista[0][0])).center(2*v+len(cargo)))
        print("="*(v+1)+"="*len(cargo)+"="*(v+1))

        for i, c in enumerate(lista):
            print("{}º : {} ( {} ) | {} VOTO(S) |".format(i+1, c[0], c[2], c[4]))
        print("="*(v+1)+"="*len(cargo)+"="*(v+1))
        
        print()
        print("Total de votos : {}\n".format(tv[pos]))

        porcentagemBrancos = (vb[pos]*100)/tv[pos]
        print("Votos Brancos : {} ({:.1f} %)\n".format(vb[pos], porcentagemBrancos))

        porcentagemNulos = (vn[pos]*100)/tv[pos]
        print("Votos Nulos : {} ({:.1f} %)\n".format(vn[pos], porcentagemNulos))

        print("="*(v+1)+"="*len(cargo)+"="*(v+1))
        print()

def apurarResultados(pref, gov, pres, vb, vn, tv):

    ordenarListaVotosCandidatos(pref)
    ordenarListaVotosCandidatos(gov)
    ordenarListaVotosCandidatos(pres)

    criarMenuParaApuracao("PREFEITO",pref, vb, vn, 0, tv)
    criarMenuParaApuracao("GOVERNADOR",gov, vb, vn, 1, tv)
    criarMenuParaApuracao("PRESIDENTE",pres, vb, vn, 2, tv)

def retornarPartidoMaisVotadoEMenosVotado(lp):
    maior = 0
    maiorPartido = ''
    menor = 0
    menorPartido = ''
    for i in range(1,len(lp)):
        if i == 1:
            menor = lp[i][1]
            menorPartido = lp[i][0]
        if lp[i][1] > maior:
            maior = lp[i][1]
            maiorPartido = lp[i][0]
        elif lp[i][1] < menor:
            menor = lp[i][1]
            menorPartido = lp[i][0]
    return maiorPartido, menorPartido # retorna o partido com mais votos e o com menos

def mostrarEleitores(el): # lista de todos os eleitores
    print("Lista de eleitores : ")
    for i in range(1,len(el)):
        print("-> ",el[i][0])
    print()

def mostrarReE(lp, el): # relatório e estatisticas
    mostrarEleitores(el)
    maiorPartido, menorPartido = retornarPartidoMaisVotadoEMenosVotado(lp)
    print("Partido mais votado : {}".format(maiorPartido))
    print("Partido menos votado : {}".format(menorPartido))
    print()

candidatos = list()
eleitores = [['','',False,False,False]]
votosBrancos = [0,0,0]
votosNulos = [0,0,0]

prefeitos = list()
governadores = list()
presidentes = list()

partidos = [['',0]]

totalVotos = [0,0,0]

print("\nIniciando urna eletrônica...\n")

while True:

    mostrarMenu()
    digito = int(input("Insira uma opção : "))
    print()

    if digito == 1:

        cadastrarCandidato(candidatos, partidos)

    elif digito == 2:

        cadastrarEleitor(eleitores)

    elif digito == 3:

        votar(candidatos, eleitores, votosBrancos, votosNulos, totalVotos, partidos)

    elif digito == 4:
        
        separarCargos(candidatos, prefeitos, governadores, presidentes)
        apurarResultados(prefeitos, governadores, presidentes, votosBrancos, votosNulos, totalVotos)

    elif digito == 5:
        mostrarReE(partidos, eleitores)

    elif digito == 6:
        print("Programa finalizado!\n")
        break
    else:
        print("\033[0;31mOpção inválida!\033[m\n")