
import random
alph = 'abcdefghijklmnopqrstuvwxyz'
ASCII_A, ASCII_a, ASCII_Z, ASCII_z, ASCII_0, ASCII_9 = ord('A'), ord('a'), ord('Z'), ord('z'), ord('0'), ord('9')


def encode(pt, key=None):
    key = [alph[random.randint(0, 25)] for _ in range(len(pt))] if key == None else (
        key if len(key) == len(pt) else [key[i % len(key)] for i in range(len(pt))])

    return (''.join(map(lambda x, y: chr(((ord(x)-ASCII_A) + (ord(y)-ASCII_A)) % 26 + ASCII_A) if 'A' <= x <= 'Z'
                       else (chr(((ord(x)-ASCII_a) + (ord(y)-ASCII_a)) % 26 + ASCII_a) if 'a' <= x <= 'z'
                             else (chr(((ord(x)-ASCII_0) + (ord(y)-ASCII_0)) % 10 + ASCII_0) if '0' <= x <= '9'
                                   else x)), list(pt), key)),''.join(key))


def decode(ct, key):
    return ''.join(map(lambda x, y: chr(((ord(x)-ASCII_A) - (ord(y)-ASCII_A)) % 26 + ASCII_A) if 'A' <= x <= 'Z'
                       else (chr(((ord(x)-ASCII_a) - (ord(y)-ASCII_a)) % 26 + ASCII_a) if 'a' <= x <= 'z'
                             else (chr(((ord(x)-ASCII_0) - (ord(y)-ASCII_0)) % 10 + ASCII_0) if '0' <= x <= '9'
                                   else x)), list(ct), key))

# print(encode("This type of cipher is often referred to as the Beaufort cipher when it uses multiple layers of random alphabetical orders Its a variant of the polyalphabetic cipher family similar to the Vigenre cipher but with a different substitution method"))
# print(decode('Pexz jrml rj yikxel vj xiwvj qzrwqvwf zs om qgr Lmnjoovc sziflo uulq rw kiao rvbdkqca ddcspy zy otqafz abvdrtgsvmcy cbrfmu Icx s lcsrhhm yo hiu aknyrlyjkvlxkl goczpr dkwifd uenildw hb gon Lykilwl cuyrfe pyz spzp k llgorwbvg pcecdwcilngm yzgrec', 'qxphjqtxhaderwavqaulnrgjddrwczvmszescrgehouvxznbeinpjaejaqrtyhxkynhdnjdfqqwwdfbqkcbrwusdeoygtltqxtdxrniaqgwrscznkcnvokobvcrujfassqcbjhuthkjxobqilwcarajckuhecjhegnslaoykkaufscwbaadfionanhjfkqeeyfhhamjkbnroeghwhgiwksidbjnfxintxidkkojosfszfmvnkqz'))

print('=============== encode ===============')
pt = input('Enter Plain Text :- ')
ct = encode(pt)
print('Cipher Text :- ',ct[0])
print('Key :- ',ct[1])
key=ct[1]

print('=============== decode ===============')
abc = input('Enter Cipher Text :- ')
print('Plain Text :- ',decode(abc,key))