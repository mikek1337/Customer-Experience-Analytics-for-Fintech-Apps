import csv
import os
import sys
class ConvertJSONToCsv:
    """
    A class to convert a list of JSON objects (Python dictionaries) to a CSV file.

    Methods
    -------
    to_csv(json: list, filename: str)
        Converts the provided list of dictionaries to a CSV file and saves it to the '../data/' directory with the given filename.

    Parameters
    ----------
    json : list
        A list of dictionaries, where each dictionary represents a row in the CSV file.
    filename : str
        The name of the CSV file to be created (should include the '.csv' extension).

    Notes
    -----
    - The CSV file will be saved in the parent directory's 'data' folder relative to the script location.
    - The header row is automatically generated from the keys of the first dictionary in the list.
    """
    def __init__(self):
        pass

    def to_csv(self, json:list, filename:str):
        """
        Converts a list of dictionaries (JSON-like objects) to a CSV file.

        Args:
            json (list): A list of dictionaries, where each dictionary represents a row of data.
            filename (str): The name of the CSV file to write to (saved in the '../data/' directory).

        Notes:
            - The CSV file will use the keys of the first dictionary in the list as the header row.
            - Each subsequent dictionary's values will be written as a row in the CSV file.
            - Existing files with the same name will be overwritten.
        """
        path = f'{os.pardir}/data/{filename}'
        f = open(path, 'w', newline='')
        cw = csv.writer(f)
        row = 0
        for data in json:
            if row == 0:
                header = data.keys()
                cw.writerow(header)
                row+=1
            cw.writerow(data.values())
        f.close()



