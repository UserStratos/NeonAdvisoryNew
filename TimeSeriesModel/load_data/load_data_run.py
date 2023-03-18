import warnings;
warnings.simplefilter("ignore")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from TimeSeriesModel.load_data.functions import opencsv, data_info, data_shape, data_description, data_columns, data_dtypes, data_missing_values, duplicated_data, data_head
from TimeSeriesModel.load_data.constants import file_name, data

opencsv(file_name)
data_info()
data_shape()
data_description()
data_columns()
data_dtypes()
data_missing_values()
duplicated_data()
data_head()
