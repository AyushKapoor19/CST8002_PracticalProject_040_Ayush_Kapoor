import unittest
from Business_Layer.business_layer import TrafficDataManager, TrafficDataRecord

class TestTrafficDataManager(unittest.TestCase):

    def setUp(self):
        """
        Set up a TrafficDataManager with sample test data.
        """
        self.manager = TrafficDataManager('dailyvehiclesdownload.csv')
        self.manager.records = [
            TrafficDataRecord("4805026", "Drumheller", "2000", "Daily Vehicles", "", 2440.67),
            TrafficDataRecord("4805026", "Drumheller", "2001", "Daily Vehicles", "", 2328.48)
        ]

    def test_get_record_valid(self):
        """
        Test getting a valid record by index.
        """
        record = self.manager.get_record(1)
        self.assertEqual(record.CSD, "Drumheller")
        self.assertEqual(record.Period, "2001")

    def test_get_record_invalid_index(self):
        """
        Test getting a record with an out-of-range index.
        """
        with self.assertRaises(IndexError):
            self.manager.get_record(5)

    def test_add_invalid_record(self):
        """
        Test adding an invalid record (not a TrafficDataRecord).
        """
        with self.assertRaises(TypeError):
            self.manager.add_record(["Invalid", "Record"])

    def test_update_record_valid(self):
        """
        Test updating an existing record.
        """
        updated_record = TrafficDataRecord("4805026", "Drumheller", "2000", "Daily Vehicles", "", 2500.00)
        self.manager.update_record(0, updated_record)

        self.assertEqual(float(self.manager.records[0].OriginalValue), 2500.00)

    def test_update_invalid_record_type(self):
        """
        Test updating a record with an invalid type.
        """
        with self.assertRaises(TypeError):
            self.manager.update_record(0, ["Invalid", "Record"])

    def test_update_record_out_of_bounds(self):
        """
        Test updating a record at an invalid index.
        """
        updated_record = TrafficDataRecord("4805026", "Drumheller", "2023", "Daily Vehicles", "", 3000.00)
        with self.assertRaises(ValueError):
            self.manager.update_record(10, updated_record)

    def test_delete_record_valid(self):
        """
        Test deleting a record successfully.
        """
        self.manager.delete_record(0)
        self.assertEqual(len(self.manager.records), 1)

    def test_delete_record_out_of_bounds(self):
        """
        Test deleting a record at an invalid index.
        """
        with self.assertRaises(IndexError):
            self.manager.delete_record(10)

    def test_delete_record_invalid_index(self):
        """
        Test deleting a record with an invalid index type.
        """
        with self.assertRaises(TypeError):
            self.manager.delete_record("one")

if __name__ == '__main__':
    unittest.main()
