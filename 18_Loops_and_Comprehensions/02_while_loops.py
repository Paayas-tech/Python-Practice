# 1. Standard while loop
count = 1
while count <= 3:
    print("While count:", count)
    count += 1

# 2. Control flow: continue and break
num = 0
while num < 10:
    num += 1

    # Skip even numbers
    if num % 2 == 0:
        continue

    # Stop once threshold is reached
    if num > 7:
        print("Breaking loop at:", num)
        break

    print("Odd number processed:", num)

# 3. while True with an explicit exit condition
attempts = 0
while True:
    attempts += 1
    if attempts >= 3:
        print("Max attempts reached, stopping.")
        break