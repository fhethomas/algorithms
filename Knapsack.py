
# coding: utf-8

# # 0-1 Knapsack problem

# In[184]:

# dynamic programming solution
import numpy as np
import pandas as pd

def namer(item,sub):
    return str(item)+'_'+str(sub)
def knapsack(items,knapsack_size):
    """
    Parameters
    ------------
    items : list
        items = [['item0',weight_int0,value_int0],
                 ['item1',weight_int1,value_int1]]
    knapsack_size : integer
        knapsack size as an integer
    Returns
    ------------
    items : list of strings
        The list of items for knapsack size
    value: integer
        The value of items output
    """
    columns=['item','weight','value']
    df=pd.DataFrame(items,columns=columns)
    df=df.sort_values(by='weight')
    sub_sack_values=np.zeros((len(df['weight']),knapsack_size+1))
    # keys will be in the format item_sacksize
    item_dictionary ={}
    sub_sack=np.arange(min(df['weight']),knapsack_size+1)
    for item in range(len(df['weight'])):
        sub_df=df.iloc[item,:]
        item_name = sub_df[0]
        weight=sub_df[1]
        value=sub_df[2]
        for sub in sub_sack:
            item_key = namer(item,sub)
            # max of previous max
            m_val = sub_sack_values[item-1,sub]
            if namer(item-1,sub) in item_dictionary.keys():
                m_item  = item_dictionary[namer(item-1,sub)]
            else:
                m_item = []
            # and value of current item + value of remaining space
            remaining_space = sub-weight
            if remaining_space>0 and item>0:
                remaining_value = sub_sack_values[item-1,sub-weight]
                remaining_item = item_dictionary[namer(item-1,sub-weight)] +[item_name]
            else:
                remaining_value=0
                remaining_item = [item_name]
            current_remaining_value = value + remaining_value
            # which is bigger?
            if m_val > current_remaining_value:
                sub_sack_values[item,sub]=m_val
                item_dictionary[item_key]=m_item
            else:
                sub_sack_values[item,sub]=current_remaining_value
                item_dictionary[item_key]=remaining_item
    items = item_dictionary[namer(len(items)-1,knapsack_size)]
    value = sub_sack_values[-1,-1]
    return items,value

