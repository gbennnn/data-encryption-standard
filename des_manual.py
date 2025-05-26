# Implementasi sederhana algoritma enkripsi DES dalam Python.
# Kode ini adalah demonstrasi dasar dari algoritma DES, dengan fokus pada konsep inti.
# Konstanta (tabel permutasi, s-box, dll.)
# Karena alasan panjang, tabel-tabel dipersingkat untuk tujuan edukasi/demonstrasi.

# DES Manual Implementation (Simplified Educational Version)

# Permutation tables (simplified, length 64)
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

IP_inv = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]

# Expansion table (E-box)
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# S-Box sederhana (4x4)
S_BOX = [
    [[14, 4, 13, 1],
     [2, 15, 11, 8],
     [3, 10, 6, 12],
     [5, 9, 0, 7]]
]

def permute(block, table):
    if max(table) > len(block):
        raise ValueError(f"Permutation table expects input of length {max(table)}, but got {len(block)}")
    return [block[i - 1] for i in table]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def string_to_bits(s):
    return [int(b) for char in s.encode('utf-8') for b in format(char, '08b')]

def bits_to_string(b):
    chars = [int(''.join(map(str, b[i:i + 8])), 2) for i in range(0, len(b), 8)]
    return bytes(chars).decode('utf-8', errors='ignore')

def s_box_substitution(bits):
    row = (bits[0] << 1) + bits[5]
    col = (bits[1] << 1) + bits[2]
    val = S_BOX[0][row % 4][col % 4]
    return [int(b) for b in format(val, '04b')]

def feistel(R, key):
    expanded = permute(R, E)[:6]  # 6-bit untuk 1 S-box
    xored = xor(expanded, key[:6])
    substituted = s_box_substitution(xored)
    # Pad hasil substitusi ke 32-bit (agar final hasil tetap 64-bit)
    return substituted + [0] * (32 - len(substituted))

def des_encrypt_block(plaintext, key):
    pt_bits = string_to_bits(plaintext)
    pt_bits = pt_bits[:64] + [0] * (64 - len(pt_bits))  # pad ke 64-bit

    key_bits = string_to_bits(key)
    key_bits = key_bits[:64] + [0] * (64 - len(key_bits))

    permuted = permute(pt_bits, IP)
    L, R = permuted[:32], permuted[32:]

    # 1 ronde Feistel
    new_R = xor(L, feistel(R, key_bits))
    new_L = R

    combined = new_L + new_R  # hasil = 64 bit

    final = permute(combined, IP_inv)
    return final

def bits_to_hex(bits):
    return hex(int(''.join(map(str, bits)), 2))[2:].zfill(16)

if __name__ == "__main__":
    # plaintext = input("Enter 8-character plaintext: ")[:8]
    # key = input("Enter 8-character key: ")[:8]
    plaintext = "Pertamia"  # Contoh plaintext
    key = "12345678"  # Contoh kunci

    ciphertext_bits = des_encrypt_block(plaintext, key)
    ciphertext_hex = bits_to_hex(ciphertext_bits)

    print("Ciphertext (hex):", ciphertext_hex)
