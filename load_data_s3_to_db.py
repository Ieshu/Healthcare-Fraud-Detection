from queries.drop_table_script import DropTableQuaries
from queries.create_table_script import CreateTableQuaries
from queries.load_data_to_postgreSQL import LoadTableQuaries
#from queries.load_data_to_redshift import LoadTableQuaries

import psycopg2
import configparser
config = configparser.ConfigParser()
config.read('dwh.cfg')

class LoadDataFromS3ToDb:
    """This class perform all the tasks to load S3 data to database tables"""
    
    def __init__(self):
        """This init method initializes the class"""
        
    def drop_test_tables(self):
        """ This methods drops the existing tables"""
        
        for query in DropTableQuaries.query_list_test:
            self.cur.execute(query)
            self.conn.commit()
        return 'Successfully dropped test tables'
    
    def drop_train_tables(self):
        """ This methods drops the existing training tables"""
        
        for query in DropTableQuaries.query_list_train:
            self.cur.execute(query)
            self.conn.commit()
        return 'Successfully dropped train tables'

    def create_test_tables(self):
        """ This methods creates the tables if not present"""
        for query in CreateTableQuaries.query_list_test:
            self.cur.execute(query)
            self.conn.commit()
        return 'Successfully created test tables'
    
    def create_train_tables(self):
        """ This methods creates the training tables if not present"""
        for query in CreateTableQuaries.query_list_train:
            self.cur.execute(query)
            self.conn.commit()
        return 'Successfully created train tables'
       
    def load_test_tables(self):
        """ This methods loads data into the tables"""
        for query in LoadTableQuaries.query_list_test:
            self.cur.execute(query)           
            self.conn.commit()
        return 'Successfully loaded test tables'
    
    def load_train_tables(self):
        """ This methods loads data into the training tables"""
        for query in LoadTableQuaries.query_list_train:
            self.cur.execute(query)
            self.conn.commit()
        return 'Successfully loaded train tables'
    
    def execute_training_pipeline(self):
        """ This method executes the training data pipeline in order"""
        
        self.create_connection()        
        out = self.drop_train_tables()
        print(out)
        out = self.create_train_tables()
        print(out)
        out = self.load_train_tables()
        print(out)   
        self.conn.close()       
        print('Successfully completed all the etl tasks')
        
    
    def execute_data_pipeline(self):
        """ This method executes the data pipeline in order"""
        
        self.create_connection()        
        out = self.drop_test_tables()
        print(out)
        out = self.create_test_tables()
        print(out)
        out = self.load_test_tables()
        print(out)    
        self.conn.close()        
        print('Successfully completed all the etl tasks')
        
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
        
      


