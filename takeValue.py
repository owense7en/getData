import pandas as pd

def take_info(info, time, regionType, regionNumber, measure_unique_col):

    list = []
    for measure in measure_unique_col:
        number = regionNumber.loc[regionNumber['MEASURE'] == measure]
        num_data = number.loc[regionNumber['TIME'] == time]
        num_data = num_data.loc[regionNumber['REGIONTYPE'] == 'SA2'][['ASGS_2016', 'Value']]
        num_data = num_data.rename(columns={'Value':measure})
        #num_data = num_data.loc[~num_data.index.duplicated(keep='ASGS_2016')]
        list.append(num_data)

    dfs = [df.set_index(['ASGS_2016']) for df in list]
    data2 = pd.concat(dfs, axis=1).reset_index()

    print(data2)
    data2.to_csv('data/'+str(info)+'/dataFor' + '_' + str(info) + '_' + str(time) + '_' + str(regionType) +'.csv')

def get_info(csv ,data_info, data_region_type, measure_unique_col):

    regionNumber = pd.read_csv(csv,header = 0,sep=',')
    regionNumber = regionNumber.drop(['Flag Codes', 'Flags'], axis=1)
    year = regionNumber.loc[regionNumber['REGIONTYPE'] == data_region_type]['TIME'].unique()
    #id_info = regionNumber['Data item'].unique()
    #print(id_info)

    for num in year:
        take_info(data_info, num, data_region_type, regionNumber, measure_unique_col)


csv = "dataInput/ABS_REGIONAL_ASGS2016_Health, Disability, Family and Community.csv"
data_info = 'family_community'
data_region_type = 'SA2'
measure_unique_col = ['FAMILY_9','HHTYPE_6','RENT_2','RENT_3',
                      'HOUSE_2','HOUSE_3','HOUSE_4','DWELL_3',
                      'DWELL_4','TENURE_2','TENURE_3','TENURE_4',
                      'MARRIAGE_2','MARRIAGE_4','MARRIAGE_6']

get_info(csv ,data_info, data_region_type, measure_unique_col)
