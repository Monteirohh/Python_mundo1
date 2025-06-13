medida = float(input('Uma distância em metro: '))
cm = medida * 100
mm = medida * 1000
print('A média de {}m corresponde a {:.0f}cm e {:.0f}'.format(medida, cm, mm))