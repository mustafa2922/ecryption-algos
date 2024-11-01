import random
import re
alphabets = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

def encrypt(pt, key=None, filler='X'):
    pointer = 0
    filler = filler.upper()
    pt = re.sub(r'\d', '', pt.upper().replace("J", "I").replace(" ", ""))
    diagraphs = list(filter(lambda x: (x != ['X'] and x != []), [
        (list(dict.fromkeys(pt[pointer:pointer+2])) +[filler], pointer := pointer + 1)[0]
        if (len(list(dict.fromkeys(pt[pointer:pointer+2]))) != 2 and pointer <= len(pt))
        else (list(dict.fromkeys(pt[pointer:pointer+2])), pointer := pointer + 2)[0] for i in range(len(pt))]))
    
    key = random.sample(alphabets, 25) if key is None else list(dict.fromkeys(list(key.upper()) + list(alphabets)))
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    positions = {char: [i // 5, i % 5] for i, char in enumerate(key)}

    pt_indexes = [[positions[i[0]], positions[i[1]]] for i in diagraphs]
    ct_indexes = [
        [[x[0][0], x[1][1]], [x[1][0], x[0][1]]]
        if (x[0][0] != x[1][0] and x[0][1] != x[1][1])
        else ([[x[0][0], (x[0][1] + 1) % 5], [x[1][0], (x[1][1] + 1) % 5]] if (x[0][0] == x[1][0])
        else [[(x[0][0] + 1) % 5, x[0][1]], [(x[1][0] + 1) % 5, x[1][1]]]) for x in pt_indexes ]

    ct = ''.join([f'{matrix[x[0][0]][x[0][1]]}{matrix[x[1][0]][x[1][1]]}' for x in ct_indexes])
    return ct

def decrypt(ct, key):
    diagraphs = [list(ct[i:i+2]) for i in range(0,len(ct),2)]
    key = list(dict.fromkeys(list(key.upper()) + list(alphabets)))
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    positions = {char: [i // 5, i % 5] for i, char in enumerate(key)}
    ct_indexes = [[positions[i[0]], positions[i[1]]] for i in diagraphs]
    pt_indexes = [
        [[x[0][0], x[1][1]], [x[1][0], x[0][1]]]
        if (x[0][0] != x[1][0] and x[0][1] != x[1][1])
        else ([[x[0][0], (x[0][1] - 1) % 5], [x[1][0], (x[1][1] - 1) % 5]] if (x[0][0] == x[1][0])
        else [[(x[0][0] - 1) % 5, x[0][1]], [(x[1][0] - 1) % 5, x[1][1]]]) for x in ct_indexes]

    pt = ''.join([f'{matrix[x[0][0]][x[0][1]]}{matrix[x[1][0]][x[1][1]]}' for x in pt_indexes]).replace('X','')
    return pt

print("Plain Text :- " , 'Attack')
print("Encryption Key :- " , 'monarchy')
print("======== Encryption ========")
print("Encrypted Text :- ",encrypt("attack", 'monarchy'))
print("======== Decryption ========")
print("Decrypted Text :- ",decrypt('RSSRDE','monarchy'))