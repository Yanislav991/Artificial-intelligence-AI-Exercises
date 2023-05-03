# Define GF(2) operations

def gf2_add(x, y):
    """
    Compute the addition of two binary bits using GF(2) (XOR operation)

    Args:
        x (int): binary bit 0 or 1
        y (int): binary bit 0 or 1

    Returns:
        int: binary bit 0 or 1 as the sum of x and y using GF(2)
    """
    return x ^ y


def gf2_mul(x, y):
    """
    Compute the multiplication of two binary bits using GF(2) (AND operation)

    Args:
        x (int): binary bit 0 or 1
        y (int): binary bit 0 or 1

    Returns:
        int: binary bit 0 or 1 as the product of x and y using GF(2)
    """
    return x & y


def str_to_bin(text):
    """
    Convert string to binary representation

    Args:
        text (str): Input string to be converted

    Returns:
        str: Binary representation of the input string
    """
    binary = ""
    for c in text:
        # Convert each character to its ASCII value and then to binary
        binary += format(ord(c), "08b")
    return binary


def bin_to_str(binary):
    """
    Convert binary representation to string

    Args:
        binary (str): Binary representation to be converted

    Returns:
        str: Converted string from binary
    """
    text = ""
    chunk_size = 8
    num_chunks = len(binary) // chunk_size
    for i in range(num_chunks):
        # Convert each 8-bit chunk to its corresponding ASCII character
        chunk = binary[i * chunk_size: (i + 1) * chunk_size]
        text += chr(int(chunk, 2))
    return text


def encrypt(key, plaintext):
    """
    Encrypt plaintext with key using GF(2)

    Args:
        key (str): Binary string to be used as key for encryption
        plaintext (str): Binary string to be encrypted

    Returns:
        str: Encrypted binary string
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        key_bit = int(key[i % len(key)])
        plaintext_bit = int(plaintext[i])
        ciphertext_bit = gf2_add(key_bit, plaintext_bit)
        ciphertext += str(ciphertext_bit)
    return ciphertext


def decrypt(key, ciphertext):
    """
    Decrypt ciphertext with key using GF(2)

    Args:
        key (str): Binary string to be used as key for decryption
        ciphertext (str): Binary string to be decrypted

    Returns:
        str: Decrypted binary string
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        key_bit = int(key[i % len(key)])
        ciphertext_bit = int(ciphertext[i])
        plaintext_bit = gf2_add(key_bit, ciphertext_bit)
        plaintext += str(plaintext_bit)
    return plaintext


# Choose a key
key = "11011001"

# Generate a random plaintext message
plaintext = "Hello, world!"

# Convert plaintext to binary representation
plaintext_binary = str_to_bin(plaintext)

# Encrypt the message
ciphertext = encrypt(key, plaintext_binary)

# Decrypt the ciphertext
decrypted_plaintext_binary = decrypt(key, ciphertext)

# Convert decrypted binary representation back to string
decrypted_plaintext = bin_to_str(decrypted_plaintext_binary)

# Print the results
print("Key:", key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Plaintext:", decrypted_plaintext)
