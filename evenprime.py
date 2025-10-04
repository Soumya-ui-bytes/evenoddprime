even_count = 0
odd_count = 0
prime_count = 0

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
print(f"Prime numbers: {prime_count}")