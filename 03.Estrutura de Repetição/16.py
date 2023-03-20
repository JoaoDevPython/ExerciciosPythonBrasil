
fibonacci = [0, 1]
while fibonacci[- 1] < 500:
    fibonacci.append(fibonacci[- 1] + fibonacci[- 2])
print(f'{", ".join(map(str, fibonacci))}')
