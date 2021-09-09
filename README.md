# Healthcare-Fraud-Detection
# Healthcare Fraud Analysis

## Project Objective

This project aims to demonstrate the whole sprectrum of data ecosystem.
It digests data into a data warehouse using an automated etl pipeline. The data is a combination of patient's information, existing medical conditions, healthcare provider information, inpatient as well as outpatient claim records. After data ingestion, exploratory data analysis is carried out to clean the data and bring out vital statistics for visualization.
The data is then fed to machine learning models to predict whether a particular healthcare provider is fraud. 
A set of training data has been used to train the models.

## Dataset Description

The dataset has been fetched from kaggle's [healthcare fraud detection analysis dataset](https://www.kaggle.com/rohitrox/healthcare-provider-fraud-detection-analysis)

Provider Fraud is one of the biggest problems facing Medicare. According to the government, the total Medicare spending increased exponentially due to frauds in Medicare claims. Healthcare fraud is an organized crime which involves peers of providers, physicians, beneficiaries acting together to make fraud claims.

**Problem Statement:** The goal of this project is to " predict the potentially fraudulent providers " based on the claims filed by them. For the purpose of this project, we are considering Inpatient claims, Outpatient claims and Beneficiary details of each provider.

**A) Inpatient Data:**
This data provides insights about the claims filed for those patients who are admitted in the hospitals. It also provides additional details like their admission and discharge dates and admit d diagnosis code.

**B) Outpatient Data:**
This data provides details about the claims filed for those patients who visit hospitals and not admitted in it.

**C) Beneficiary Details Data:**
This data contains beneficiary KYC details like health conditions,regioregion they belong to etc.

## Data Model

The data model consists of four tables:

* beneficiary_data - Contains all the patient information
* inpatient_data - Contains information of inpatient attendence along with healthcare provider information
* outpatient_data - Contains information of outpatient attendence along with healthcare provider information
* fraudalent_provider - Used to classify a provider as fraud or not.

Following is a pictorial representation of the relational data model:
![ERD Diagram](/ERD.png)

## Project Execution steps

**1.** The dataset files are copied to a S3 bucket. As of now, this step has been performed manually, However, this can also be achieved using the kaggle api.

**2.** An AWS Redshift cluster is instanciated using boto3 library. Refer to [Redshift_Connection.ipynb](/Redshift_Connection.ipynb) file for steps. This notebook uses credentials from [dwh.cfg](/dwh.cfg) file

**3.** Data is loaded from S3 to Redshift by executing [etl_pipeline.ipynb](/etl_pipeline.ipynb) . This etl performs the following steps:

* Drop any existig tables using [drop_table_script.py](/queries/drop_table_script.py)
* Recreate the tables using [create_table_script.py](/queries/create_table_script.py)
* Load data into the tables using [load_data_to_redshift.py](queries/load_data_to_redshift.py )
* Validate the data  using [data_validator.py](/queries/data_validator.py) 

**4.** [Medicare_Provider_Fraud_Detection_Analysis.ipynb](/Medicare_Provider_Fraud_Detection_Analysis.ipynb) notebook contains all the steps for exploratory data analysis and application of machine learning models. Below is the brief overview of the steps:

* Data is loaded from Redshift.
* Data is cleaned and relevant dataframes are prepared.
* Inpatient, Outpatient, and beneficiary data are merged to prepare consolidsated patient data.
* Visualization is done using various plots and graphs.
* Machine Learning models are trained using training dataset.
* Model accuracy is analysed using the test dataset. The following algorithms have been used to compare accuracy:
	* Decision Tree
	* Naive Bayes
	* Random Forest
	* SVM
	* Gradient Boosting
	
## Technology

* S3 - File storage for csv file
* Redshift - Data Warehouse
* PostgreSQL - Data Warehouse(Local deployment)
* boto3 - AWS IAC
* matplotlib - Data Visualization
* scikit-learn - Machine learning models
	
