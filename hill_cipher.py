import numpy as np

key_matrix = np.zeros((4,4), dtype=int)
message_vector = np.zeros((4,1), dtype=int)
cipher_matrix = np.zeros((4,1), dtype=int)

def get_key_matrix(key):
    k = 0
    for i in range(4):
        for j in range(4):
            key_matrix[i][j] = ord(key[k]) % 65
            k += 1

def encrypt(message_vector):
    for i in range(4):
        cipher_matrix[i][0] = 0
        for j in range(4):
            cipher_matrix[i][0] += key_matrix[i][j] * message_vector[j][0]
        cipher_matrix[i][0] = cipher_matrix[i][0] % 26

def hill_cipher(message, key):
    get_key_matrix(key)
    cipher_text = ""
    if len(message) % 4 != 0:
        message += "X" * (4 - len(message) % 4)

    for i in range(0, len(message), 4):
        block = message[i:i + 4]

        for j in range(4):
            message_vector[j][0] = ord(block[j]) % 65

        encrypt(message_vector)

        cipher_text += "".join(chr(cipher_matrix[i][0] + 65) for i in range(4))

    return cipher_text

def main():
    message = "Superrabittu"
    key = "thankyouannayaaa"
    print(hill_cipher(message, key))

if __name__ == "__main__":
    main()
