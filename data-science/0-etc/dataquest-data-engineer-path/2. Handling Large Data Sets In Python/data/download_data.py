from yahoo_finance import Share
import csv

goog = Share('GOOG')
data = goog.get_historical('2012-01-01', '2017-03-17')
write = []
write = [[d["Date"], d["Close"]] for d in data]

write = sorted(write, key=lambda x:x[0])
write.insert(0,["date", "price"])
with open("prices.csv", "w+") as f:
    writer = csv.writer(f)
    writer.writerows(write)