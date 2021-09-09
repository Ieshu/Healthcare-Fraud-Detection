import configparser
config = configparser.ConfigParser()
config.read('dwh.cfg')

class LoadTableQuaries:
    """ This class is used to load data from S3 to PostgreSQL"""
        
    test_beneficiary_data = ("""
    COPY beneficiary_data FROM {}
    CSV HEADER;
    """).format(config.get("LOCAL","test_beneficiary_data"))    
    
    test_inpatient_data = ("""
    COPY inpatient_data FROM {}
    CSV HEADER;
    """).format(config.get("LOCAL","test_inpatient_data"))

    test_outpatient_data = ("""
    COPY outpatient_data FROM {}
    CSV HEADER;
    """).format(config.get("LOCAL","test_outpatient_data"))
    
    test_1542969243754 = ("""
    COPY fraudulent_provider(provider) FROM {}
    CSV HEADER;
    """).format(config.get("LOCAL","test_1542969243754"))    

    train_beneficiary_data = ("""
    copy train_beneficiary_data FROM {}
    CSV HEADER;
    """).format(config.get("LOCAL","train_beneficiary_data"))    
    
    train_inpatient_data = ("""
    copy train_inpatient_data FROM {}
    CSV HEADER;
    """).format(config.get("LOCAL","train_inpatient_data"))

    train_outpatient_data = ("""
    COPY train_outpatient_data FROM {}
    CSV HEADER;
    """).format(config.get("LOCAL","train_outpatient_data"))
    
    train_1542865627584 = ("""
    COPY train_fraudulent_provider FROM {}
    CSV HEADER;
    """).format(config.get("LOCAL","train_1542865627584"))
    
    
    query_list_train = [train_1542865627584, train_beneficiary_data, train_inpatient_data, train_outpatient_data]
    
    query_list_test = [test_1542969243754, test_beneficiary_data, test_inpatient_data, test_outpatient_data]
