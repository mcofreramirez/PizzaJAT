
def tipo_salsa(ingredientes, eleccion):
    if eleccion == 'T':
        ingredientes['salsa'] = 'Salsa de Tomate'
    
    elif eleccion == 'A':
        ingredientes['salsa'] = 'Salsa Alfredo'
    
    elif eleccion == 'B':
        ingredientes['salsa'] = 'Salsa Barbecue'
    
    elif eleccion == 'P':
        ingredientes['salsa'] = 'Salsa Pesto'
    
    if eleccion in ['T','A','B','P']:
        print(f'Su salsa se cambió a {ingredientes["salsa"]}')
    
    else:
        print('No se ha cambiado su tipo de Salsa')
    return ingredientes


if __name__ == "__main__":
        ingredientesPrueba = {'masa': 'Masa Tradicional','salsa': 'Salsa de Tomate','ingredientes': ['Queso']}

        eleccion = input ("""Escoja el tipo de Salsa:
        T). Salsa de tomate
        D). Salsa alfredo
        B). Salsa Barbecue
        P). Salsa pesto
            
        >""").upper()
        ingredientes = tipo_salsa(ingredientesPrueba, eleccion)
        
        print(ingredientes)