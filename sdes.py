P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8=[6, 3, 7, 4, 8, 5, 10, 9]

IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

SBOX1 = [[1, 0, 3, 2],
         [3, 2, 1, 0],
         [0, 2, 1, 3],
         [3, 1, 3, 2]]

SBOX2 = [[0, 1, 2, 3],
         [2, 0, 1, 3],
         [3, 0, 1, 0],
         [2, 1, 0, 3]]
def permute(bits, table):
    return [bits[i - 1] for i in table]
def left_shift(bits, n):
    return bits[n:] + bits[:n]
def generate_keys(key):
    key = permute(key, P10)
    left, right = key[:5], key[5:]

    left, right = left_shift(left, 1), left_shift(right, 1)
    K1 = permute(left + right, P8)

    left, right = left_shift(left, 2), left_shift(right, 2)
    K2 = permute(left + right, P8)

    return K1, K2
def sbox_substitution(bits, sbox):
    row = int(f"{bits[0]}{bits[3]}", 2)
    col = int(f"{bits[1]}{bits[2]}", 2)
    return [int(b) for b in format(sbox[row][col], '02b')]
def feistel(right, subkey):
    expanded = permute(right, EP)
    xored = [expanded[i] ^ subkey[i] for i in range(8)]

    left, right = xored[:4], xored[4:]
    left = sbox_substitution(left, SBOX1)
    right = sbox_substitution(right, SBOX2)

    return permute(left + right, P4)
def sdes(input_bits, key, encrypt=True):
    K1, K2 = generate_keys(key)
    if not encrypt:
        K1, K2 = K2, K1

    bits = permute(input_bits, IP)
    left, right = bits[:4], bits[4:]

    left = [left[i] ^ f for i, f in enumerate(feistel(right, K1))]
    left, right = right, left  # Swap

    left = [left[i] ^ f for i, f in enumerate(feistel(right, K2))]

    return permute(left + right, IP_INV)
def bin_str_to_list(bin_str):
    return [int(b) for b in bin_str]
key = bin_str_to_list("1010000010")  # 10-bit key
plaintext = bin_str_to_list("11010101")  # 8-bit plaintext

ciphertext = sdes(plaintext, key, encrypt=True)
decrypted = sdes(ciphertext, key, encrypt=False)

print("Plaintext: ", "".join(map(str, plaintext)))
print("Ciphertext: ", "".join(map(str, ciphertext)))
print("Decrypted: ", "".join(map(str, decrypted)))
