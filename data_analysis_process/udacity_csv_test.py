import unicodecsv

enrollments_filename = '../csv_file/enrollments.csv'
engagement_filename = '../csv_file/daily_engagement.csv'
submissions_filename = '../csv_file/project_submissions.csv'

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv(enrollments_filename)
engagement = read_csv(engagement_filename)
submissions = read_csv(submissions_filename)

print enrollments[0]
print engagement[0]
print submissions[0]