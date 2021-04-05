from pymongo import MongoClient
import ssl

def get_db(db_config):
    """
    Return MongoDB db instance. 
    The <db_config> parameter passed in to this function is the dict object defined in app_config.yml for each MongoDB environment, i.e sandpit, prod etc
    The invoker of this function needs to extract the value by app_config[<env_name>] and call this function to establish connection.
    """
    hosts=[]
    db_uri=''

    for host in db_config['hosts']:
        hosts.append( host['host'] + ":" + str(host['port'] ))

    db_uri = "mongodb://"   + \
            ','.join(hosts) + \
            "/?authSource=" + db_config['auth_source'] + \
            "&replicaSet="  + db_config['replica_set']


    db = MongoClient(
        db_uri,
        username = db_config['username'],
        password = db_config['password'],
        authMechanism = db_config['auth_mechanism'],
        ssl = (True if db_config['use_ssl'] else False),
        ssl_certfile = (db_config['ssl_certificate_file'] if db_config['ssl_certificate_file'] else None),
        ssl_ca_certs = (db_config['ssl_ca_file'] if db_config['ssl_ca_file'] else None),
        ssl_cert_reqs = (ssl.CERT_OPTIONAL if db_config['use_ssl'] else None),
        maxPoolSize = 5,
        wtimeout = 2500
        )[db_config['db_name']]
    
    return db
