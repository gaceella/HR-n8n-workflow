# crypto.py
# --------------------------------------------
# Hill Cipher using Linear Algebra
# Correct, reversible, and stable implementation
# Alphabet = A-Z + space → mod 27
# --------------------------------------------

import numpy as np
import secrets

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
mod = len(alphabet)   # 27 characters


# ---------- Text / Number Conversion ----------

def text_to_nums(text):
    """
    Convert text to numeric list based on alphabet index.
    Unsupported characters are ignored.
    """
    text = text.upper()
    cleaned = ""
    for c in text:
        if c in alphabet:
            cleaned += c
    return [alphabet.index(c) for c in cleaned]


def nums_to_text(nums):
    """
    Convert numeric list back to text.
    """
    return "".join(alphabet[n] for n in nums)


# ---------- Modular Inverse Helpers ----------

def mod_inverse(a, m):
    """
    Finds modular inverse of integer a under modulo m.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def matrix_mod_inverse(K, mod):
    """
    Computes inverse of a 2x2 matrix under modulo arithmetic.
    """
    # Matrix elements
    a, b = K[0, 0], K[0, 1]
    c, d = K[1, 0], K[1, 1]

    # Determinant
    det = (a * d - b * c) % mod

    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        return None  # Not invertible

    # Adjugate matrix
    adj = np.array([[d, -b],
                    [-c, a]])

    # Inverse matrix mod N
    K_inv = (det_inv * adj) % mod
    return K_inv


# ---------- Secure Key Generation ----------

def generate_key_matrix():
    """
    Generates a secure random invertible 2x2 matrix key.
    """
    while True:
        K = np.array([[secrets.randbelow(mod), secrets.randbelow(mod)],
                      [secrets.randbelow(mod), secrets.randbelow(mod)]])
        K_inv = matrix_mod_inverse(K, mod)
        if K_inv is not None:
            return K, K_inv


# ---------- Encryption ----------

def encrypt(text, K):
    """
    Encrypt plaintext using:
    C = (K × P) mod 27
    """
    nums = text_to_nums(text)

    # Padding if odd length
    if len(nums) % 2 != 0:
        nums.append(alphabet.index(" "))

    encrypted = []

    for i in range(0, len(nums), 2):
        P = np.array([[nums[i]],
                      [nums[i + 1]]])

        C = (K @ P) % mod   # Linear Algebra core

        encrypted.extend(C.flatten())

    return nums_to_text(encrypted)


# ---------- Decryption ----------

def decrypt(cipher_text, K_inv):
    """
    Decrypt ciphertext using:
    P = (K_inv × C) mod 27
    """
    nums = text_to_nums(cipher_text)

    # Ciphertext must be even length
    if len(nums) % 2 != 0:
        return "ERROR: Invalid ciphertext length"

    decrypted = []

    for i in range(0, len(nums), 2):
        C = np.array([[nums[i]],
                      [nums[i + 1]]])

        P = (K_inv @ C) % mod

        decrypted.extend(P.flatten())

    # Remove possible padding space at end
    return nums_to_text(decrypted).rstrip()
