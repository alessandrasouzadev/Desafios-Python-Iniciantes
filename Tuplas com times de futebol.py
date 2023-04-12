times =('São Paulo', 'America-MG','Athletico-PR','Fortaleza','Atlético-MG',
        'Bahia','Goiás','Botafogo','Palmeiras', 'Corinthians','Vasco da Gama',
        'Coritiba','Cruzeiro','Cuiabá','Flamengo','Fluminense','Grêmio',
        'Internacional','Bragantino','Santos')

print('-='*20)
print(f'Lista de times do Brasileirão: {times}')

print('-='*20)
print(f'Os 5 primeiros são {times[0:5]}')

print('-='*20)
print(f'Os 4 últimos são {times[-4:]}')

print('-='*20)
print(f'Times em ordem alfabética {sorted(times)}')

print('-='*20)
print(f'O Bragantino está na {times.index("Bragantino")+1}° posição')
