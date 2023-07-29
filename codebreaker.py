import hashlib
import itertools
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_password(candidate):
    print(f'Trying: {candidate}')
    if hashlib.sha1(candidate.encode()).hexdigest() == target_hash:
        return candidate
    return None

def crack_password(length):
    for candidate in itertools.product(chars, repeat=length):
        password_candidate = ''.join(candidate)
        result = check_password(password_candidate)
        if result:
            return result
    return None
    
def main():
    print("\033c")
    password = 'ac'
    global chars, target_hash
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    target_hash = hashlib.sha1(password.encode()).hexdigest()

    with ThreadPoolExecutor() as executor:
        for length in range(1, len(password) + 1):
            tasks = [executor.submit(crack_password, length) for i in range(4)] # Adjust the number 4 according to the available CPU cores
            for future in as_completed(tasks):
                result = future.result()
                if result:
                    print(f'The password is {result}')
                    return


if __name__ == '__main__':
    main()