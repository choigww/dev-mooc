import pandas as pd

data=pd.read_csv('data/CRDC2013_14.csv')
data['tot_enrollment'] = data['TOT_ENR_M'] +\
                            data['TOT_ENR_F']

all_enrollment = data['tot_enrollment'].sum()
enrollment_colnames = ['SCH_ENR_HI_M','SCH_ENR_HI_F','SCH_ENR_AM_M', 'SCH_ENR_AM_F', 'SCH_ENR_AS_M', 'SCH_ENR_AS_F', 'SCH_ENR_HP_M','SCH_ENR_HP_F','SCH_ENR_BL_M','SCH_ENR_BL_F','SCH_ENR_WH_M','SCH_ENR_WH_F','SCH_ENR_TR_M','SCH_ENR_TR_F']

sub_enrollments = []
for colname in enrollment_colnames:
    print(colname, end=' : ')
    print(data[colname].sum() / all_enrollment)