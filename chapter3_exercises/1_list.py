ranking = ['Real Madrid', 'Barcelona', 'Corinthians', 'Bayern Munchen', 'Al Ahly']

topThree = ranking[:3]

print('A) mostrando os 3 primeiros colocados: ', topThree)

lastTwo = ranking[3:]

print('B) mostrando o 4º e 5º colocados: ', lastTwo)

alphabeticalOrder = ranking
alphabeticalOrder.sort()

print('C) mostrando em ordem alfabética: ', alphabeticalOrder)

barcelonaPosition = ranking.index('Barcelona')


print('D) posição do barcelona no ranking: ', barcelonaPosition + 1)
print('   posição do barcelona na LISTA:   ', barcelonaPosition)