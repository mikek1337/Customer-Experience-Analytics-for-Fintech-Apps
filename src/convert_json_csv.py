import csv
import os
import sys
class ConvertJSONToCsv:
    def __init__(self):
        pass

    def to_csv(self, json:list, filename:str):
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



