# This Script is used to compute the total volume of every stock

def mapper(_, text, writer):
    columns = text.split("\t")
    writer.emit(columns[1], int(columns[7]));

def reducer(key,values,writer):
    writer.emit(key, sum(map(int,values)))
