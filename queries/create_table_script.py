class CreateTableQuaries:
    """This class is used to create the table structures.
    
    """
    create_test_beneficiary_data = """ CREATE TABLE beneficiary_data (
                                                        BeneID VARCHAR(50) PRIMARY KEY, 
                                                        DOB VARCHAR(50), 
                                                        DOD VARCHAR(50), 
                                                        Gender float8, 
                                                        Race float8, 
                                                        RenalDiseaseIndicator VARCHAR(50), 
                                                        State float8, 
                                                        County float8, 
                                                        NoOfMonths_PartACov float8, 
                                                        NoOfMonths_PartBCov float8, 
                                                        ChronicCond_Alzheimer float8, 
                                                        ChronicCond_Heartfailure float8, 
                                                        ChronicCond_KidneyDisease float8, 
                                                        ChronicCond_Cancer float8, 
                                                        ChronicCond_ObstrPulmonary float8, 
                                                        ChronicCond_Depression float8, 
                                                        ChronicCond_Diabetes float8, 
                                                        ChronicCond_IschemicHeart float8, 
                                                        ChronicCond_Osteoporasis float8, 
                                                        ChronicCond_rheumatoidarthritis float8,
                                                        ChronicCond_stroke float8, 
                                                        IPAnnualReimbursementAmt float8, 
                                                        IPAnnualDeductibleAmt float8, 
                                                        OPAnnualReimbursementAmt float8, 
                                                        OPAnnualDeductibleAmt float8
                                                        )"""
    
    
    create_test_inpatient_data = """ CREATE TABLE inpatient_data (
                                                        BeneID VARCHAR(50), 
                                                        ClaimID VARCHAR(50), 
                                                        ClaimStartDt VARCHAR(50), 
                                                        ClaimEndDt VARCHAR(50), 
                                                        Provider VARCHAR(50), 
                                                        InscClaimAmtReimbursed int8,
                                                        AttendingPhysician VARCHAR(50), 
                                                        OperatingPhysician VARCHAR(50), 
                                                        OtherPhysician VARCHAR(50), 
                                                        AdmissionDt VARCHAR(50), 
                                                        ClmAdmitDiagnosisCode VARCHAR(50), 
                                                        DeductibleAmtPaid float8, 
                                                        DischargeDt VARCHAR(50), 
                                                        DiagnosisGroupCode VARCHAR(50), 
                                                        ClmDiagnosisCode_1 VARCHAR(50), 
                                                        ClmDiagnosisCode_2 VARCHAR(50), 
                                                        ClmDiagnosisCode_3 VARCHAR(50), 
                                                        ClmDiagnosisCode_4 VARCHAR(50), 
                                                        ClmDiagnosisCode_5 VARCHAR(50), 
                                                        ClmDiagnosisCode_6 VARCHAR(50), 
                                                        ClmDiagnosisCode_7 VARCHAR(50), 
                                                        ClmDiagnosisCode_8 VARCHAR(50), 
                                                        ClmDiagnosisCode_9 VARCHAR(50), 
                                                        ClmDiagnosisCode_10 VARCHAR(50), 
                                                        ClmProcedureCode_1 float8, 
                                                        ClmProcedureCode_2 float8, 
                                                        ClmProcedureCode_3 float8, 
                                                        ClmProcedureCode_4 float8, 
                                                        ClmProcedureCode_5 float8, 
                                                        ClmProcedureCode_6 float8,
                                                        PRIMARY KEY (BeneID, ClaimID),
                                                        FOREIGN KEY (BeneID) REFERENCES beneficiary_data(BeneID),
                                                        FOREIGN KEY (Provider) REFERENCES fraudulent_provider(Provider)
                                                        )"""
    
    create_test_outpatient_data = """ CREATE TABLE outpatient_data (
                                                        BeneID VARCHAR(50), 
                                                        ClaimID VARCHAR(50), 
                                                        ClaimStartDt VARCHAR(50), 
                                                        ClaimEndDt VARCHAR(50), 
                                                        Provider VARCHAR(50), 
                                                        InscClaimAmtReimbursed int8,
                                                        AttendingPhysician VARCHAR(50), 
                                                        OperatingPhysician VARCHAR(50), 
                                                        OtherPhysician VARCHAR(50), 
                                                        ClmDiagnosisCode_1 VARCHAR(50), 
                                                        ClmDiagnosisCode_2 VARCHAR(50), 
                                                        ClmDiagnosisCode_3 VARCHAR(50), 
                                                        ClmDiagnosisCode_4 VARCHAR(50), 
                                                        ClmDiagnosisCode_5 VARCHAR(50), 
                                                        ClmDiagnosisCode_6 VARCHAR(50), 
                                                        ClmDiagnosisCode_7 VARCHAR(50), 
                                                        ClmDiagnosisCode_8 VARCHAR(50), 
                                                        ClmDiagnosisCode_9 VARCHAR(50), 
                                                        ClmDiagnosisCode_10 VARCHAR(50), 
                                                        ClmProcedureCode_1 float8, 
                                                        ClmProcedureCode_2 float8, 
                                                        ClmProcedureCode_3 float8, 
                                                        ClmProcedureCode_4 float8, 
                                                        ClmProcedureCode_5 float8, 
                                                        ClmProcedureCode_6 float8, 
                                                        DeductibleAmtPaid float8, 
                                                        ClmAdmitDiagnosisCode VARCHAR(50),
                                                        PRIMARY KEY (BeneID, ClaimID),
                                                        FOREIGN KEY (BeneID) REFERENCES beneficiary_data(BeneID),
                                                        FOREIGN KEY (Provider) REFERENCES fraudulent_provider(Provider)
                                                        )"""
    
    create_test_1542969243754 = """ CREATE TABLE fraudulent_provider (
                                                    Provider VARCHAR(50) PRIMARY KEY,
                                                    PotentialFraud VARCHAR(10)
                                                    )"""
    
    
    #################################################################################
    
    create_train_beneficiary_data = """ CREATE TABLE train_beneficiary_data (
                                                        BeneID VARCHAR(50) PRIMARY KEY, 
                                                        DOB VARCHAR(50), 
                                                        DOD VARCHAR(50), 
                                                        Gender float8, 
                                                        Race float8, 
                                                        RenalDiseaseIndicator VARCHAR(50), 
                                                        State float8, 
                                                        County float8, 
                                                        NoOfMonths_PartACov float8, 
                                                        NoOfMonths_PartBCov float8, 
                                                        ChronicCond_Alzheimer float8, 
                                                        ChronicCond_Heartfailure float8, 
                                                        ChronicCond_KidneyDisease float8, 
                                                        ChronicCond_Cancer float8, 
                                                        ChronicCond_ObstrPulmonary float8, 
                                                        ChronicCond_Depression float8, 
                                                        ChronicCond_Diabetes float8, 
                                                        ChronicCond_IschemicHeart float8, 
                                                        ChronicCond_Osteoporasis float8, 
                                                        ChronicCond_rheumatoidarthritis float8,
                                                        ChronicCond_stroke float8, 
                                                        IPAnnualReimbursementAmt float8, 
                                                        IPAnnualDeductibleAmt float8, 
                                                        OPAnnualReimbursementAmt float8, 
                                                        OPAnnualDeductibleAmt float8
                                                        )"""
    
    
    create_train_inpatient_data = """ CREATE TABLE train_inpatient_data (
                                                        BeneID VARCHAR(50), 
                                                        ClaimID VARCHAR(50), 
                                                        ClaimStartDt VARCHAR(50), 
                                                        ClaimEndDt VARCHAR(50), 
                                                        Provider VARCHAR(50), 
                                                        InscClaimAmtReimbursed int8,
                                                        AttendingPhysician VARCHAR(50), 
                                                        OperatingPhysician VARCHAR(50), 
                                                        OtherPhysician VARCHAR(50), 
                                                        AdmissionDt VARCHAR(50), 
                                                        ClmAdmitDiagnosisCode VARCHAR(50), 
                                                        DeductibleAmtPaid float8, 
                                                        DischargeDt VARCHAR(50), 
                                                        DiagnosisGroupCode VARCHAR(50), 
                                                        ClmDiagnosisCode_1 VARCHAR(50), 
                                                        ClmDiagnosisCode_2 VARCHAR(50), 
                                                        ClmDiagnosisCode_3 VARCHAR(50), 
                                                        ClmDiagnosisCode_4 VARCHAR(50), 
                                                        ClmDiagnosisCode_5 VARCHAR(50), 
                                                        ClmDiagnosisCode_6 VARCHAR(50), 
                                                        ClmDiagnosisCode_7 VARCHAR(50), 
                                                        ClmDiagnosisCode_8 VARCHAR(50), 
                                                        ClmDiagnosisCode_9 VARCHAR(50), 
                                                        ClmDiagnosisCode_10 VARCHAR(50), 
                                                        ClmProcedureCode_1 float8, 
                                                        ClmProcedureCode_2 float8, 
                                                        ClmProcedureCode_3 float8, 
                                                        ClmProcedureCode_4 float8, 
                                                        ClmProcedureCode_5 float8, 
                                                        ClmProcedureCode_6 float8,
                                                        PRIMARY KEY (BeneID, ClaimID),
                                                        FOREIGN KEY (BeneID) REFERENCES train_beneficiary_data(BeneID),
                                                        FOREIGN KEY (Provider) REFERENCES train_fraudulent_provider(Provider)
                                                        )"""
    
    create_train_outpatient_data = """ CREATE TABLE train_outpatient_data (
                                                        BeneID VARCHAR(50), 
                                                        ClaimID VARCHAR(50), 
                                                        ClaimStartDt VARCHAR(50), 
                                                        ClaimEndDt VARCHAR(50), 
                                                        Provider VARCHAR(50), 
                                                        InscClaimAmtReimbursed int8,
                                                        AttendingPhysician VARCHAR(50), 
                                                        OperatingPhysician VARCHAR(50), 
                                                        OtherPhysician VARCHAR(50), 
                                                        ClmDiagnosisCode_1 VARCHAR(50), 
                                                        ClmDiagnosisCode_2 VARCHAR(50), 
                                                        ClmDiagnosisCode_3 VARCHAR(50), 
                                                        ClmDiagnosisCode_4 VARCHAR(50), 
                                                        ClmDiagnosisCode_5 VARCHAR(50), 
                                                        ClmDiagnosisCode_6 VARCHAR(50), 
                                                        ClmDiagnosisCode_7 VARCHAR(50), 
                                                        ClmDiagnosisCode_8 VARCHAR(50), 
                                                        ClmDiagnosisCode_9 VARCHAR(50), 
                                                        ClmDiagnosisCode_10 VARCHAR(50), 
                                                        ClmProcedureCode_1 float8, 
                                                        ClmProcedureCode_2 float8, 
                                                        ClmProcedureCode_3 float8, 
                                                        ClmProcedureCode_4 float8, 
                                                        ClmProcedureCode_5 float8, 
                                                        ClmProcedureCode_6 float8, 
                                                        DeductibleAmtPaid float8, 
                                                        ClmAdmitDiagnosisCode VARCHAR(50),
                                                        PRIMARY KEY (BeneID, ClaimID),
                                                        FOREIGN KEY (BeneID) REFERENCES train_beneficiary_data(BeneID),
                                                        FOREIGN KEY (Provider) REFERENCES train_fraudulent_provider(Provider)
                                                        )"""
    
    create_train_1542865627584 = """ CREATE TABLE train_fraudulent_provider (
                                                    Provider VARCHAR(50) PRIMARY KEY,
                                                    PotentialFraud VARCHAR(10)
                                                    )"""
 


    query_list_test = [create_test_beneficiary_data, create_test_1542969243754, create_test_inpatient_data, create_test_outpatient_data]
    
    query_list_train = [create_train_beneficiary_data, create_train_1542865627584, create_train_inpatient_data, create_train_outpatient_data, ]


