import datetime


assert int(datetime.datetime.now().strftime('%M')) % 2 == 0, \
"Current datetime is an uneven number which we have deemed improper for some reason."
