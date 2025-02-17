import csv
import uuid
import os
from Model_Layer.TrafficDataRecord import TrafficDataRecord

def load_csv(file_path):
    """
    Author: Ayush Kapoor
    Loads traffic data records from a CSV file.

    Parameters:
    ----------
    file_path : str
        The path to the CSV file.

    Returns:
    -------
    list
        A list of TrafficDataRecord objects.
    """
    records = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                record = TrafficDataRecord(
                    CSDUID=row['CSDUID'].strip(),
                    CSD=row['CSD'].strip(),
                    Period=int(row['Period'].strip()),
                    IndicatorSummaryDescription=row['IndicatorSummaryDescription'].strip(),
                    UnitOfMeasure=row['UnitOfMeasure'].strip(),
                    OriginalValue=float(row['OriginalValue'].strip())
                )
                records.append(record)
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return records

def save_csv(records):
    """
    Author: Ayush Kapoor
    Saves traffic data records to a CSV file with a UUID in the filename.

    Parameters:
    ----------
    records : list
        A list of TrafficDataRecord objects to save.
    """
    try:
        unique_filename = f"traffic_data_{uuid.uuid4().hex}.csv"
        
        current_directory = os.getcwd()
        
        full_file_path = os.path.join(current_directory, unique_filename)

        with open(full_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['CSDUID', 'CSD', 'Period', 'IndicatorSummaryDescription', 'UnitOfMeasure', 'OriginalValue'])
            for record in records:
                writer.writerow([record.CSDUID, record.CSD, record.Period, record.IndicatorSummaryDescription,
                                 record.UnitOfMeasure, record.OriginalValue])

        print(f"Data saved to {full_file_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")