from itertools import zip_longest
import operator

def initPrioritizeValues(value_generator_function):
  '''
  Creates a PrioritizeValues class that can be compaire instances of its self
  value_generator_function is a function that creates the values that will be
    compared to.
  The the further left or closer to the top values have higher priority.
  '''
  class PrioritizeValues:
    def __init__(self, *argv):
      '''
      argv are values that are passed into value_generator_function
      '''
      self.values = tuple(value_generator_function(*argv))
      if len(self.values) <= 0: raise ValueError('No values to compare.')

    def __iter__(self):
      return iter(self.values)

    def __len__(self):
      return len(self.values)

    @staticmethod
    def get_value_generator_function():
      return value_generator_function

    def compare_all(self, other, comp_function):
      '''
      Compares each of the PrioritizeValues instances to each other with comp_function.
      If all comparisons are true then True is returned else False
      '''
      if self.get_value_generator_function() != other.get_value_generator_function():
        raise ValueError('Uses different value_generator_function')
      if len(self) != len(other):
        raise ValueError('Unequal number of values to compare.')

      return all(comp_function(*values) for values in zip(self, other))

    def __eq__(self, other):
      # ==
      return self.compare_all(other, operator.eq)
    def __ne__(self, other):
      # !=
      return self.compare_all(other, operator.ne)

    def compare_priority(self, other, comp_function, return_if_equal):
      '''
      comp_function is called on the first non-equal values in self and other.
      If all values are equal return_if_equal is returned
      '''
      for left, right in zip(self, other):
        if left == right: continue
        return comp_function(left, right)
      return return_if_equal

    def __lt__(self, other):
      # <
      return self.compare_priority(other, operator.lt, False)
    def __gt__(self, other):
      # >
      return self.compare_priority(other, operator.gt, False)

    def __le__(self, other):
      # <=
      return self.compare_priority(other, operator.le, True)
    def __ge__(self, other):
      # >=
      return self.compare_priority(other, operator.ge, True)

    def __str__(self):
      return 'PrioritizeValues ' + str(self.values)

  return PrioritizeValues
