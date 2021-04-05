##!/usr/bin/env python3

from app_config import app_config
import database
import pandas as pd
import json

# to be replaced by input parameter
env_name = 'sandpit'
input_file='/Users/qiugua/GIT_REPO/realpython_materials/python-contact-book/data_load/incoming/LIFPOLData20210220.dat'
input_file_header=()
db=None
chunk_size = 5
idx=0
# We want all data initially loaded as str. the automatic data type detection can cause issue, i.e. remove leading zero
input_file_data_type = {'D': 'str', 'ProductCode': 'str', 'ProductDescription': 'str', 'PolicyName': 'str', 'PolicyNumber': 'str', 'PolicyStatus': 'str', 'OpenDate': 'str', 'CancellationDate': 'str', 'PolicyStatusChange': 'str', 'LoanNumber': 'str', 'LoanType': 'str', 'OriginalLoanAmount': 'str', 'InsuredPercentage': 'str', 'ContinuationOnCancel': 'str', 'PaymentMethod': 'str', 'PaymentFrequency': 'str', 'NextPaymentDate': 'str', 'BilledToDate': 'str', 'NextPaymentAmount': 'str', 'AgentId': 'str', 'AgentType': 'str', 'LastUpdateDate': 'str', 'OSCI': 'str', 'OwnerName': 'str', 'OwnerRole': 'str', 'ActionStatus': 'str', 'BenefitId': 'str', 'BeneficiaryName': 'str', 'BenefitAmount': 'str', 'BenefitCode': 'str', 'BenefitText': 'str', 'BenefitLastUpdateDate                                                               ': 'str'}

df = pd.read_csv(input_file, sep='\s*\|\s*', engine='python', header =1)
df.head(10) # df.tail(10)

def get_input_file_header():
    '''
    read the very first line of incoming file to get file header (not csv header)
    '''
    df=pd.read_csv(input_file,sep='|', nrows=1,header=None)
    input_file_header=(df.iloc[0,0], df.iloc[0,1], df.iloc[0,2])

def validate_input_file_heaer(input_file_header):
    '''
    validate input file header for date time
    '''
    pass
    #print(input_file_header[0], input_file_header[1], input_file_header[2])

input_file_header = get_input_file_header()

#for df in pd.read_csv(input_file,sep='\s*\|\s*', engine='python',header =1, chunksize=chunk_size, dtype= input_file_data_type):
for df in pd.read_csv(input_file,sep='|',header =1, chunksize=chunk_size, dtype= input_file_data_type):
    idx += 1
    print(str(idx) + 'what------------')
    for dt_key, dt_value in input_file_data_type.items():
        if dt_value == 'str':
            df[dt_key] = df[dt_key].str.strip()

    for df_idx, df_row in df.iterrows():
        print(str(df_idx) + '|' + df_row['D'] + '|' + df_row['OSCI'] + '|' + df_row['ProductDescription'] + '|' + df_row['PolicyName'] + '|' + df_row['PolicyStatus'] + '|')
    
    break
    #print(df['D'] + ' ' + df['OSCI'] + ' ' + df['ProductDescription'])
    doc1 = {"test": "this is a good one"}
    doc2 = {"test": "this is also a good one"}
    if idx == 2:
        break





#if db == None:
#    db = database.get_db(app_config['db_config'][env_name])
#    print(db)
#
#print(db.list_collection_names())

#mongo_temp_dict = {
    #        '_id': id,
    #        'ProductCode': row['ProductCode'] , 'ProductDescription': row['ProductDescription'], 
    #        'PolicyNumber': row['PolicyNumber'], 'PolicyStatus': row['PolicyStatus'], 
    #        'OpenDate': datetime.strptime(row['OpenDate'], "%Y-%m-%d"), 
    #         'BenefitAmount': Decimal128(decimal.Decimal(row['BenefitAmount'])), 
    #        'LastUpdateDate': syd_timezone.localize(datetime.strptime(row['LastUpdateDate'], "%Y-%m-%dT%H:%M:%S"))
    #    }