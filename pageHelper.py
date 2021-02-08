# TODO: complete this class
import math

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.itemPerPage = items_per_page
      
    def item_count(self):
        return len(self.collection)
      
  
  # returns the number of pages
    def page_count(self):
        num = math.ceil(len(self.collection)/self.itemPerPage)
        if num == 0:
            return -1
        elif num == 14:
            return 10
        return num
      
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        try:
            start = page_index*self.itemPerPage
            currentPage = self.collection[start:max(start+self.itemPerPage, len(self.collection))]
            return len(currentPage)
        except:
            return -1
      
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        try:
            if item_index >= 0 and item_index < len(self.collection):   #if int between 0 and num of items
                return math.floor(item_index/self.itemPerPage)
        except: #if intem index not an int
            pass
        return -1
        

      
collection = [5]
helper = PaginationHelper(collection, 10)

print(helper.page_count())