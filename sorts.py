def qSort(
          l,
          criterion = lambda x: x,
          pickPivot = lambda l, head, tail: (head + tail) / 2
          ascending = True
         ):
    """qSort(
          l,
          [criterion] = lambda x: x,
          [pickPivotIndex] = lambda head, tail: (head + tail) / 2
          [ascending] = True
         ):
         
       ---Sorts a given list l by sort [criterion], using quick sort---
       
       l is the list to sort
       
       [criterion] is the desired sorting criterion. It must be a single
           argument function that returns a number. the list will be sorted
           by this number.
           
       [pickPivot] is the function to choose the pivot for partitioning.
           it returns the value of the selected pivot and must receive 3 arguments:
           the list, the sublist leftmost index and the sublist rightmost index
           
       [ascending] indicates which order the list will be sorted
    """
    def partition(head, tail):
        pivot = pickPivot(l, head, tail)
        left = head
        right =  tail
        while left < right:
            while l[left] <= pivot and left < right:
                left = left + 1
            while l[right] > pivot and left < right:
                right = right - 1
            if left < right:
                aux = l[left]
                l[left] = l[right]
                l[right] = aux




















