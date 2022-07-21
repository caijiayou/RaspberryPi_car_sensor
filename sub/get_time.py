from datetime import datetime

def get_time():
    DateTime = datetime.now()
    Time = str(DateTime.year) + '-' + str(DateTime.month) + '-' + str(DateTime.day)
    Time += ' ' + str(DateTime.hour) + ':' + str(DateTime.minute) + ':' + str(DateTime.second)
    return Time
    # print(Time)

if __name__=='__main__':
    getTime = get_time()
    print(getTime)