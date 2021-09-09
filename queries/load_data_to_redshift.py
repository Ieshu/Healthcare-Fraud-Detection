import configparser
config = configparser.ConfigParser()
config.read('dwh.cfg')

class LoadTableQuaries:
    """ This class is used to load data from S3 to Redshift cluster"""
        
    test_beneficiary_data = ("""
    COPY beneficiary_data FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF region 'us-west-2'
    FORMAT AS CSV
    TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL maxerror 100;
    """).format(config.get("S3","test_beneficiary_data"), config.get("IAM_ROLE","ARN"))
    
    
    test_inpatient_data = ("""
    COPY inpatient_data FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF region 'us-west-2'
    FORMAT AS CSV
    TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL maxerror 100;
    """).format(config.get("S3","test_inpatient_data"), config.get("IAM_ROLE","ARN"))

    test_outpatient_data = ("""
    COPY outpatient_data FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF region 'us-west-2'
    FORMAT AS CSV
    TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL maxerror 100;
    """).format(config.get("S3","test_outpatient_data"), config.get("IAM_ROLE","ARN"))
    
    test_1542969243754 = ("""
    COPY fraudulent_provider FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF region 'us-west-2'
    FORMAT AS CSV
    TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL maxerror 100;
    """).format(config.get("S3","test_1542969243754"), config.get("IAM_ROLE","ARN"))
    

    train_beneficiary_data = ("""
    COPY train_beneficiary_data FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF region 'us-west-2'
    FORMAT AS CSV
    TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL maxerror 100;
    """).format(config.get("S3","train_beneficiary_data"), config.get("IAM_ROLE","ARN"))
    
    
    train_inpatient_data = ("""
    COPY train_inpatient_data FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF region 'us-west-2'
    FORMAT AS CSV
    TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL maxerror 100;
    """).format(config.get("S3","train_inpatient_data"), config.get("IAM_ROLE","ARN"))

    train_outpatient_data = ("""
    COPY train_outpatient_data FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF region 'us-west-2'
    FORMAT AS CSV
    TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL maxerror 100;
    """).format(config.get("S3","train_outpatient_data"), config.get("IAM_ROLE","ARN"))
    
    train_1542865627584 = ("""
    COPY train_fraudulent_provider FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF region 'us-west-2'
    FORMAT AS CSV
    TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL maxerror 100;
    """).format(config.get("S3","train_1542865627584"), config.get("IAM_ROLE","ARN"))
    
        
    query_list_train = [train_1542865627584, train_beneficiary_data, train_inpatient_data, train_outpatient_data]
    
    query_list_test = [test_1542969243754, test_beneficiary_data, test_inpatient_data, test_outpatient_data]
