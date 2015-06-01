def merge_sort(sequence):
    if len(sequence) < 2:
        return sequence
    m = len(sequence) / 2
    return merge(merge_sort(sequence[:m]), merge_sort(sequence[m:]))


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

LIS = [1,232,4,3423,4,231,23,214,23,51,53,46,54,6,423,5,46,54,7645,8,5476,5,3,423,543,75,52465,47,34,53,534,674,743,546,4576,34,34645]
print merge_sort(LIS)[::-1]