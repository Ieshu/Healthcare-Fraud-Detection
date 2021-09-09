import psycopg2
import configparser
config = configparser.ConfigParser()
config.read('dwh.cfg')

class DataValidator:
    """This class validates the database tables"""
    
    def __init__(self):
        """This init method initializes the class"""
        

        
    def create_connection(self):
        """ This methods establishes connection with the database"""
        
        #Connect to redshift cluster
        #self.conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
        #self.cur =  self.conn.cursor()
        #print('Connected to Redshift cluster')      
        
        # connect to default database
        #self.conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=student")
        #self.conn.set_session(autocommit=True)
        #self.cur = self.conn.cursor()
    
        # create sparkify database with UTF8 encoding
        #self.cur.execute("DROP DATABASE IF EXISTS sparkifydb")
        #self.cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

        # close connection to default database
        #self.conn.close()    
    
        # connect to sparkify database
        self.conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=postgres password=student")
        self.cur = self.conn.cursor()
        
        print('Connected to Local PostgreSQL')
        

    def check_beneficiary_id(self):
        """ This methods checks beneficiary id"""
        
        self.create_connection()
        print('Checking inpatient data')
        sql_str = 'select count(*) from inpatient_data where beneid is null'
        self.cur.execute(sql_str)
        result = self.cur.fetchone()
        if result[0]==0:
            print('Inpatient data successfully verified')
        else:
            raise ValueError('Beneficiary Id missing in some inpatient information')
            
            
        print('Checking outpatient data')
        sql_str = 'select count(*) from outpatient_data where beneid is null'
        self.cur.execute(sql_str)
        result = self.cur.fetchone()
        if result[0]==0:
            print('Outpatient data successfully verified')
        else:
            raise ValueError('Beneficiary Id missing in some outpatient information')
        self.conn.close()
        
          

    def check_provider_id(self):
        """ This methods checks provider id"""
        
        self.create_connection()
        print('Checking inpatient data')
        sql_str = 'select count(*) from inpatient_data where provider is null'
        self.cur.execute(sql_str)
        result = self.cur.fetchone()
        if result[0]==0:
            print('Inpatient data successfully verified')
        else:
            raise ValueError('Provider Id missing in some inpatient information')
            
            
        print('Checking outpatient data')
        sql_str = 'select count(*) from outpatient_data where provider is null'
        self.cur.execute(sql_str)
        result = self.cur.fetchone()
        if result[0]==0:
            print('Outpatient data successfully verified')
        else:
            raise ValueError('Provider Id missing in some outpatient information')
        self.conn.close()
        


