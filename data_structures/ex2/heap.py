def heapsort(arr):
 # Initialize a new heap
 he = Heap()

 # loop through the array and insert each element into the heap
 for elem in arr:
  he.insert(elem)

 # Initializ a new list
 narr = []
 
 # Get the length of the heap
 size = he.get_size()

 # Loop through till we get to the size of the heap
 # and insert each max element at the beginning of the list.
 # This sorts the heap without calling the sorted/sort method.
 # The delete the item from the heap.
 for i in range(0, size):
  narr.insert(0, he.get_max())
  he.delete()

 # Return the newly created list
 return narr

 # NOTES:
 # I assumed it wanted us to create a heapsort with using the Heap class,
 # otherwise, I don't see the point in having the heap there. The tests wanted
 # it to be min -> max, while the heap is a max heap, so I used the
 # for in range to do the sorting for a min -> max. I could have used the
 # sorted(he.storage), but that wouldn't delete the value ones it was done
 # from the heap. Or I could have done, sorted(narr) and just had them inserted
 # from max -> min but I felt if I was already doing a loop I could just
 # have just inserted at the beginning of the list and then deleted it
 # from the heap.
 

class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2