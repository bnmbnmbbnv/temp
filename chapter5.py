__author__ = 'Administrator'
import newinter34.temp.chapter5sanitize
# os.chdir('D:/Code/resources/chapter5')
def dataopen(dataurl):
    try:
        with open(dataurl) as daf:
            data = daf.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return (None)
James = dataopen('D:/Code/resources/chapter5/james.txt')
Sarah = dataopen('D:/Code/resources/chapter5/sarah.txt')
Julie = dataopen('D:/Code/resources/chapter5/julie.txt')
Mikey = dataopen('D:/Code/resources/chapter5/mikey.txt')
newJames = sorted(set([newinter34.temp.chapter5sanitize.chapter5sanitize(j) for j in James]))
newSarah = sorted(set([newinter34.temp.chapter5sanitize.chapter5sanitize(j) for j in Sarah]))
newJulie = sorted(set([newinter34.temp.chapter5sanitize.chapter5sanitize(j) for j in Julie]))
newMikey = sorted(set([newinter34.temp.chapter5sanitize.chapter5sanitize(j) for j in Mikey]))
print(newJames[0:3])
print(newSarah[0:3])
print(newJulie[0:3])
print(newMikey[0:3])

