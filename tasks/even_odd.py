__all__ = ("even_odd",)


# def even_odd(numbers: list[int]) -> float:
#     try:
#         first_sum = 0
#         second_sum = 0
#         for num in numbers:
#             if num % 2 == 0:
#                 first_sum += num
#             else:
#                 second_sum += num
#         return first_sum / second_sum
#     except ZeroDivisionError as e:
#         return 0

def even_odd(numbers: list[int]) -> float:
    try:
        return sum(filter(lambda x: x % 2 == 0, numbers)) / sum(filter(lambda x: x % 2 == 1, numbers))
    except ZeroDivisionError as e:
        return 0
