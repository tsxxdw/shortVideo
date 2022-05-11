import datetime


def getDateStr1():
    current_date = datetime.datetime.now().strftime('%Y%m%d')
    return current_date

def getDateStr2():
    current_date = datetime.datetime.now().strftime('%HH%MM%SS')
    return current_date

def getDateStr3():
    current_date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return current_date


if __name__ == '__main__':
    result = getDateStr1()
    print(result)
