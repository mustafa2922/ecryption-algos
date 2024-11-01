
ASCII_A, ASCII_a, ASCII_Z, ASCII_z, ASCII_0, ASCII_9 = ord('A'), ord('a'), ord('Z'), ord('z'), ord('0'), ord('9')

def encrypt(pt, key=3):
    return ''.join(map(lambda x: chr((ord(x)-ASCII_A+key) % 26 + ASCII_A) if 'A' <= x <= 'Z'
                       else (chr((ord(x)-ASCII_a+key) % 26 + ASCII_a) if 'a' <= x <= 'z'
                             else (chr((ord(x)-ASCII_0+key) % 10 + ASCII_0) if '0' <= x <= '9'
                                   else x)), list(pt)))

def decrypt(ct, key=3):
    return ''.join(map(lambda x: chr((ord(x)-ASCII_A-key) % 26 + ASCII_A) if 'A' <= x <= 'Z'
                       else (chr((ord(x)-ASCII_a-key) % 26 + ASCII_a) if 'a' <= x <= 'z'
                       else (chr((ord(x)-ASCII_0-key) % 10 + ASCII_0) if '0' <= x <= '9'
                        else x)), list(ct)))

# starter code 
mode = input('Select the mode (e/d) :- ')

while mode == 'e' or mode == 'd':
    if mode == 'e':
        pt = input('Enter the plain text :- ')
        key = int(input('Enter the key :- '))
        ct = encrypt(pt, key)
        print('Cipher text :- ', ct)
        mode = input('Select the mode (e/d) :- ')
    elif mode == 'd':
        ct = input('Enter the cipher text :- ')
        key = int(input('Enter the key :- '))
        pt = decrypt(ct, key)
        print('Plain text :- ', pt)
        mode = input('Select the mode (e/d) :- ')