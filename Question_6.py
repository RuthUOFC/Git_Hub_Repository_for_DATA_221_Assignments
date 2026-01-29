from itertools import count


def distribution_analysis(numbers):
    Total_Elements = len(numbers)
    unique_numbers = sorted(list(set(numbers)))
    result = {}
    for key in unique_numbers:
        count = 0
        for n in numbers:
            if n <= key:
                count +=1

        percentage =(count/ Total_Elements) * 100
        result[key] = percentage

    return result


numbers = [3,1,2,3,4,2]
print(distribution_analysis(numbers))