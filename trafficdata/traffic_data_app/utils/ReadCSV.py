from .DTO import DTO
import csv
import os
from datetime import datetime

# fileName = "D:/Git/PythonLearning/PythonLearning/trafficdata/traffic_data_app/data/Traffic_Volumes_-_Provincial_Highway_System.csv"
fileName = ""


def readCSV(fileName):
    """
    Reads a CSV file and returns a list of DTO objects.
    Args:
        fileName (str): The path to the CSV file.
    Returns:
        list: A list of DTO objects.
    """
    dtos = []
    id = 1  # Initialize id variable

    print(os.getcwd())
    try:
        with open(fileName) as data:
            reader = list(csv.reader(data)) #Using list to convert the reader object to a list
        for row in reader[2:100]: #Loads the first 100 rows ommiting the header
            dto = DTO()
            dto.set_id(id)  # Set the id of the DTO object
            dto.set_sectionID(row[0])
            dto.set_highway(row[1])
            dto.set_section(row[2])
            dto.set_sectionLength(row[3])
            dto.set_sectionDescription(row[4])
            # Function to format the date
            date_str = row[5]
            date_obj = datetime.strptime(date_str, '%m/%d/%Y')  # Convert string to datetime object
            formatted_date = date_obj.strftime('%Y-%m-%d')  # Format datetime object to string in 'YYYY-MM-DD' format
            dto.set_date(formatted_date)
            # dto.set_date(row[5])
            dto.set_description(row[6])
            dto.set_group(row[7])
            dto.set_type(row[8])
            dto.set_county(row[9])
            dto.set_ptrucks(row[10])
            adt_value = float(row[11]) if row[11] else 0.0
            dto.set_adt(adt_value)
            dto.set_direction(row[13])
            dtos.append(dto)
            id += 1  # Increment the id variable

        return dtos
    except FileNotFoundError:
        print(f"File {fileName} not found.")
        return []
print ("Program made by Andres Porras")