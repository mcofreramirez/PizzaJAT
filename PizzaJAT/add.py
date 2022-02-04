def agregar_ingrediente(ingredientes, eleccion):
    
    disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo','Jamon','Carne','Tocino','Queso']
    
    nuevo_ingrediente = disponibles[eleccion-1]
    
    if nuevo_ingrediente in ingredientes['ingredientes']:
        print('El ingrediente ya existe')
    
    else:
        ingredientes['ingredientes'].append(nuevo_ingrediente)
        print(f'Se ha agregado {nuevo_ingrediente}')

    return ingredientes

if __name__ == "__main__":
        ingredientesPrueba = {'masa': 'Masa Tradicional','salsa': 'Salsa de Tomate','ingredientes': ['Queso']}

        eleccion = int(input(''' Seleccione su ingrediente:
        1). Tomate
        2). Champiñones
        3). Aceituna
        4). Cebolla
        5). Pollo
        6). Jamón
        7). Carne
        8). Tocino
        9). Queso
        >'''))
            
        ingredientes = agregar_ingrediente(ingredientesPrueba, eleccion)

        print (ingredientesPrueba)