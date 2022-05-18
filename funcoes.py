
def imprimir_titulo(titulo, local):

    titulo = [titulo.text for titulo in local] 

    titulo = ' '.join(map(str, titulo))
    
    return titulo

def data_br(data):
    ano,mes,dia = data.split('-')
    out_data = '{}/{}/{}'.format(dia,mes,ano)
    
    return out_data


