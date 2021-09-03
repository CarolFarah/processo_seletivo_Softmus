def contandoVales(caminho):
    soma = 0
    vales = 0
    n = 0

    for p in range(len(caminho)):
        if caminho[p] in 'dD':
            n += -1
            soma = + n
            if soma == -1:
                vales = vales + 1

        elif caminho[p] in 'sS':
            n += 1
            soma = + n

    return vales