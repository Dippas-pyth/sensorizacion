def tipo_flor(longitud_petalo, ancho_petalo):
    if longitud_petalo < 2.5:
        return "0"
    else:
        if ancho_petalo < 1.7:
            return "2"
        else:
            return "1"
