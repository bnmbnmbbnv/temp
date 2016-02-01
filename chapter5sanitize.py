__author__ = 'Administrator'
def chapter5sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
       return (time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)
print('aaaa')