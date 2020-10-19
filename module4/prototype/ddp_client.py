from ddp_library import Circulo, Rectangulo
from copy import copy

circulo_original = Circulo(5)
rectangulo_original = Rectangulo(4, 3)
print(f'-I- El área del circulo es {circulo_original.area():.2f}')
print(f'-I- El área del rectángulo es {circulo_original.area():.2f}')
print('-' * 80)

### CIRCULO

# Clonamos los objetos. Aquí comienzan los problemas
# Al modificar el radio en el objeto original, afectamos a la copia
print('Asignación simple')
circulo_copia = circulo_original
circulo_copia.radio = 7
print(f'-I- El área del circulo original: {circulo_original.area():.2f} {circulo_original}')
print(f'-I- El área del circulo copia:    {circulo_copia.area():.2f} {circulo_copia}')
print(f'-I- id original:                  {circulo_original.id}')
print(f'-I- id copia:                     {circulo_copia.id}')
print('-' * 80)

# Entonces usamos el método clonar
print('Usando el método clonar')
circulo_copia = circulo_original.clonar()
circulo_copia.radio = 6
print(f'-I- El área del circulo original: {circulo_original.area():.2f} {circulo_original}')
print(f'-I- El área del circulo copia:    {circulo_copia.area():.2f} {circulo_copia}')
print('-' * 80)

# Usamos el método copia de manera directa evitando el clone
print('Método copy directo')
circulo_copia = copy(circulo_original)
circulo_copia.radio = 8
print(f'-I- El área del circulo original: {circulo_original.area():.2f} {circulo_original}')
print(f'-I- El área del circulo copia:    {circulo_copia.area():.2f} {circulo_copia}')
print('-' * 80)

### RECTANGULO

# Usamos el método copia de manera directa en el rectángulo
print('Método copy directo')
rectangulo_copia = copy(rectangulo_original)
print(f'-I- El área del circulo original: {rectangulo_original.area():.2f} {rectangulo_original}')
print(f'-I- El área del circulo copia:    {rectangulo_copia.area():.2f} {rectangulo_copia}')
print('-' * 80)

# Usamos el método clonar en el rectángulo
print('Usando el método clonar')
rectangulo_original.color = 'rosa'
rectangulo_copia = rectangulo_original.clonar()
# Incluso la copia puede seguir accediendo a los atributos de la superclase
rectangulo_copia.pos_x = 12
print(f'-I- El área del circulo original: {rectangulo_original.area():.2f} {rectangulo_original}')
print(f'-I- El área del circulo copia:    {rectangulo_copia.area():.2f} {rectangulo_copia}')
print(f'-I- pos_x:                        {rectangulo_copia.pos_x}')
# Incluso accedemos al ID que es un atributo oculto
print(f'-I- id original:                  {rectangulo_original.id}')
print(f'-I- id copia:                     {rectangulo_copia.id}')
print(f'-I- color original:               {rectangulo_original.color}')
print(f'-I- color copia:                  {rectangulo_copia.color}')
print('-' * 80)

# Usamos el método deepcopy en el rectángulo
print('Usando el método deepcopy')
rectangulo_original.color = 'rosa'
rectangulo_copia = rectangulo_original.deepcopy()
# Incluso la copia puede seguir accediendo a los atributos de la superclase
rectangulo_copia.pos_x = 12
print(f'-I- El área del circulo original: {rectangulo_original.area():.2f} {rectangulo_original}')
print(f'-I- El área del circulo copia:    {rectangulo_copia.area():.2f} {rectangulo_copia}')
print(f'-I- pos_x:                        {rectangulo_copia.pos_x}')
# Incluso accedemos al ID que es un atributo oculto
print(f'-I- id original:                  {rectangulo_original.id}')
print(f'-I- id copia:                     {rectangulo_copia.id}')
print(f'-I- color original:               {rectangulo_original.color}')
print(f'-I- color copia:                  {rectangulo_copia.color}')
print('-' * 80)