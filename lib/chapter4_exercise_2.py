def encode(text, key):
    cipher = make_cipher(key)

    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        print(ciphered_char)
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    # encrypted = 'EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL'
    # key = 'secretkey'
    cipher = make_cipher(key)
    print('cipher',cipher)
    # ['s', 'e', 'c', 'r', 't', 'k', 'y', 'a', 'b', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'z']
    plaintext_chars = []
    for i in encrypted:
        # for each letter in encrypted var
        # plain_char = cipher[65 - ord(i)]
        plain_char = cipher[ord(i) - 65]
        # create a new var called plain_char = 
        print('plain char',plain_char)
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    print('key',key)
    alphabet = [chr(i + 97) for i in range(0, 26)]
    print('alphabet',alphabet)
    cipher_with_duplicates = list(key) + alphabet
    print('cipher with duplicates',cipher_with_duplicates)
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")