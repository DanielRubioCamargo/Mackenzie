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

def cadastrarCandidato(l):

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

        print()
        op = input("Deseja continuar? [sim/nao] : ").lower()
        print()

        if op == "sim":
            continue
        break

def cadastrarEleitor(l):

    while True:

        nome = input("Insira seu nome : ").title()
        cpf = input("Insira seu CPF : ")

        lAux = list()
        lAux.append(nome)
        lAux.append(cpf)
        for i in range(3):
            lAux.append(False)
        l.append(lAux)

        print()
        op = input("Deseja continuar? [sim/nao] : ").lower()
        print()

        if op == "sim":
            continue
        break

def votar(l, e, b, n, tv):

    for el in range(len(e)):
        print("-"*55)
        print()
        if len(l) != 0:
            listaCargos = ["PREFEITO","GOVERNADOR","PRESIDENTE"]
            for i in range(3):
                podeContinuar = False
                for j in range(len(l)):
                    if l[j][3] == listaCargos[i] and e[el][i+2] == False:
                        podeContinuar = True
                        break
                if podeContinuar:
                    print("Vez de votar : {} | CPF : {}\n".format(e[el][0],e[el][1]))
                    print("Vote para ", listaCargos[i], " !\n")
                    podeBreak = False
                    while True:
                        if podeBreak:
                            break
                        op = int(input("Digite o número de seu candidato : "))
                        print()
                        if op == -1:
                            b[i] += 1
                            tv[i] += 1
                            e[el][i+2] = True
                            print("Voto em branco!\n")
                            break
                        elif op == -2:
                            n[i] += 1
                            tv[i] += 1
                            e[el][i+2] = True
                            print("Voto nulo!\n")
                            break
                        else:
                            count = 0
                            for k in range(len(l)):
                                if l[k][1] == op and l[k][3] == listaCargos[i]:
                                    op2 = input("\033[0;33mCandidato : {} - {} | Confirma? [sim/nao] : \033[m".format(l[k][0],l[k][2])).lower()
                                    print()
                                    if op2 == "sim":
                                        l[k][4] += 1
                                        tv[i] += 1
                                        e[el][i+2] = True
                                        print("\033[0;32mSucesso | Seu voto para {} foi confirmado!\033[m\n".format(listaCargos[i]))
                                        podeBreak = True
                                        break
                                    else:
                                        print("\033[0;31mVoto não confirmado! Tente novamente : \033[m\n")
                                        continue
                                count += 1
                                if count == len(l):
                                    print("\033[0;31mNúmero de candidato inválido!\033[m\n")
        else:
            print("\033[0;33m\nNão há candidatos para serem votados!\033[m\n")
        print("-"*55)
        print()

def separarCargos(l, pref, gov, pres):
    
    for i in l:
        if i[3] == "PREFEITO":
            pref.append(i)
        elif i[3] == "GOVERNADOR":
            gov.append(i)
        else:
            pres.append(i)

def ordenarLista(lista):

    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][4] < lista[j][4]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def criarMenuParaApuracao(cargo, lista, vb, vn, pos, tv):
    
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
        print("Votos Brancos : {} ({:.1f}%)\n".format(vb[pos], porcentagemBrancos))

        porcentagemNulos = (vn[pos]*100)/tv[pos]
        print("Votos Nulos : {} ({:.1f}%)\n".format(vn[pos], porcentagemNulos))

        print("="*(v+1)+"="*len(cargo)+"="*(v+1))
        print()

def apurarResultados(pref, gov, pres, vb, vn, tv):

    ordenarLista(pref)
    ordenarLista(gov)
    ordenarLista(pres)

    criarMenuParaApuracao("PREFEITO",pref, vb, vn, 0, tv)
    criarMenuParaApuracao("GOVERNADOR",gov, vb, vn, 1, tv)
    criarMenuParaApuracao("PRESIDENTE",pres, vb, vn, 2, tv)


def mostrarReE():
    pass

candidatos = list()
eleitores = list()
votosBrancos = [0,0,0]
votosNulos = [0,0,0]

prefeitos = list()
governadores = list()
presidentes = list()

totalVotos = [0,0,0]

while True:

    mostrarMenu()
    digito = int(input("Insira uma opção : "))
    print()

    if digito == 1:

        cadastrarCandidato(candidatos)

    elif digito == 2:

        cadastrarEleitor(eleitores)

    elif digito == 3:

        votar(candidatos, eleitores, votosBrancos, votosNulos, totalVotos)

    elif digito == 4:
        
        separarCargos(candidatos, prefeitos, governadores, presidentes)
        apurarResultados(prefeitos, governadores, presidentes, votosBrancos, votosNulos, totalVotos)

    elif digito == 5:
        pass

    elif digito == 6:
        print("Programa finalizado!\n")
        break
    else:
        print("\033[0;31mOpção inválida!\033[m\n")