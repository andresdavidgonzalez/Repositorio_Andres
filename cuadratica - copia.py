import math as m # libreria math ahora se llama m

a=int(input('ingrese el valor de a: '))
b=int(input('ingrese el valor de b: '))
c=int(input('ingrese el valor de c: '))
raiz=b**2-4*a*c
if raiz > 0:
    x1=(-b+m.sqrt(raiz))/(2*a)
    x2=(-b-m.sqrt(raiz))/(2*a)
    print('x1 =',x1)
    print('x2 =',x2)
else:
    raiz=m.fabs(raiz)
    x_r=-b/(2*a)
    x_i=m.sqrt(raiz)/(2*a)
    print('Las respuestas son:\n'\
          'x1 =',x_r,'+',x_i,'i\n'\
            'x2 =',x_r,'-',x_i,'i')
# help(math.escribir la funcion especifica)
# \ n : Se utiliza para dar un salto de linea.

# hacer programas, colocarlos en un archivo comprimido y en viarlo al aula virtual

#A.lower() convierte a minuscula
#A.upper() convierte a mayus