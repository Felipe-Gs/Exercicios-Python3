# soma elemtos na lista
def vetor():
    x = []
    for c in range(20):
        x.append(float(input('diga um valor: ')))
    soma = sum(x)
    print(soma)
vetor()