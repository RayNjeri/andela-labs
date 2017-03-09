class BinarySearch(object):
  def __init__(self, a, b):
    self.a = a
    self.b = b
    self.myList = list(range(b,(a*b)+1,b))

  def __getitem__(self , number):
    return self.myList[number]
  def __setitem__(self, number, value):
    return self.myList[number] == value


  def search(self,value):
    first_index = 0
    mid_index = int(self.a/2)
    last_index = self.a-1
    count = 0
    

    if self.myList[first_index] == self.myList[last_index]:
      return {'count': 0, 'index': last_index}
    elif self.myList[last_index] == value:
      return {'count': 0, 'index': last_index}

    if self.myList[first_index] == self.myList[last_index]:
      return {'count': 0, 'index':last_index}
    else:

      while first_index <= last_index:
        count += 1


      if self.myList[mid_index] == value:
        return {'count':count, 'index': mid_index}
      elif value > self.myList[mid_index]:
        first_index = mid_index + 1
      elif value < self.myList[mid_index]:
        self.myList[first_index] = self.myList[mid_index] - 1
      elif self.myList[first_index] > self.myList[last_index]:
        return  {'count' : 0, 'index' : -1}

    
        



y = BinarySearch(20,2)
print(y.search(5))
print("done")



    




      
     

      
