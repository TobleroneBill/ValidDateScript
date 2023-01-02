import re
import pyperclip
# gets input and check if it has dates using format: DD/MM/YYYY. Then checks validity

MonthToDays = {
    ('01','January',31),
    ('02', 'February', 28),     # This one is weird
    ('03', 'March', 31),
    ('04', 'April', 30),
    ('05', 'May', 31),
    ('06', 'June', 30),
    ('07', 'July', 31),
    ('08', 'August', 31),
    ('09', 'September', 30),
    ('10', 'October', 31),
    ('11', 'November', 30),
    ('12', 'December', 31)
}


def ValidDayRange(day,limit):
    if day < 0 or day > limit:
        return False
    else:
        return True

def leapyearValid(year, day):
    # Years divisible by 100 arent leap years, unless they are divisible by 400
    # if leap year
    if year % 100 == 0:  # invalid leapyear
        if year % 400 == 0:  # valid leap year
            # Leap year day range
            return ValidDayRange(day,29)
        else:
            # normal day range
            return ValidDayRange(day,28)
    # if the above 2 didnt match, then test for leap year the regular way
    elif year % 4 == 0:
        # leap range
        return ValidDayRange(day,29)
    else:
        # normal Range
        return ValidDayRange(day,28)

#regex for ??/??/???????????????????????????????????????????? (FOREVER :D)
dateRe = re.compile(r'(\d{2})/(\d{2})/(\d+)')

string = pyperclip.paste()

dateMatches = dateRe.findall(string)

validatedDates = []
for date in dateMatches:
    # Convert into date components
    day = int(date[0])
    month = date[1]
    year = int(date[2])

    validDate = False
    for item in MonthToDays:
        # If the month matches, the month tuple[0]
        if item[0] == month:
            # If feb
            if month == '02':
                validDate = leapyearValid(year,day)
            else:
            # If less than 0 or greater than the month's largest date, It is invalid
                validDate = ValidDayRange(day,item[2])
                break

    datestring = f'{date[0]}/{date[1]}/{date[2]}'
    # If month isn't in range, this will always be false
    if validDate == False:
        validatedDates.append(f'invalid Date ({datestring})')
    else:
        validatedDates.append(datestring)

cpString = ''
for item in enumerate(validatedDates):
    print(f'{item[0]+1}: {item[1]}')
    cpString += f'{item[0]+1}: {item[1]} \n'

pyperclip.copy(cpString)

