__author__ = 'Administrator'
import pickle
import os
# os.chdir('D:/Code/resources/chapter5')
James = []
Sarah = []
Julie = []
Mikey = []
try:
    # with open('D:/Code/resources/chapter5/james.txt','rb')as james_file,open('D:/Code/resources/chapter5/julie.txt','rb')as julie_file,open('D:/Code/resources/chapter5/mikey.txt','rb')as mikey_file,open('D:/Code/resources/chapter5/sarah.txt','rb')as sarah_file:
    #     James = pickle.load(james_file)
    #     Sarah = pickle.load(sarah_file)
    #     Julie = pickle.load(julie_file)
    #     Mikey = pickle.load(mikey_file)
    Jamesdata = open('D:/Code/resources/chapter5/james.txt','r')
    Sarahdata = open('D:/Code/resources/chapter5/sarah.txt','r')
    Juliedata = open('D:/Code/resources/chapter5/julie.txt','r')
    Mikeydata = open('D:/Code/resources/chapter5/mikey.txt','r')
    James = Jamesdata.read().strip().split(',')
    Sarah = Sarahdata.read().strip().split(',')
    Julie = Juliedata.read().strip().split(',')
    Mikey = Mikeydata.read().strip().split(',')
    print(James)
    print(sorted(James))
    print(Sarah)
    print(sorted(Sarah))
    print(Julie)
    print(sorted(Julie))
    print(Mikey)
    print(sorted(Mikey))
    # James.append()
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as perr:
    print('Pickle error:'+str(perr))
finally:
    Jamesdata.close()
    Juliedata.close()
    Mikeydata.close()
    Sarahdata.close()
    pass
    #
    # print(Sarah)
    # print(Julie)
    # print(Mikey)
