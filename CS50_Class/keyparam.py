words = ["zebra", "ant", "elephant", "dog", "cat"]

last_letter = sorted(words, key=lambda word: word[-1])

print(" ".join(last_letter))

numbers = [10, 102, 450, 3, 23, 45, 67]

#order = sorted(numbers, key=lambda cijfer: cijfer % 2 == 0)
#order = sorted(numbers, key=lambda x: (x % 2 != 0, x), reverse=True)
#order = sorted(numbers, key=lambda x: (x % 2 != 0, -x))

order = sorted(numbers, key=lambda cijfer: (cijfer % 2 != 0, -cijfer, len(str(cijfer))))

print(" ".join((map(str, order))))  