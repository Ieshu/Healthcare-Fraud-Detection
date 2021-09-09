class DropTableQuaries:
    """ This class is used to drop existing tables"""
    
    drop_test_beneficiary_data = """ DROP TABLE IF EXISTS beneficiary_data"""    
    drop_test_inpatient_data = """ DROP TABLE IF EXISTS inpatient_data"""   
    drop_test_outpatient_data = """ DROP TABLE IF EXISTS outpatient_data"""   
    drop_test_1542969243754 = """ DROP TABLE IF EXISTS fraudulent_provider"""
    
    
    drop_train_beneficiary_data = """ DROP TABLE IF EXISTS train_beneficiary_data"""    
    drop_train_inpatient_data = """ DROP TABLE IF EXISTS train_inpatient_data"""    
    drop_train_outpatient_data = """ DROP TABLE IF EXISTS train_outpatient_data"""    
    drop_train_1542865627584 = """ DROP TABLE IF EXISTS train_fraudulent_provider"""    
    
    query_list_test = [drop_test_inpatient_data, drop_test_outpatient_data, drop_test_1542969243754, drop_test_beneficiary_data]
    
    query_list_train = [drop_train_inpatient_data, drop_train_outpatient_data, drop_train_1542865627584, drop_train_beneficiary_data]