cont = 0
idades = 0
op = ()
while True:
    idade = int(input('digite sua idade'))
    cont += 1
    idades += idade
    media = idades / cont
    op = input('digite se quer verificar a media: s/n')
    if op == 'n':
        continue
    else:
        print(media)
        if media >= 0 and media <= 25:
            print('que turma jovem!')
        elif media >= 26 and media <= 60:
            print('turma adulta!')
        elif media >= 61 and media <= 999:
            print('turma idosa!')
        break