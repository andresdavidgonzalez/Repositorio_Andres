n = float(input('¿Cual es su nota? '))
if n>=0 and n <= 5: # 0<=n<=5
    if n >= 3:
        print('Aprobo')
    else:
        print('Reprobo')
else:
    print('La nota es invalida.')