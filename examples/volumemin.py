# This Script is used to compute the minimum volume of every stock

def mapper(_, text, writer):
    columns = text.split("\t")
    writer.emit(columns[1], int(columns[7]));

def reducer(key,values,writer):
    data = map(int,values)
    volmin = min(data)
    writer.emit(key, volmin)
