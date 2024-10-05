def get_count(number: int, divisor: int) -> int:
    count = 0
    while number > (divisor - 1):
        number -= divisor
        count += 1
    return count