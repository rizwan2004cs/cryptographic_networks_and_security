# Function to create the matrix from the key
def create_matrix(key):
    key = key.upper().replace("J", "I")  # Treat 'J' as 'I'
    matrix = ""
    for char in key:
        if char not in matrix:
            matrix += char
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in matrix:
            matrix += char
    return [matrix[i:i+5] for i in range(0, 25, 5)]  # 5x5 matrix

# Function to find the position of a letter in the matrix
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

# Function to prepare the text (remove spaces, make it uppercase, and handle repeated letters)
def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared_text = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared_text.append(text[i] + 'X')
            i += 1
        else:
            prepared_text.append(text[i:i+2])
            i += 2
    if len(prepared_text[-1]) == 1:
        prepared_text[-1] += 'X'
    return prepared_text

# Function to encrypt a digraph (pair of letters)
def encrypt(matrix, digraph):
    row1, col1 = find_position(matrix, digraph[0])
    row2, col2 = find_position(matrix, digraph[1])

    if row1 == row2:  # Same row: Move right
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Same column: Move down
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  # Rectangle rule: Swap corners
        return matrix[row1][col2] + matrix[row2][col1]

# Main function to encrypt the plaintext
def playfair_encrypt(plaintext, key):
    matrix = create_matrix(key)
    prepared_text = prepare_text(plaintext)
    ciphertext = "".join(encrypt(matrix, pair) for pair in prepared_text)
    return ciphertext

# Example usage
key = "KEYWORD"
plaintext = "HELLO WORLD"
ciphertext = playfair_encrypt(plaintext, key)

print("Ciphertext:", ciphertext)
