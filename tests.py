import unittest

import PrioritizeValues

class TestPrioritizeValues(unittest.TestCase):
  def test_comparisons(self):
    pv = PrioritizeValues.initPrioritizeValues(lambda a: (a, 1/a))

    self.assertFalse(pv(1) < pv(1))
    self.assertTrue(pv(1) <= pv(1))
    self.assertTrue(pv(1) == pv(1))
    self.assertFalse(pv(1) != pv(1))
    self.assertTrue(pv(1) >= pv(1))
    self.assertFalse(pv(1) > pv(1))

    self.assertTrue(pv(1) < pv(2))
    self.assertTrue(pv(1) <= pv(2))
    self.assertFalse(pv(1) == pv(2))
    self.assertTrue(pv(1) != pv(2))
    self.assertFalse(pv(1) >= pv(2))
    self.assertFalse(pv(1) > pv(2))

    self.assertFalse(pv(2) < pv(1))
    self.assertFalse(pv(2) <= pv(1))
    self.assertFalse(pv(2) == pv(1))
    self.assertTrue(pv(2) != pv(1))
    self.assertTrue(pv(2) >= pv(1))
    self.assertTrue(pv(2) > pv(1))


unittest.main()
