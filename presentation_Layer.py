from Business_Layer.business_layer import TrafficDataManager
from Model_Layer.TrafficDataRecord import TrafficDataRecord

def display_records(records):
    """
    Author: Ayush Kapoor
    Displays a list of traffic data records.

    Parameters:
    ----------
    records : list
        A list of TrafficDataRecord objects to display.
    """
    for index, record in enumerate(records):
        print(f"Index: {index}, Record: {record}")

def display_menu():
    """
    Author: Ayush Kapoor
    Displays the main menu options to the user.
    """
    print("Name- Ayush Kapoor")
    print("1. Reload data")
    print("2. Save data")
    print("3. Display all records")
    print("4. Display a single record")
    print("5. Add a new record")
    print("6. Update a record")
    print("7. Delete a record")
    print("8. Exit")

def main():
    """
    The main function of the presentation layer that provides a loop to handle user inputs and interact with the TrafficDataManager.
    """
    manager = TrafficDataManager('dailyvehiclesdownload.csv')

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.reload_data()
            print("Data reloaded.")
        elif choice == '2':
            # No need to ask for a file path; save to the same directory
            manager.save_data()  # Use the save_data method without the file path argument
            print("Data saved.")
        elif choice == '3':
            display_records(manager.get_records())
        elif choice == '4':
            index = int(input("Enter the index of the record: "))
            record = manager.get_record(index)
            if record:
                print(record)
            else:
                print("Record not found.")
        elif choice == '5':
            csduid = input("Enter CSDUID: ")
            csd = input("Enter CSD: ")
            period = input("Enter Period: ")
            indicator_summary = input("Enter Indicator Summary Description: ")
            unit_of_measure = input("Enter Unit of Measure: ")
            original_value = input("Enter Original Value: ")

            # Ensure the correct capitalization for attribute names:
            new_record = TrafficDataRecord(
                CSDUID=csduid,  # Correct capitalization
                CSD=csd,  # Correct capitalization
                Period=period,  # Correct capitalization
                IndicatorSummaryDescription=indicator_summary,  # Correct capitalization
                UnitOfMeasure=unit_of_measure,  # Correct capitalization
                OriginalValue=original_value  # Correct capitalization
            )
            manager.add_record(new_record)
            print("Record added.")
        elif choice == '6':
            index = int(input("Enter the index of the record to update: "))
            record = manager.get_record(index)
            if record:
                # Make sure to update attributes with the correct names
                record.CSDUID = input(f"Enter new CSDUID (current: {record.CSDUID}): ") or record.CSDUID
                record.CSD = input(f"Enter new CSD (current: {record.CSD}): ") or record.CSD
                record.Period = input(f"Enter new Period (current: {record.Period}): ") or record.Period
                record.IndicatorSummaryDescription = input(f"Enter new Indicator Summary (current: {record.IndicatorSummaryDescription}): ") or record.IndicatorSummaryDescription
                record.UnitOfMeasure = input(f"Enter new Unit of Measure (current: {record.UnitOfMeasure}): ") or record.UnitOfMeasure
                record.OriginalValue = input(f"Enter new Original Value (current: {record.OriginalValue}): ") or record.OriginalValue
                print("Record updated.")
            else:
                print("Record not found.")
        elif choice == '7':
            index = int(input("Enter the index of the record to delete: "))
            manager.delete_record(index)
            print("Record deleted.")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
