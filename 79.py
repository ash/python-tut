import datetime

n = datetime.datetime.now()
print(n.strftime('year=%Y, month=%m, month name=%B, week=%W, dayofweek=%w, day=%d, day name=%A'))
print(n.strftime("Today is %d.%m.%Y, %A"))


# print('My birthday is on %dth of %s.' % (15, 'September'))
# print('My birthday is on {0}th of {1}.'.format(15, 'September'))
