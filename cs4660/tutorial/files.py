"""Files tests simple file read related operations"""

from io import open
from tutorial import lists

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
         
        print(file_path)
        f = open(file_path, encoding='utf-8')
        text = f.read() 
        lines = text.split('\n') 
        for line in lines:
            if len(line) > 0:
                parts = list(map(int, line.split(' '))) 
                self.numbers.append(parts) 
        print(self.numbers)
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """

    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        pass
        return lists.get_avg(self.numbers[line_number])

    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        pass
        return max(self.numbers[line_number])
        

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        pass
        return min(self.numbers[line_number])

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        pass
        return sum(self.numbers[line_number])
        
