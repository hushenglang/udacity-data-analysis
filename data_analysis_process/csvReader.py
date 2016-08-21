import unicodecsv

enrollments = []

### the plain way to read the file, need to mannually close the file.
# f = open('../csv_file/enrollments.csv', 'rb')
# reader = unicodecsv.DictReader(f)
# ### reader will only be iteratered once.
# for row in reader:
#     enrollments.append(row)
# f.close()

### the "with as" way to read the file, it will close the file automatically.
with open('../csv_file/enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    ### reader will only be iteratered once.
    for row in reader:
        enrollments.append(row)

print enrollments[0]
print enrollments[1]
