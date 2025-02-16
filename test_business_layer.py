"""
Unit tests for TrafficDataManager.

Author: Ayush Kapoor
"""

import unittest
from Business_Layer.business_layer import TrafficDataManager
from Model_Layer.TrafficDataRecord import TrafficDataRecord

class TestTrafficDataManager(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by initializing a TrafficDataManager
        with a small set of test data.
        """
        self.manager = TrafficDataManager('traffic-data.csv')
        self.manager.records = [
            TrafficDataRecord("4805026", "Drumheller", "2000", "Daily Vehicles (per km of road)", "", "2440.67151"),
            TrafficDataRecord("4805026", "Drumheller", "2001", "Daily Vehicles (per km of road)", "", "2328.48399"),
        ]

    def test_add_record(self):
        """
        Test if the program correctly adds a new traffic data record.
        """
        new_record = TrafficDataRecord("4805026", "Drumheller", "2002", "Daily Vehicles (per km of road)", "", "1482.75917")
        self.manager.add_record(new_record)

        self.assertEqual(len(self.manager.records), 3)
        self.assertEqual(self.manager.get_record(2).csduid, "4805026")
        self.assertEqual(self.manager.get_record(2).csd, "Drumheller")
        self.assertEqual(self.manager.get_record(2).period, "2002")
        self.assertEqual(self.manager.get_record(2).indicator_summary, "Daily Vehicles (per km of road)")
        self.assertEqual(self.manager.get_record(2).unit_of_measure, "")
        self.assertEqual(self.manager.get_record(2).original_value, "1482.75917")

    def test_update_record(self):
        """
        Test if the program correctly updates an existing traffic data record.
        """
        updated_record = TrafficDataRecord("4805026", "Drumheller", "2000", "Daily Vehicles (per km of road)", "", "2500.00000")
        self.manager.update_record(0, updated_record)
        record = self.manager.get_record(0)

        self.assertEqual(record.csduid, "4805026")
        self.assertEqual(record.csd, "Drumheller")
        self.assertEqual(record.period, "2000")
        self.assertEqual(record.indicator_summary, "Daily Vehicles (per km of road)")
        self.assertEqual(record.unit_of_measure, "")
        self.assertEqual(record.original_value, "2500.00000")

if __name__ == '__main__':
    unittest.main()
