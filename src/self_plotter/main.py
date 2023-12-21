from data_loader import data_loader as data_loader

dehum_input = r"C:\Users\ajayj\DehumGraph\data\Main Data\Deh(in).csv"

data = data_loader(dehum_input)
print(data.head())
print(data.shape)