import numpy as np
import pandas as pd 

'''
extract_ts: a function that extracts timestamps of certain events
beh_df: a dataframe of the behavioral data
target
num: False when you want to extract non-number data
return a list of the timestamp that a image is related to the behavior
'''
def extract_ts(beh_df, col_name, num=True):
    onset_timing = []
    if num == True:
        for i in range(beh_df.shape[0]):
            if beh_df.trialCount[i]!= 0 :
                t = beh_df[col_name][i]
                onset_timing.append(int(round(t)) // 2+1)
    else:
        for i in range(beh_df.shape[0]):
            if beh_df.trialCount[i]!= 0 :
                onset_timing.append(beh_df[col_name][i])
    return onset_timing

'''
extract_data: a function that extracts (activation) value difference from certain timestamps in a block design
fdata: A 1-D array extracted from get_fdata, could be one cloumn of a higher-dimension array
reg_num: index of the region
ori/prb _ts: the list of the timestamp in the block design
return a list of the timestamp that a image is related to the behavior
'''
def extract_diff(fdata, org_ts, prb_ts, reg_num=0):
    o_act = []
    p_act = []
    diff = []
    for j in org_ts :
        o_act.append(fdata[j, reg_num])
    for j in prb_ts :
        p_act.append(fdata[j, reg_num])
    for k in range(len(o_act)):
        diff.append(p_act[k]-o_act[k])
    return diff

'''
CatNSave: categorize the activity to the stimului pair and save them as seperate .csv for further analysis
data: something needs categorize, a list
cond: list of the condition (os, ts, od, td) , length should be same with data
sub, run and breg (brain region name) is included in the filename
returns lists of categorized data
'''
def CatNSave(data, cond, sub=None, run=None, breg=None):
    os = []
    od = []
    ts = []
    td = []
    for i in range(len(data)):
        if cond[i] == 'os':
            os.append(data[i])
        elif cond[i] == 'od':
            od.append(data[i])
        elif cond[i] == 'ts':
            ts.append(data[i])
        elif cond[i] == 'td':
            td.append(data[i])
        else:
            print(cond[i] + ' not saved')
    np.savetxt('/Users/hycheng/Desktop/MS/113-2/BH/final_project/osGroupSR_' + str(sub) + str(run) + breg + '.csv', os)
    np.savetxt('/Users/hycheng/Desktop/MS/113-2/BH/final_project/odGroupSR_' + str(sub) + str(run) + breg + '.csv', od)
    np.savetxt('/Users/hycheng/Desktop/MS/113-2/BH/final_project/tsGroupSR_' + str(sub) + str(run) + breg + '.csv', ts)
    np.savetxt('/Users/hycheng/Desktop/MS/113-2/BH/final_project/tdGroupSR_' + str(sub) + str(run) + breg + '.csv', td)
    
    return 0
    
