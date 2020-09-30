# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

# simpler solution
def partition(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


class Sorter:

    def __init__(self, letters):
        self.letters = letters 
        self.positions_r = []
        self.positions_g = []
        self.positions_b = []

    def swap(self, positions, i):
        j = positions[-1]
        self.letters[i], self.letters[j] = self.letters[j], self.letters[i]


    def check(self, i):
        char = self.letters[i]

        if char == "R":
            if i in self.positions_r:
                self.positions_r.remove(i)
                return True
            return False

        if char == "G":
            if i in self.positions_g:
                self.positions_g.remove(i)
                return True
            return False

        if char == "B":
            if i in self.positions_b:
                self.positions_b.remove(i)
                return True
            return False

    def preswap(self, i):
        char = self.letters[i]

        if char == "R":
            self.swap(self.positions_r, i)
            del self.positions_r[-1]

        elif char == "G":
            self.swap(self.positions_g, i)
            del self.positions_g[-1]

        elif char == "B":
            self.swap(self.positions_b, i)
            del self.positions_b[-1]

    def arrange(self):

        count_r = self.letters.count('R')
        count_g = self.letters.count('G')
        count_b = len(self.letters) - count_r - count_g

        self.positions_r = range(count_r)
        self.positions_g = range(count_r, count_r+count_g)
        self.positions_b = range(count_r+count_g, count_r+count_g+count_b)

        i = 0
        while i < len(self.letters):
            print (self.letters)
            if self.check(i):
                i+=1
            else:
                self.preswap(i)
            if not self.positions_r and not self.positions_g and not self.positions_b:
                break

solution = Sorter(['G', 'B', 'R', 'R', 'B', 'R', 'G'])
solution.arrange()

assert (solution.letters == ['R', 'R', 'R', 'G', 'G', 'B', 'B'])

