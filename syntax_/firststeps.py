numbers = [1, 2, 4, 7, 10]
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for i in numbers:
        if i % 2 == 0:
            print(f"{i} is even")
            even_count += 1
        else:
            print(f"{i} is odd")
            odd_count += 1

    return {
        "even": even_count,
        "odd": odd_count
    }

result = count_even_odd(numbers)

print("\nSummary:")
print(f"Evens: {result['even']}")
print(f"Odds: {result['odd']}")


