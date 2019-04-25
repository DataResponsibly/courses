import math
import random
import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn import linear_model
from math import sqrt
from FAIR.FairnessInRankings import FairnessInRankingsTester


def standardizeData(data,colums_to_exclude=[]):
    """
        data is a dataframe stored all the data read from a csv source file
        colums_to_exclude is a array like data structure stored the attributes which should be ignored in the normalization process.
        return the standardized data
    """
    df = data.loc[:, data.columns.difference(colums_to_exclude)]# remove no weight attributes
    df_stand = (df - df.mean())/np.std(df)
    data.loc[:, data.columns.difference(colums_to_exclude)] = df_stand
    
    return data

def normalizeDataset(data,colums_to_exclude=[]):
    """
        data is a dataframe stored all the data read from a csv source file
        colums_to_exclude is a array like data structure stored the attributes which should be ignored in the normalization process.
        return the normalized data
    """
    df = data.loc[:,data.columns.difference(colums_to_exclude)] # remove no weight attributes
    norm_df = (df - df.min()) / (df.max() - df.min())
    data.loc[:,data.columns.difference(colums_to_exclude)] = norm_df

    return data

def computeFairRankingProbability(k,p,generated_ranking,default_alpha=0.05):
    """
    Sub-function to compute p-value used in FA*IR oracle

    Attributes:
        k: top_K value in FA*IR
        p: minimum proportion of protected group
        generated_ranking: input ranking of users
        default_alpha: default significance level of FA*IR
    Return:  p-value, fairness, rank position fail, adjusted significance level and list of ranking positions that protected group should be using FA*IR
    """
    ## generated_ranking is a list of tuples (id, "pro"),...(id,"unpro")

    gft = FairnessInRankingsTester(p, default_alpha, k, correctedAlpha=True)
    posAtFail, isFair = gft.ranked_group_fairness_condition(generated_ranking)

    p_value = gft.calculate_p_value_left_tail(k, generated_ranking)

    return p_value, isFair, posAtFail, gft.alpha_c, gft.candidates_needed

def computePairN(att_name, att_value, data):
    """
    Sub-function to compute number of pairs that input value > * used in Pairwise oracle

    Attributes:
        att_name: sensitive attribute name
        att_value: value of protected group of above attribute
        data: dataframe that stored the data 
    Return:  number of pairs of att_value > * in input data, number of pairs of att_value > * estimated using proportion, and proportion of group with att_value
    """
    # input checked_atts includes names of checked sensitive attributes
    total_N = len(data)
    # get the unique value of this sensitive attribute
    values_att = list (data[att_name].unique())
    # for each value, compute the current pairs and estimated fair pairs

    position_lists_val = data[data[att_name]==att_value].index+1
    size_vi = len(position_lists_val)
    count_vi_prefered_pairs = 0
    for i in range(len(position_lists_val)):
        cur_position = position_lists_val[i]
        left_vi = size_vi - (i + 1)
        count_vi_prefered_pairs = count_vi_prefered_pairs + (total_N - cur_position - left_vi)
    # compute estimated fair pairs
    total_pairs_vi = size_vi*(total_N-size_vi)
    estimated_vi_pair = math.ceil((size_vi / total_N) * total_pairs_vi)

    return int(count_vi_prefered_pairs),int(estimated_vi_pair),int(size_vi)

def mergeUnfairRanking(_px, _sensitive_idx, _fprob):  # input is the ranking
    """
    Generate a fair ranking.

    Attributes:
        _px: input ranking (sorted), list of ids
        _sensitive_idx: the index of protected group in the input ranking
        _fprob: probability to choose the protected group
    Return:  generated fair ranking, list of ids
    """
    #     _px=sorted(range(len(_inputrankingscore)), key=lambda k: _inputrankingscore[k],reverse=True)
    rx = [x for x in _px if x not in _sensitive_idx]
    qx = [x for x in _px if x in _sensitive_idx]
    rx.reverse()  # prepare for pop function to get the first element
    qx.reverse()
    res_list = []

    while (len(qx) > 0 and len(rx) > 0):
        r_cur = random.random()
        #         r_cur=random.uniform(0,1.1)
        if r_cur < _fprob:
            res_list.append(qx.pop())  # insert protected group first
        else:
            res_list.append(rx.pop())

    if len(qx) > 0:
        qx.reverse()
        res_list = res_list + qx
    if len(rx) > 0:
        rx.reverse()
        res_list = res_list + rx

    if len(res_list) < len(_px):
        print("Error!")
    return res_list

def Cdf(_input_array, x):
    """
    Compute the CDF value of input samples using left tail computation
    Attributes:
        _input_array: list of data points
        x: current K value
    Return:  value of cdf
    """
    # left tail
    count = 0.0
    for vi in _input_array:
        if vi <= x:
            count += 1.0
    prob = count / len(_input_array)
    return prob