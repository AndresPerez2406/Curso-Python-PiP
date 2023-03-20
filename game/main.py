import random

opciones = ('piedra', 'papel', 'tijera')

userwin = 0

pcwin = 0

ronda = 1

while True:

    print('*' * 10)
    print('Ronda =>', ronda)
    print('*' * 10)

    user = (input('Elija Piedra, Papel o Tijera =>'))
    user = user.lower()

    if not user in opciones:
        print('Esta opcion no es valida')
        continue

    pc = random.choice(opciones)

    # print(user, 'vs', pc)
    # print(userwin, '-', pcwin)

    ronda +=1

    if pc == user:
        ronda -=1
        print('Empate')
        print('Marcador se mantiene => Usuario', userwin,'- Pc', userwin)
    elif user == 'piedra' and pc == 'tijera':
        userwin += 1
        print('Usuario gana con',user, 'a' ,pc, ' Marcador =>', userwin,'-', pcwin)
    elif user == 'papel' and pc == 'piedra':
        userwin += 1
        print('Papel win')
    elif user == 'tijera' and pc == 'papel':
        userwin += 1
        print('Usuario gana con',user, 'a' ,pc, ' Marcador =>', userwin,'-', pcwin)
    else:
        pcwin += 1
        print('Pc gana con',pc, 'a' ,user, 'Marcador =>', pcwin,'-', userwin)

    if userwin == 3:
        print('Usuario gana por limite de puntos', userwin)
        print('Maracdor final: Usuario =>', userwin, '- Pc =>', pcwin)
        break
    elif pcwin == 3:
        print('Pc gana por limite de puntos', pcwin)
        print('Marcador final: Pc =>', pcwin, '- Usuario =>' , userwin)
        break





