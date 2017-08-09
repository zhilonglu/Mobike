import numpy as np


path = "C:\\Users\\NLSDE\\Desktop\\Mobike\\"


user_dict={}
with open(path+"train.csv") as f:
    f.readline()#skip the header
    all = f.readlines()
    for i in range(len(all)):
        value = all[i].replace("\n","").split(",")
        orderid = value[0]
        userid = value[1]
        bikeid = value[2]
        biketype = value[3]
        starttime = value[4]
        geohashed_start_loc = value[5]
        geohashed_end_loc = value[6]
        key = userid+"#"+geohashed_start_loc
        if key not in user_dict.keys():
            user_dict[key] = {}
            user_dict[key][geohashed_end_loc] = 1
        else:
            valueList = user_dict[key]
            isFind = False
            for v in valueList.keys():
                if geohashed_end_loc in v:
                    valueList[v] +=1
                    isFind = True
            if isFind == False:
                valueList[geohashed_end_loc] = 1
            user_dict[key] = valueList
for key in user_dict:
    temp = sorted(user_dict[key].items(),key=lambda item:item[1],reverse=True)
    user_dict[key] = temp
# print(user_dict)
result = {}
with open(path+"test.csv") as f2:
    f2.readline()  # skip the header
    all = f2.readlines()
    for i in range(len(all)):
        value = all[i].replace("\n", "").split(",")
        orderid = value[0]
        userid = value[1]
        bikeid = value[2]
        biketype = value[3]
        starttime = value[4]
        geohashed_start_loc = value[5]
        result[orderid] = []
        key = userid+"#"+geohashed_start_loc
        if key in user_dict.keys():#表明key存在
            tempV = user_dict[userid+"#"+geohashed_start_loc]
        else:#key不存在，表明该用户曾经并未出现在这个地方
            break
        cnt = 0
        print(tempV)
        for v in tempV:
            if cnt <=3:
                result[orderid].append(v[1])
                cnt +=1
print(result)



