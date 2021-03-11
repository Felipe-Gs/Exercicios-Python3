#idade em dias
def pessoa(anos, meses, dias):
    an = anos*365
    ms = meses*30
    soma = an + ms + dias
    print(f'voce tem {soma} dias')
anos = int(input('diga o total de anos: '))
meses = int(input('diga o total de meses'))
dias = int(input('diga o tota de dias'))

pessoa(anos, meses, dias)