def validate_isbn(isbn):
    """
    Validasi ISBN-10 atau ISBN-13.
    """
    isbn = isbn.replace("-", "").replace(" ", "") 

    # Validasi ISBN-10
    if len(isbn) == 10:
        return validate_isbn10(isbn)

    # Validasi ISBN-13
    elif len(isbn) == 13:
        return validate_isbn13(isbn)

    else:
        return False, "Panjang ISBN tidak valid. Harus 10 atau 13 digit."

def validate_isbn10(isbn):
    """
    Validasi ISBN-10 menggunakan aturan modulo 11.
    """
    try:
        total = 0
        for i in range(9):
            total += (10 - i) * int(isbn[i])

        # Cek digit terakhir (bisa berupa 'X')
        if isbn[9].upper() == 'X':
            total += 10
        else:
            total += int(isbn[9])

        if total % 11 == 0:
            return True, "ISBN-10 valid."
        else:
            return False, "ISBN-10 tidak valid."
    except ValueError:
        return False, "ISBN-10 berisi karakter tidak valid."

def validate_isbn13(isbn):
    """
    Validasi ISBN-13 menggunakan aturan modulo 10.
    """
    try:
        total = 0
        for i in range(12):
            multiplier = 1 if i % 2 == 0 else 3
            total += multiplier * int(isbn[i])

        check_digit = (10 - (total % 10)) % 10
        if check_digit == int(isbn[12]):
            return True, "ISBN-13 valid."
        else:
            return False, "ISBN-13 tidak valid."
    except ValueError:
        return False, "ISBN-13 berisi karakter tidak valid."

# Program utama
if __name__ == "__main__":
    print("Selamat datang di Program Validasi ISBN Arzis")
    print()
    print("Silahkan Masukkan ISBN yang ingin kamu cek")
    isbn = input("Masukkan ISBN (10 atau 13 digit): ")
    valid, message = validate_isbn(isbn)
    print(message)
