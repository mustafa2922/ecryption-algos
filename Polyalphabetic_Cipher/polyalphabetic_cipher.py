
import random

def encode(pt, M1=None, M2=None, M3=None):

    M1 = [chr(i) for i in random.sample(range(97,123),26)] if M1 == None else M1 
    M2 = [chr(j) for j in random.sample(range(97,123),26)] if M2 == None else M2 
    M3 = [chr(k) for k in random.sample(range(97,123),26)] if M3 == None else M3 

    if len(M1) == len(M2) == len(M3) == 26:
        return {
            'ct':''.join([(M1[ord(pt[i])-97] if i % 3 == 0 else (M2[ord(pt[i])-97] if i % 3 == 1 
                    else M3[ord(pt[i])-97])) for i in range(len(pt))]),
            'M1': ''.join(M1),'M2': ''.join(M2),'M3': ''.join(M3) }
    
    return 'All keys must contain all alphabets'


def decode(ct,M1,M2,M3):
    if len(M1) == len(M2) == len(M3) == 26:
        return ''.join([(chr(M1.index(ct[i])+97) if i % 3 == 0 else (chr(M2.index(ct[i])+97) if i % 3 == 1 
                  else chr(M3.index(ct[i])+97) )) for i in range(len(ct))])
    
    return 'All keys must contain all alphabets'

print('=============== encode ===============')
pt = input('Enter Plain Text :- ')
cipher_data = encode(pt)
ct, M1, M2, M3 = cipher_data['ct'], cipher_data['M1'], cipher_data['M2'], cipher_data['M3']
print('Cipher Text :- ',ct)
print(f"M1: {M1}")
print(f"M2: {M2}")
print(f"M3: {M3}")
print('=============== decode ===============')
abc = input('Enter Cipher Text :- ')
print('Plain Text :- ',decode(abc,M1,M2,M3))