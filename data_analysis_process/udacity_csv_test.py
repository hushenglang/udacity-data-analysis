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
print engagement[0]['account_key']
print submissions[0]

enrollAccountKeys = map(lambda x: x['account_key'], enrollments)
engagementAccountKeys = map(lambda x: x['account_key'], engagement)
strangeAccountKeys = list(set(enrollAccountKeys).difference(set(engagementAccountKeys)))

strangeEnrollments = [e for e in enrollments if
                      e['account_key'] in strangeAccountKeys and e['join_date'] != e['cancel_date']]
print 'result:', len(strangeEnrollments)
print strangeEnrollments[0]


###########################################################
udacity_test_accounts = set([e['account_key'] for e in enrollments if e['is_udacity'] == 'True'])
print 'udacity_test_accounts num:', len(udacity_test_accounts)
print 'udacity_test_accounts', udacity_test_accounts

def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data

non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(engagement)
non_udacity_submissions = remove_udacity_accounts(submissions)

print 'non_udacity_enrollments: ', len(non_udacity_enrollments)


##########################################################
paid_students = {}
for enrollment in non_udacity_enrollments:
    if (not enrollment['is_canceled'] or
            enrollment['days_to_cancel'] > 7):
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if (account_key not in paid_students or
                    enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date
print 'paid_students:', len(paid_students)


##########################################################
def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)
print len(paid_enrollments)
print len(paid_engagement)
print len(paid_submissions)


###########################################################
def within_one_week(join_date, engagement_date):
    time_delta = en gagement_date - join_date
    return time_delta.days < 7

paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']
    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

print len(paid_engagement_in_first_week)
