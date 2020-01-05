import ctypes 

class DynamicArray(object):
    
    def __init__(self):
        self.n = 0 # counts of the actual elements 
        self.capacity = 1 # capacity to which the array can hold the elements 
        self.A = self.make_array(self.capacity) # special method that creates an array

    def __len__(self):
        """return total counts of elements in an array"""
        return self.n 

    def __getItem__(self, k):
        """returns the item at kth location"""
        if not 0 <= k < self.n:
            return IndexError ('Index out of Range!')
        
        return self.A[k]

    def append(self, element):
        if self.n == self.capacity:
            self._resize = (self.capacity * 2) # raise the capacity to 2 times
            # if total counts becomes equal to capacity 
     
        self.A[self.n] = element 
        self.n += 1 

    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B 
        self.capacity = new_cap 

    def make_array(self, new_cap):
        """makes an array with new capacity """

        return (new_cap * ctypes.py_object)()

arr = DynamicArray()

print(arr.append(1))
print(len(arr))