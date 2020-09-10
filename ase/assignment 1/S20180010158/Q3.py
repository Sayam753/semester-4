# Question 3
class IncreasingList(list):
    def __init__(self):
        super().__init__()

    def append(self, val):
        """
        first, it removes all elements from the list that have greater values than val, starting from the last one, and once there are no greater element in the list, it appends val to the end of the list
        """
        for i in range(len(self)-1, -1, -1):
            if self[i] > val:
                self.remove(self[i])
        super().append(val)

    def pop(self):
        """
        removes the last element from the list if the list is not empty, otherwise, if the list is empty, it does nothing
        """
        if len(self) != 0:
            super().pop()

    def __len__(self):
        """
        returns the number of elements in the list
        """
        return super().__len__()
