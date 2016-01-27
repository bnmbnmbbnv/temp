__author__ = 'Administrator'
import pickle
# with open('D:/Code/resources/chapter5/james.txt','wb')as jame:
#     pickle.dump([12,'sdf',123],jame)
james = open('D:/Code/resources/chapter5/james.txt','rb')
# jj = open('mydata.pickle','rb')
a_list = pickle.load(james)
print(a_list)
# readsomething = open('D:/Code/resources/chapter5/james.txt','rb')
# rst = pickle.load(readsomething)
# print(rst)