from pandas_profiling import ProfileReport
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import shap


data_df = pd.read_csv('11-21_Mounts_Bay.csv',header = 0,sep=',')

data_df = data_df.replace('-', np.nan, regex=True)
data_df = data_df.replace('/', np.nan, regex=True)
data_df = data_df.dropna(thresh=9)


list1 = ['Date', 'Daytime Average Temperature (degrees Celsius)','Daytime Average Humidity (%)',
         'Average Pressure (hPa)','Total Precipitation (mm)',
         'Average Windspeed (m/s)','Daytime Average Enthalpy','Daytime Average Moisture',
          'Occupancy', 'Daytime kWh - actual power consumption (kWh)',
         'Actual water consumption (kLiter)','Actual Gas consumption (MJ)']


scaler = StandardScaler()

data_df1 = pd.DataFrame(scaler.fit_transform(data_df),columns=list1)

profile = ProfileReport(data_df1, explorative=True)

shap.plots.waterfall(data_df)

profile.to_file('profile-family.html')


