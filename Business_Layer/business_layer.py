from Persistence_Layer.persistence_layer import load_csv, save_csv

class TrafficDataManager:
    """
    Author: Ayush Kapoor
    A class to manage traffic data records from a CSV file.

    Attributes:
    ----------
    file_path : str
        The path to the CSV file.
    records : list
        A list of traffic data records.
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
        """
        Reloads data from the CSV file into the records list.
        """
        self.records = load_csv(self.file_path)

    def save_data(self):
        """
        Saves the current records to a new CSV file.

        """
        save_csv(self.records)

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
        if 0 <= index < len(self.records):
            return self.records[index]
        else:
            return None

    def add_record(self, record):
        """
        Adds a new traffic data record to the list.

        Parameters:
        ----------
        record : dict
            The traffic data record to be added.
        """
        self.records.append(record)

    def update_record(self, index, updated_record):
        """
        Author: Ayush Kapoor
        Updates an existing traffic data record at a given index.

        Parameters:
        ----------
        index : int
            The index of the record to be updated.
        updated_record : dict
            The updated traffic data record.
        """
        if 0 <= index < len(self.records):
            self.records[index] = updated_record

    def delete_record(self, index):
        """
        Deletes a traffic data record by index.

        Parameters:
        ----------
        index : int
            The index of the record to be deleted.
        """
        if 0 <= index < len(self.records):
            self.records.pop(index)