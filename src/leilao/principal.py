from dominio import Usuario, Leilao, Lance, Avaliador

leo = Usuario("Leo")
vini = Usuario("Vini")
joice = Usuario("Joice")

lance_leo = Lance(leo, 300.0)
lance_vini = Lance(vini, 1300.0)
lance_joice = Lance(joice, 30.0)

leilao = Leilao("Iphone XS")

leilao.lances.append(lance_leo)
leilao.lances.append(lance_vini)
leilao.lances.append(lance_joice)

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'Maior lance: {avaliador.maior_lance}')
print(f'Menor lance: {avaliador.menor_lance}')
