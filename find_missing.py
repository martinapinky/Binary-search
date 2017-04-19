def find_missing(list1, list2):
    missing_number = sum(list2) - sum(list1)
    if missing_number < 0:
        missing_number = missing_number * -1
    return missing_number

print(find_missing([1,2,3,4,5], [1,2,3,4]))