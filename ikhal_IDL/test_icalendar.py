from sys import displayhook
from icalendar import Calendar, Event


def display(cal):
    return cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip()

cal = Calendar()
cal['dtstart'] = '20050404T080000'
cal['summary'] = 'Python meeting about calendaring the CHIZ'

print(cal['dtstart'])
print(display(cal))