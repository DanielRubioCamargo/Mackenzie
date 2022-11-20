lista = [["lula",13, "pt", "presidente"],["bozo",22, "pl", "presidente"],["ciro",12, "bts", "presidente"]]

n = int(input())

nome = ''
numero = 0
partido = ''
cargo = ''

#foreach
for i in lista:
    if i[1] == n:
        nome = i[0]
        numero = i[1]
        partido = i[2]
        cargo = i[3]

print("Nome : {}\nNumero : {}\nPartido : {}\nCargo : {}".format(nome, numero, partido, cargo))