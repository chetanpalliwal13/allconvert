"""
Files to do conversion from tupleTo - list, dictionary, numpyArray, namedTuple, bytes, int, string, unicode
And also provide interface to do operation on tuple which not permitted in python to do.
e.g tuple modification, insert element in tuple, remove elemnt from tuple.
"""
import numpy

def insert(index, value, tupleo):
    """
    insert(...) method of tupleTo instance
    T.insert(index, object, tupleo)  -- insert object before index in tuple, tupleo
    """
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    convertlist.insert(index, value)
    return tuple(convertlist)
	
def append(value, tupleo):
    """
    append(...) method of tupleTo instance
    T.append(object, tupleo) -> None -- append object to end of tuple, tupleo
    """
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    convertlist.append(value)
    return tuple(convertlist)

def clear(tupleo):
    """
    clear(...) method of tupleoTo instance
    T.clear(tupleo) -> None -- Remove all elements from tuple, tupleo
    """
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    convertlist.clear()
    return tuple(convertlist)
	
def copy(tupleo):
    """
    clear(...) method of tupleoTo instance
    T.copy(tupleo) -> Tuple -- a shallow copy of tuple, tupleo
    """
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    return tuple(convertlist.copy())
	
def extend(value, tupleo):
    """
    extend(...) method of tupleoTo instance
    T.extend(iterable, tupleo) -> None -- extend tuple, tupleo by appending elements from the iterable
    """
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    if type(value) !=tuple:
        raise TypeError("{} is not tuple".format(value))
    convertlist = list(tupleo)
    convertlist.extend(list(value))
    return convertlist
	
def pop(tupleo, *index):
    """
    pop(...) method of tupleoTo instance
    T.pop(tupleo, index) -> item -- remove and return item at index (default last) from tuple, tupleo.
    Raises IndexError if list is empty or index is out of range
    """
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    if index:
        convertlist.pop(*index)
    else:
        convertlist.pop(len(convertlist)-1)
    return tuple(convertlist)
	
def remove(value, tupleo):
    """
    remove(...) method of tupleoTo instance
    T.remove(value, tupleo) -> None -- remove first occurrence of value from tuple, tupleo.
    Raises ValueError if the value is not present
    """
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    convertlist.remove(value)
    return tuple(convertlist)
	
def reverse(tupleo):
    """
    reverse(...) method of tupleTo instance
    T.reverse(tupleo) -- reverse *IN PLACE tuple, tupleo*
    """
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    return tupleo[::-1]
	
def sort(tupleo, key=None, reverse=False):
    """
    sort(...) method of tupleTo instance
    T.sort(tupleo, key=None, reverse=False) -> None -- stable sort *IN PLACE tuple, tupleo*
    """
    if type(tupleo) != tuple:
        raise TypeError("{} is not tuple".format(tupleo))
    convertlist = list(tupleo)
    convertlist.sort(key=key, reverse=reverse)
    return tuple(convertlist)


# Code for conversion of tuple, list of tuple to List and Dictionary.
# Conversion:
#    - Formal conversion
#    - Index based conversion

def tupleToDict(tupleTo, index=0):
    """
    tupleToDict(...) method of tupleTo instance
    T.tupleToDict(tupleTo, object) -> None -- convert tuple to Dictionary.
    if index given then index is key and remain elements are value in list format (default index 0)
    """
    if type(tupleTo) != tuple:
        raise TypeError("{} is not tuple".format(tupleTo))
    dict = {}
    if len(tupleTo)==0:
        return dict
    elif len(tupleTo)==1:
        dict.update({tupleTo[0]:''})
        return dict
    else:
        if index==0:
            dict.update({tupleTo[0]:list(tupleTo[1:])})
            return dict
        else:
            dict.update({tupleTo[index]:list(pop(tupleTo, index))})
            return dict
	
def tupleToList(tupleTo):
    """
    tupleToList(...) method of tupleTo instance
    T.tupleToList(tupleTo) -> None -- convert tuple to List to Full Depth Level.
    """
    if type(tupleTo)==tuple:
        tupleTo = list(tupleTo)
    for i in range(len(tupleTo)):
        if type(tupleTo[i])==tuple:
            tupleTo[i]=list(tupleTo[i])
            tupleToList(tupleTo[i])
        elif type(tupleTo[i])==list:
            tupleToList(tupleTo[i])
        else:
            pass
    return tupleTo

def tupleToArray(tupleTo, fullDepthLevel='No'):
    """
    tupleToArray(...) method of tupleTo instance
    T.tupleToArray(tupleTo, fullDepthLevel='No') -> numpy Array -- convert tuple to numpy Arrary to Full Depth Level.
    """
    if type(tupleTo) != tuple:
        raise TypeError("{} is not tuple".format(tupleTo))
    return numpy.array(tupleTo) if fullDepthLevel=='No' else return numpy.array(tupleToList(tupleTo))
