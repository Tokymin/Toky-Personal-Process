# Polybius Square encryption and decryption algorithm
class PolybiusSquare:
    def __init__(self, keyword_left, keyword_top, square_type='a'):
        # Initialize keywords and square
        self.keyword_left = keyword_left
        self.keyword_top = keyword_top
        self.square_type = square_type
        self.square = self.generate_square()

    def generate_square(self):
        # 5x5 Polybius square based on keyword
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        used_letters = set(self.keyword_left + self.keyword_top)
        remaining_letters = [c for c in alphabet if c not in used_letters]

        # Create the square based on keyword (left side and top)
        square = []
        if self.square_type == 'a':
            square = [
                list(self.keyword_left),
                list(remaining_letters[:5]),
                list(remaining_letters[5:10]),
                list(remaining_letters[10:15]),
                list(remaining_letters[15:])
            ]
        elif self.square_type == 'b':
            square = [
                list(self.keyword_top),
                list(remaining_letters[:5]),
                list(remaining_letters[5:10]),
                list(remaining_letters[10:15]),
                list(remaining_letters[15:])
            ]

        return square

    def encrypt(self, plaintext):
        ciphertext = []
        for char in plaintext.upper():
            found = False
            for row_idx, row in enumerate(self.square):
                if char in row:
                    col_idx = row.index(char)
                    ciphertext.append(self.keyword_left[row_idx] + self.keyword_top[col_idx])
                    found = True
                    break
            if not found:
                ciphertext.append(char)  # Non-alphabet characters remain unchanged
        return ' '.join(ciphertext)

    def decrypt(self, ciphertext):
        plaintext = []
        pairs = ciphertext.split()
        for pair in pairs:
            if len(pair) == 2:
                row_char, col_char = pair
                row_idx = self.keyword_left.index(row_char)
                col_idx = self.keyword_top.index(col_char)
                plaintext.append(self.square[row_idx][col_idx])
            else:
                plaintext.append(pair)
        return ''.join(plaintext)


# Example use case:
# We use the 'WHITE' and 'B' as keywords for both top and left in example (a).

keyword_left = "WHITE"
keyword_top = "BKNIH"
square_type = 'a'

polybius = PolybiusSquare(keyword_left, keyword_top, square_type)

# Example data you provided
ciphertext = "0B 01 D4 25 00 00 00 4C 75 E3 E5 00 01 59 3E 01 84 5A 93 C6 E9 2D 00 00 00 00 03 2F 30 2D 02 14 50 26 1C 11 8C 43 38 19 21 83 5E 15 13 7A 4A CF 1A 22 7C 58 02 15 00 FA C0 8E 47 94 27 3C 7D 4E 61 E0 9D 6A 3D 63 49 AC BD 70 39 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
print("Decrypted text:", polybius.decrypt(ciphertext))
