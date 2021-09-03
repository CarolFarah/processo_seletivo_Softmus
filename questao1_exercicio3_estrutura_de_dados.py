lista = {"Nova Zelândia": "Wellington", "Estados Unidos": 'Washington', 'Brasil': "Brasília", "Siria": "Damasco", "Libano": 'Beirute', "Japão": 'Tóquio', "Itália": 'Roma', "Inglaterra": 'Londres', "Irlanda": "Dublin", "Coréia do Sul": "Seul", "Austrália": 'Camberra', "África do Sul": ["Cidade do Cabo", 'Pretória', "Bloemfontein"], "Egito": "Cairo", "Angola": 'Luanda'}

def sortList(l):
    print(f"Lista ordenada pelos países: {sorted(lista.items(), key=lambda x: x[0])}")
    print(f"Lista ordenada pelas capitais: {sorted(lista.items(), key=lambda x: x[1][0])}")