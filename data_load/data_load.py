##!/usr/bin/env python3

from app_config import app_config
import database
import pandas as pd
import json

# to be replaced by input parameter
env_name = 'sandpit'
input_file=''
input_file_header=()
db=None
chunk_size = 5
idx=0
# We want all data initially loaded as str. the automatic data type detection can cause issue, i.e. remove leading zero
input_file_data_type = {'D': 'str' }

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



