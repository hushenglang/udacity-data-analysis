import unicodecsv

### the plain way to read the file, need to mannually close the file.
# f = open('../csv_file/enrollments.csv', 'rb')
# reader = unicodecsv.DictReader(f)
# ### reader will only be iteratered once.
# for row in reader:
#     enrollments.append(row)
# f.close()

### the "with as" way to read the file, it will close the file automatically.
# with open('../csv_file/enrollments.csv', 'rb') as f:
#     reader = unicodecsv.DictReader(f)
#     ### reader will only be iteratered once.
#     for row in reader:
#         enrollments.append(row)


def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('../csv_file/enrollments.csv')
daily_engagement = read_csv('../csv_file/daily_engagement.csv')
project_submissions = read_csv('../csv_file/project_submissions.csv')

print len(enrollments)

unique_enrolled_students = set()
for enrollment in enrollments:
    unique_enrolled_students.add(enrollment['account_key'])
print len(unique_enrolled_students)

print len(daily_engagement)

unique_engagement_students = set()
for engagement_record in daily_engagement:
    unique_engagement_students.add(engagement_record['acct'])
print len(unique_engagement_students)

print len(project_submissions)

unique_project_submitters = set()
for submission in project_submissions:
    unique_project_submitters.add(submission['account_key'])
print len(unique_project_submitters)