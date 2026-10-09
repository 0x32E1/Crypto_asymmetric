import re
from gmpy2 import isqrt, invert, is_square, mpz
from Crypto.Util.number import long_to_bytes

with open("crypto.py") as f:
    src = f.read()

n = mpz(int(re.search(r"n\s*=\s*(\d+)", src).group(1)))
e = int(re.search(r"e\s*=\s*(\d+)", src).group(1))

with open("ciphertext.txt") as f:
    ct_hex = f.read().strip()
c = int(ct_hex, 16)

A = isqrt(n)
if A * A < n:
    A += 1
A2 = A * A
B2 = A2 - n

i = 0
while not is_square(B2):
    A += 1
    B2 += 2 * A - 1
    i += 1

B = isqrt(B2)
p = A + B
q = A - B
assert p * q == n, "factorization failed"

phi = (p - 1) * (q - 1)
d = invert(e, phi)

flag = long_to_bytes(int(pow(c, d, n)))
print(f"iterations: {i}")
print(f"p = {p}")
print(f"q = {q}")
print(f"flag: {flag.decode()}")

with open("solution.txt", "wb") as f:
    f.write(flag)
