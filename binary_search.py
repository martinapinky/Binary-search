class BinarySearch(list):
    def __init__(self, a, b):
        self.length = a
        for i in range(1, a + 1):
            self.append(i * b)

# for binarylist = BinarySearch(10, 10)  ---[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    def search(self, value):
        first = 0
        last = self.length - 1
        found = False
        num_of_iterations = 1

        while first <= last and not found:
            midpoint = (first + last) // 2
            if self[midpoint] == value:
                found = True
            else:
                num_of_iterations += 1
                if value < self[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        found_dict = {'count' : num_of_iterations, 'index' : self.index(value)}
        return found_dict

# print(BinarySearch(10, 3))
one_to_twenty = BinarySearch(20, 1)
two_to_forty = BinarySearch(20, 2)
ten_to_thousand = BinarySearch(100, 10)
# print(one_to_twenty.search(16))
# print(two_to_forty.search(16))
print(two_to_forty)
print(two_to_forty.search(40))


