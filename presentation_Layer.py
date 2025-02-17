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
            manager.save_data()
            print("Data saved.")
        elif choice == '3':
            display_records(manager.get_records())
        elif choice == '4':
            index = int(input("Enter the index of the record: "))
            record = manager.get_record(index - 2)
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

            new_record = TrafficDataRecord(
                CSDUID=csduid,
                CSD=csd,
                Period=period,
                IndicatorSummaryDescription=indicator_summary,
                UnitOfMeasure=unit_of_measure,
                OriginalValue=original_value
            )
            manager.add_record(new_record)
            print("Record added.")
        elif choice == '6':
            index = int(input("Enter the index of the record to update: "))
            record = manager.get_record(index)
            if record:
                if isinstance(record, dict):
                    record = TrafficDataRecord(
                        record.get("CSDUID", ""),
                        record.get("CSD", ""),
                        record.get("Period", ""),
                        record.get("IndicatorSummaryDescription", ""),
                        record.get("UnitOfMeasure", ""),
                        record.get("OriginalValue", "")
                    )
                record.CSDUID = input(f"Enter new CSDUID (current: {record.CSDUID}): ") or record.CSDUID
                record.CSD = input(f"Enter new CSD (current: {record.CSD}): ") or record.CSD
                record.Period = input(f"Enter new Period (current: {record.Period}): ") or record.Period
                record.IndicatorSummaryDescription = input(f"Enter new Indicator Summary (current: {record.IndicatorSummaryDescription}): ") or record.IndicatorSummaryDescription
                record.UnitOfMeasure = input(f"Enter new Unit of Measure (current: {record.UnitOfMeasure}): ") or record.UnitOfMeasure
                record.OriginalValue = input(f"Enter new Original Value (current: {record.OriginalValue}): ") or record.OriginalValue
                manager.update_record(index, record)
                print("Record updated.")
            else:
                print("Record not found.")
        elif choice == '7':
            index = int(input("Enter the index of the record to delete: "))
            manager.delete_record(index - 2)
            print("Record deleted.")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
