
def encrypt(pt, depth=2):
    pt = pt.replace(' ','')
    pointer, times, upper, lower, sequence = 0, 0, 2 * (depth - 1), 0, True

    return ''.join(
        [pt[(
            pointer, 
            pointer:=pointer + (
                upper if (lower == 0) 
                else (lower if (upper == 0) else (upper if sequence else lower))
            ),
            sequence:= not sequence
            )[0]] 
        if (pointer < len(pt)) 
        else ((
            times:=times+1,
            pointer:=times, 
            sequence := True, 
            upper := upper-2, 
            lower := lower+2, 
            pt[(
                pointer,pointer:=pointer + (
                    upper if (lower == 0) 
                    else (lower if (upper == 0) else (upper if sequence else lower))
            ), 
            sequence:= not sequence)[0]]
            )[5])
        for _ in range(len(pt))]
    )

def decrypt(ct, depth):

    return ''.join([_ for _ in ct])


print(encrypt('ab cd ef gh ij kl mn op qr st uv wx yz',14))