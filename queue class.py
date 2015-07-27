class Queue(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Inserts one element into queue""" 
        if not e in self.vals:
            self.vals.append(e)

    def remove(self):
        """Remove value from queue and return it
        If queue empty, raise ValueError"""
        try:
            self.vals.pop()
        except:
            raise ValueError('list is empty')
            
            