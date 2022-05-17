
def imprimir_titulo(titulo, local):

    titulo = [titulo.text for titulo in local] 

    titulo = ' '.join(map(str, titulo))
    
    return titulo
