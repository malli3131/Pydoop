# This Script is used to compute the total, minimum, maximum volume of every stock

def mapper(_, text, writer):
    columns = text.split("\t")
    writer.emit(columns[1], int(columns[7]));

def reducer(key,values,writer):
    data = map(int,values)
    volmin = min(data)
    volmax = max(data)
    volsum = sum(data)
    record = str(volsum) + "\t" + str(volmin) + "\t" + str(volmax)
    writer.emit(key, record)
