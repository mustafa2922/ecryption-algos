import random
chars = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789'

def encode(pt, key=None):
    pt_bin_encode = ''.join(map(lambda x: format(ord(x), '08b'), list(pt)))
    key = ''.join([format(ord(chars[random.randint(0, len(chars)-1)]), '08b')
                for _ in range(len(pt))]) if key == None else key
    ct_bin_encode = format(int(pt_bin_encode, 2) ^ int(
                key, 2), f'0{len(pt_bin_encode)}b')
    ct_encoded = ''.join([chr(int(ct_bin_encode[i:i+8], 2))
                for i in range(0, len(ct_bin_encode), 8)])

    return pt, pt_bin_encode, key, ct_bin_encode, ct_encoded

def decode(ct, key):
    ct_bin_decode = ''.join([format(ord(i), '08b') for i in ct])
    pt_bin_decode = format(int(ct_bin_decode, 2) ^ int(
                key, 2), f'0{len(ct_bin_decode)}b')
    pt_decoded = ''.join([chr(int(pt_bin_decode[i:i+8], 2))
                for i in range(0, len(pt_bin_decode), 8)])

    return ct, ct_bin_decode, key, pt_bin_decode, pt_decoded

pt, pt_bin_encode, key, ct_bin_encode, ct_encoded = encode('Mustafa Raza')
ct, ct_bin_decode, key, pt_bin_decode, pt_decoded = decode(ct_encoded, key)

print('Encoded Text :- ', ct_encoded)
print('Decoded Text :- ', pt_decoded)