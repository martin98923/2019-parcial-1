def decimal_to_hexadecimal(num):
    dicc = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    num_a = str(int(num)%16)
    num_b = str(int((int(num)/16)%(16)))
    num_c = str(int(int(num)/(16*16)))
    if int(num_a) > 9:
        num_a = dicc[int(num_a)]
    if int(num_b) > 9:
        num_b = dicc[int(num_b)]
    if int(num_c) > 9:
        num_c = dicc[int(num_c)]
    num_d = num_c+num_b+num_a
    return num_d

   
