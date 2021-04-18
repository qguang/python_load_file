##!/usr/bin/env python3

from app_config import APP_BASEDIR, APP_CONFIG
import database
import pandas as pd
import json
import os
from datetime import datetime

import pprint


# to be replaced by input parameter
ENV_NAME='sandpit'
incoming_dir=os.path.join(APP_BASEDIR, 'incoming')
incoming_files={
    'customer': os.path.join(incoming_dir,'customer.csv')
}


mongo_db=database.get_db(APP_CONFIG[ENV_NAME]['db_config'])
customer_collection = mongo_db['customer']

# load CSV
df_customer = pd.read_csv(incoming_files['customer'], sep=',', header =0)
df_customer.rename(columns=lambda x: x.lower(), inplace=True)
df_customer['dob'] = df_customer['dob'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))

# transform
temp_json_result=df_customer.to_json(orient='records')
parsed_json = json.loads(temp_json_result)

# insert into DB
mongodb_result=None
customer_collection.delete_many({})
mongodb_result=customer_collection.insert_many(parsed_json)

print(len(mongodb_result.inserted_ids))

#pprint.pprint(parsed_json)
