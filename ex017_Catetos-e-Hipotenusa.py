co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hi,))

import math
co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente'))
hi = math(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
