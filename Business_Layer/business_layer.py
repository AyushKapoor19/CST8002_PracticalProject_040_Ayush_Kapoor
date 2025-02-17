from Persistence_Layer.persistence_layer import load_csv, save_csv
from Model_Layer.TrafficDataRecord import TrafficDataRecord

class TrafficDataManager:
    """
    Author: Ayush Kapoor
    A class to manage traffic data records from a CSV file.

    Attributes:
    ----------
    file_path : str
        The path to the CSV file.
    records : list
        A list of traffic data records (each record is a dictionary).
    """

    def __init__(self, file_path):
        """
        Author: Ayush Kapoor
        Initializes TrafficDataManager with a file path and loads data.

        Parameters:
        ----------
        file_path : str
            The path to the CSV file.
        """
        self.file_path = file_path
        self.records = load_csv(file_path)

    def reload_data(self):
        """Reloads data from the CSV file into the records list."""
        self.records = load_csv(self.file_path)

    def save_data(self):
        """Saves the current records to the CSV file."""
        
        records_to_save = []
        for record in self.records:
            if isinstance(record, TrafficDataRecord):
                records_to_save.append(record)
            elif isinstance(record, dict):
                record_obj = TrafficDataRecord(
                    record["CSDUID"],
                    record["CSD"],
                    record["Period"],
                    record["IndicatorSummaryDescription"],
                    record["UnitOfMeasure"],
                    record["OriginalValue"]
                )
                records_to_save.append(record_obj)
            else:
                raise TypeError("Record must be either a TrafficDataRecord or a dictionary.")

        save_csv(records_to_save)



    def get_records(self):
        """
        Returns all traffic data records.

        Returns:
        -------
        list
            A list of all traffic data records.
        """
        return self.records

    def get_record(self, index):
        """
        Returns a specific traffic data record by index.

        Parameters:
        ----------
        index : int
            The index of the record.

        Returns:
        -------
        dict or None
            The traffic data record if index is valid, otherwise None.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if 0 <= index < len(self.records):
            return self.records[index]
        raise IndexError("Index out of range.")

    def add_record(self, record):
        """
        Adds a new traffic data record to the list.

        Parameters:
        ----------
        record : dict or TrafficDataRecord
            The traffic data record to be added.

        Raises:
        ------
        TypeError
            If the record is not a dictionary or a TrafficDataRecord instance.
        """
        if isinstance(record, TrafficDataRecord):
            record = {
                "CSDUID": record.CSDUID,
                "CSD": record.CSD,
                "Period": record.Period,
                "IndicatorSummaryDescription": record.IndicatorSummaryDescription,
                "UnitOfMeasure": record.UnitOfMeasure,
                "OriginalValue": record.OriginalValue
            }
        elif not isinstance(record, dict):
            raise TypeError("Record must be a dictionary or a TrafficDataRecord instance.")
        
        self.records.append(record)

    def update_record(self, index, updated_record):
        """
        Updates an existing traffic data record at a given index.

        Parameters:
        ----------
        index : int
            The index of the record to be updated.
        updated_record : TrafficDataRecord or dict
            The updated traffic data record (can be a TrafficDataRecord or a dictionary).
        """
        if 0 <= index < len(self.records):
            if isinstance(updated_record, dict):
                updated_record = TrafficDataRecord(
                updated_record.get("CSDUID", ""),
                updated_record.get("CSD", ""),
                updated_record.get("Period", ""),
                updated_record.get("IndicatorSummaryDescription", ""),
                updated_record.get("UnitOfMeasure", ""),
                updated_record.get("OriginalValue", "")
            )
            
            if not isinstance(updated_record, TrafficDataRecord):
                raise TypeError("Updated record must be a TrafficDataRecord or a dictionary.")

            self.records[index] = updated_record
        else:
            raise ValueError("Index out of bounds.")


    def delete_record(self, index):
        """
        Deletes a traffic data record by index.

        Parameters:
        ----------
        index : int
            The index of the record to be deleted.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if 0 <= index < len(self.records):
            del self.records[index]
        else:
            raise IndexError("Index out of range.")
