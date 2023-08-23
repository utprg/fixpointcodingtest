import datetime
def gettime(timepoint,ms):
    year=int(timepoint[0:4])
    month=int(timepoint[4:6])
    day=int(timepoint[6:8])
    hour=int(timepoint[8:10])
    minute=int(timepoint[10:12])
    second=int(timepoint[12:14])
    milisecond=int(ms)*1000
    return datetime.datetime(year,month,day,hour,minute,second,milisecond)