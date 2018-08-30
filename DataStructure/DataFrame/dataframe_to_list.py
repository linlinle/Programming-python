import pandas as pd
import numpy as np

'''首先使用np.array()函数把DataFrame转化为np.ndarray()，再利用tolist()函数把np.ndarray()转为list'''

data_x = pd.read_csv("file_path",usecols=[2,3,4])#pd.dataframe
train_data = np.array(data_x)#np.ndarray()
train_x_list=train_data.tolist()#list


