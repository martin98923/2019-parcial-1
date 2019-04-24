from decimal_to_hexa import decimal_to_hexadecimal

def interfaz (num):
    if not num:
        return 'Ingrese un numero'
    try:
        int(num)
        if 4095 < int(num):
            return 'Ingrese un numero menor a 4095'
        else:
            if int(num)<0:
                return 'Ingrese un  numero positivo'
            else:
                return decimal_to_hexadecimal(num)
    except:
        return 'Ingrese un numero'


