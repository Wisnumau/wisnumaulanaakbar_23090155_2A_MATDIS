# Anda ingin membuat sistem yang dapat memvalidasi alamat email berdasarkan pola umum, yaitu harus mengandung
# karakter "@", diikuti oleh domain yang valid.
# Deskripsi NFA:

# Keadaan: Q = {q0, q1, q2, q3, q4}
# Alfabet input: Σ = {a-z, A-Z, 0-9, @, ., -}
# Keadaan awal: q0
# Keadaan akhir: q4
# Fungsi transisi:
# δ(q0, alphanumeric) = q1
# δ(q1, alphanumeric) = q1
# δ(q1, '@') = q2
# δ(q2, alphanumeric) = q3
# δ(q3, alphanumeric) = q3
# δ(q3, '.') = q4
# δ(q4, alphanumeric) = q4
# Contoh:

# Input: "user@example.com"
# Output: True (valid)
import re

def validate_email(email):
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    return bool(pattern.match(email))

# Contoh penggunaan
email = "user@example.com"
print(validate_email(email))  # Output: True
