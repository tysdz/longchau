letters_dict = {
    'A': '00000',
    'B': '00001',
    'C': '00010',
    'D': '00011',
    'E': '00100',
    'F': '00101',
    'G': '00110',
    'H': '00111',
    'I': '01000',
    'J': '01001',
    'K': '01010',
    'L': '01011',
    'M': '01100',
    'N': '01101',
    'O': '01110',
    'P': '01111',
    'Q': '10000',
    'R': '10001',
    'S': '10010',
    'T': '10011',
    'U': '10100',
    'V': '10101',
    'W': '10110',
    'X': '10111',
    'Y': '11000',
    'Z': '11001',
    'THANH': '1001100111000000111000111'
}

# Example usage
letter = 'THANH'
# Step 1: Encoding 'THANH' into a binary string
print('Name after encoding: ', letters_dict[letter])
X = letters_dict[letter]

# Step 2: Building Knapsack-based cryptography

a = [2, 7, 14, 30, 61, 122, 245, 490, 980, 1961, 3923, 7846, 15692, 31385, 62770, 125541, 251082, 502164, 1004328, 2008656, 4017313, 8034626, 16069252, 32138505, 64277010]
m = 64437423
w = 77 

# Generate public key
b = [(w * ai) % m for ai in a]

# Step 3: Encrypting X using the public key
T = sum(b[i] for i in range(len(X)) if X[i] == '1')

# Step 4: Decrypting T using the private key
# Function to find multiplicative inverse
def multiplicative_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1

w_inverse = multiplicative_inverse(w, m)
T_prime = (T * w_inverse) % m

# Recover original message
message = ''
remainder = T_prime
for ai in reversed(a):
    if ai <= remainder:
        message = '1' + message
        remainder -= ai
    else:
        message = '0' + message

print('Original message:', message)
