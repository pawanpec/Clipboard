from os.path import join, dirname
#import pandas as pd
#import numpy as np
import csv
import re
from pymongo import MongoClient

"""

Use this file to read in the project nurse data, perform text pre-processing
and store data in mongo. The fields we're interested in storing are:

  'How many years of experience do you have?' -> experience,
  'What's your highest level of education?' -> education,
  'What is your hourly rate ($/hr)?' -> salary,
  'Department' -> department,
  'What (City, State) are you located in?' -> location,
  'What is the Nurse - Patient Ratio?' -> patientNurseRatio

Check server/models/Record.js for an example of the schema.

"""
header = {"How many years of experience do you have?":"experience",
"What's your highest level of education?":"education", "What is your hourly rate ($/hr)?":"salary",
 "Department":"department", "What (City, State) are you located in?":"location", "What is the Nurse - Patient Ratio?":"patientNurseRatio"}

def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['clipboardinterview']
    csvfile = open(join(dirname(__file__), '../data/projectnurse.csv'), 'r')
    reader = csv.DictReader( csvfile )
    for each in reader:
        row={}
        for field in header.keys():
            val = header[field]
            if val=='salary':
                if 'year' in each[field] or 'yr' in each[field] or 'annual' in each[field]:
                    res=re.findall('\d+', each[field])
                    yrVal=float(float(res[0])/2920);
                    if yrVal<=1:
                        yrVal=yrVal*1000
                    row['stdval']=yrVal
                elif 'month' in each[field]:
                    res=re.findall('\d+', each[field])
                    row['stdval']=float(float(res[0])/240)
                elif 'week' in each[field]:
                    if 'biweek' in each[field] or '2 weeks' in each[field]:
                        res=re.findall('\d+', each[field])
                        row['stdval']=float(float(res[0])/196)
                    else:
                        res=re.findall('\d+', each[field])
                        row['stdval']=float(float(res[0])/98)
                elif 'day' in each[field]:
                    res=re.findall('\d+', each[field])
                    row['stdval']=float(float(res[0])/8)
                else:
                    res=re.findall('\d+', each[field])
                    if not len(res)==0:
                        x=float(res[0])
                        if(x<=200):
                            row['stdval']=x
                        else:
                            row['others']=x
                    else:
                        row['others']=each[field]
            row[val]=each[field]
        db.records.insert(row)


if __name__ == "__main__":
    main()
