def isSorted(l,
             criterion = lambda x: x,
             ascending = True
             ):
    """isSorted(l,
              [criterion] = lambda x: x,
              [ascending] = True
             ):
       
       ---Checks if a given list is sorted by a given criterion---
       
       l is the list in which the search will be performed.
    
       [criterion] is a single parameter function that calculates the value of a
           given element in l.
           
       [ascending] is a flag to tell the function if the list is ordered
           increasingly or decreasingly. 
    """
    
    for i in xrange(1, len(l)):
        if (  ( (-1)**(1 + ascending) ) * criterion(l[i]) <
           ( (-1)**(1 + ascending) ) * criterion(l[i - 1])  ):
            return False
    return True

def binSearch(l,
              target,
              elementValue = lambda x: x,
              targetValue = lambda x: x,
              ascending = True,
              notFound = -1
             ):
    """binSearch(l,
              target,
              [elementValue] = lambda x: x,
              [targetValue] = lambda x: x,
              [ascending] = True,
              [notFound] = -1):
    
    ---Performs a binary search in a given list---
    
    l is the list in which the search will be performed.
    
    target is the searched element.
    
    [elementValue] is a single parameter function that calculates the value of a
        given element in l.
        
    [targetValue] is a single parameter function that calculates the value the target
        parameter
        
    The search compares targetValue(target) to elementValue(l[i]) to determine the relation
        between them. With this the function becomes more generic.
        
    [ascending] is a flag to tell the function if the list is ordered
        increasingly or decreasingly.
        
    [notFound] is the return value if the element is not in the list.
    
    IMPORTANT: the list MUST be sorted by the criteria estabilished by the [elementValue]
        function AND the [ascending] flag, or it will return inconsistent results.
        In order to keep the complexity at log(n), the search function can not
        check if the list is ordered. There is the isOrdered function for that.
    """
    
    targetValue = ( (-1)**(1 + ascending) ) * targetValue(target)
    def f(head, tail):
        if head > tail:
            return notFound
        else:
            m = (head + tail) / 2
            valueCurr = ( (-1)**(1 + ascending) ) * elementValue(l[m])
            if valueCurr == targetValue:
                return m
            elif valueCurr > targetValue:
                return f(head, m - 1)
            else:
                return f(m + 1, tail)
    return f(0, len(l) - 1)
    
def binSearch(l,
              target,
              compare = lambda target, element:
                        1 if target > element else (-1 if target < element else 0),
              ascending = True,
              notFound = -1
             ):
    """binSearch(l,
              target,
              [compare] = lambda target, element:
                          1 if target > element else (-1 if target < element else 0),
              [ascending] = True,
              [notFound] = -1):
    
    ---Performs a binary search in a given list---
    
    l is the list in which the search will be performed.
    
    target is the searched element.
    
    [compare] is a two parameter function to compare the target element with an
        element from the list l. it must return a value larger than zero
        if the first argument is larger than the second; smaller than zero if
        the first argument is smaller than the second and zero if they are equal
        
    [ascending] is a flag to tell the function if the list is ordered
        increasingly or decreasingly.
        
    [notFound] is the return value to be used if the element is not in the list.
    
    IMPORTANT: the list MUST be sorted by the implicit criterion estabilished 
        by the [compare] function AND the [ascending] flag, or it will return
        inconsistent results.
        In order to keep the complexity at log(n), the search function can not
        check if the list is ordered. There is the isSorted function for that.
    """
    
    def f(head, tail):
        if head > tail:
            return notFound
        else:
            m = (head + tail) / 2
            comparison = ( (-1)**(1 + ascending) ) * compare(target, l[m])
            if comparison == 0:
                return m
            elif comparison < 0:
                return f(head, m - 1)
            else:
                return f(m + 1, tail)
    return f(0, len(l) - 1)
    

def seqSearch(l,
              target,
              elementValue = lambda x: x,
              targetValue = lambda x: x,
              notFound = -1
             ):
    """seqSearch(l, target, elementValue = lambda x: x, targetValue = lambda x: x, notFound = -1):
    
    l is the list in which the search will be performed.
    
    target is the searched element.
    
    [elementValue] is a single parameter function that calculates the value of a
        given element in l.
        
    [targetValue] is a single parameter function that calculates the value the target
        parameter
        
    The search compares targetValue(target) to elementValue(l[i]) to determine the relation
        between them. With this the function becomes more abstract.
        
    [notFound] is the return value if the element is not in the list.
    
    """
    
    targetValue = targetValue(target)
    for i in xrange(len(l)):
        if targetValue == elementValue(l[i]):
            return i
    return notFound
    
def seqSearch(l,
              target,
              compare = lambda target, element: target == element
              notFound = -1
             ):
    """seqSearch(l, target, elementValue = lambda x: x, targetValue = lambda x: x, notFound = -1):
    
    l is the list in which the search will be performed.
    
    target is the searched element.
    
    [compare] is a two argument function to compare the target element with an
        element from the list. it must return True for equal elements and
        False for distinct ones.
        
    The search compares targetValue(target) to elementValue(l[i]) to determine the relation
        between them. With this the function becomes more abstract.
        
    [notFound] is the return value if the element is not in the list.
    
    """
    
    for i in xrange(len(l)):
        if compare(target, l[i]):
            return i
    return notFound
    
def indexBinSearch(l,
              target,
              compare = lambda target, element:
                        1 if target > element else (-1 if target < element else 0),
              ascending = True,
              valueFound = -1
             ):
    """indexBinSearch(l,
              target,
              [compare] = lambda target, element:
                          1 if target > element else (-1 if target < element else 0),
              [ascending] = True,
              [notFound] = -1):
    
    ---Performs a binary search in a given list where an element is NOT expected
       to be found and returns the index where it should be---
    
    l is the list in which the search will be performed.
    
    target is the searched element.
    
    [compare] is a two parameter function to compare the target element with an
        element from the list l. it must return a value larger than zero
        if the first argument is larger than the second; smaller than zero if
        the first argument is smaller than the second and zero if they are equal
        
    [ascending] is a flag to tell the function if the list is ordered
        increasingly or decreasingly.
        
    [valueFound] is the return value to be used if the element IS, in fact, in the list.
    
    IMPORTANT: the list MUST be sorted by the implicit criterion estabilished 
        by the [compare] function AND the [ascending] flag, or it will return
        inconsistent results.
        In order to keep the complexity at log(n), the search function can not
        check if the list is ordered. There is the isSorted function for that.
    """
    
    def f(head, tail):
        if head == tail:
            return (head if vertex.name < Vertex.vertices[head].name
                         else head - 1
                   )
        else:
            m = (head + tail) / 2
            comparison = ( (-1)**(1 + ascending) ) * compare(target, l[m])
            if comparison == 0:
                return valueFound
            elif comparison < 0:
                return f(head, m - 1)
            else:
                return f(m + 1, tail)
    return f(0, len(l) - 1)
    
    
    
    
    
    
    
