from bs4 import BeautifulSoup
import requests

def fix_time(number):
    # Will increment parent variable with left over time and store the rest
    # Example:
    #   From 367 minutes it'll increment hours variable with 6 hours and store 7 minutes
    # This works the same for seconds and minutes

    if number/60 < 9:
        number = int(float( "0." + str(number/60)[2:]) * 60)
    elif number/60 > 9:
        number = int(float( "0." + str(number/60)[3:]) * 60)
    elif number/60 > 99:
        number = int(float( "0." + str(number/60)[4:]) * 60)
    elif m/60 > 999:
        number = int(float( "0." + str(number/60)[5:]) * 60)

    return number


def get_playlist_time(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    time_stamp_divs = soup.findAll('div', {'class': 'timestamp'})
    time_stamps = []

    for x in time_stamp_divs:
        time_stamps.append(x.text)

    h = 0
    m = 0
    s = 0

    # Splits the time stamp into the three different sections and appends each section into above variables
    # Hours, minutes and seconds

    for time_stamp in time_stamps:
        digits = time_stamp.split(":")

        # checks if time stamps are under an hour or a minute long
        if len(digits) == 3:
            h += int(digits[0])
            m += int(digits[1])
            s += int(digits[2])
        elif len(digits) == 2:
            m += int(digits[0])
            s += int(digits[1])
        else:
            s += int(digits[0])


    m += int(s/60)
    s = fix_time(s)

    h += int(m/60)
    m = fix_time(m)

    # output end result
    return("%s hours, %s minutes and %s seconds." % (h, m ,s))

if __name__ == '__main__':
    playlist_time = get_playlist_time("https://www.youtube.com/playlist?list=PLloEvDjFgtoRDJ0OatlYDNwyXjnPnF21y")
    print(playlist_time)