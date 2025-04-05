# Create a tuple with the first 5 prime numbers.

primes = []

def is_prime(n):
    # Kiểm tra xem n có phải là số nguyên tố không
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tìm 5 số nguyên tố đầu tiên
num = 2  # Bắt đầu từ số 2
while len(primes) < 5:
    if is_prime(num):
        primes.append(num)
    num += 1

# Tạo tuple từ danh sách số nguyên tố
prime_tuple = tuple(primes)

print(prime_tuple)
