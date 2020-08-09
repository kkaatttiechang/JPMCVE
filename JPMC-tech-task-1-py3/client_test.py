import unittest
from client3 import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    s, bp, ap, p = getDataPoint(quotes[0])
    self.assertEqual(p,120.84)
    s, bp, ap, p = getDataPoint(quotes[1])
    self.assertEqual(p,119.775)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    s, bp, ap, p1 = getDataPoint(quotes[0])
    s, bp, ap, p2 = getDataPoint(quotes[1])
    self.assertTrue(getRatio(p1, p2)>0)

  """ ------------ Add more unit tests ------------ """
  def test_if_zeroOrNeg(self):
    quotes = [
      {'top_ask': {'price': -119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': -120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'GHI'}
    ]
    s, bp, ap, p1 = getDataPoint(quotes[0])
    s, bp, ap, p2 = getDataPoint(quotes[1])
    s, bp, ap, p3 = getDataPoint(quotes[2])
    self.assertIsNone(getRatio(p1, p2))
    self.assertIsNone(getRatio(p2, p3))
    self.assertIsNone(getRatio(p2, p1))
    self.assertTrue(getRatio(p2, 90)>0)

if __name__ == '__main__':
    unittest.main()
