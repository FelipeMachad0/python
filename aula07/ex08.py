largura = float(input('insira a largura da parede: '))
altura = float(input('insira a altura da parede: '))
m2 = largura * altura
tinta = m2/2
print('sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, m2))
print('para pintar sua parede você precisa de {}l de tinta'.format(tinta))