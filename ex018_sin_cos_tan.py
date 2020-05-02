
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ãngulo que você deseja:'))
sen = sin(radians(ângulo))
cos = cos(radians(ângulo))
tan = tan(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tan))