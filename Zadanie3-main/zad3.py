import random
import string

def create_secure_password(password_length):
    errors = 0
    while True:
        try:
            password_length = int(password_length)
            if password_length < 8:
                errors += 1
                if errors > 1:
                    return "nie poprawna liczba wyjscie z programu"
                print("Długośc hasła powinna wynosić minimum 8 znaków")
                continue
            break
        except ValueError:
            errors += 1
            if errors > 1:
                return "nie poprawny znak, wyjście z programu"
            print("złe dane, wpisz numer.")

    
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
   
    password = "".join(random.choices(allowed_chars, k=password_length))

    

    return password

print(create_secure_password(int(input("Jak długie ma być twoje hasło ?"))))