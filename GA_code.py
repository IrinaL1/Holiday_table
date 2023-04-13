import math

def date_trans(date_string):
    year, month, day = map(int, date_string.strip().split('.'))
    if month == 1:
        n_date = day
    elif month == 2:
        n_date = day + 31
    elif month == 3:
        n_date = day + 31 + 28
    elif month == 4:
        n_date = day + 31 + 28 + 31
    elif month == 5:
        n_date = day + 31 + 28 + 31 + 30
    elif month == 6:
        n_date = day + 31 + 28 + 31 + 30 + 31
    elif month == 7: 
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30
    elif month == 8:
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif month == 9:
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif month == 10:
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif month == 11:
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif month == 12:
        n_date = day + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
    return n_date

k1 =1
k2 = 1
k3 = 1


def hol_eval_func (w, h_date_start, h_date_end, w_date_start, w_date_end):
    if (h_date_end - h_date_start <= 0):
        print("Wrong holiday. Change start = ", h_date_start, "and end date = ", h_date_end, "or check the lenght\n")
        return -1
    if (w_date_end - w_date_start <= 0):
        print("Wrong holiday. Change start = ", w_date_start, "and end date = ", w_date_end, "or check the lenght\n")
        return -1
    if (w == 0):
        return 1
    if (w == 0.5):
        w_date_start = w_date_start - 5
        w_date_end = w_date_end + 5
        if (h_date_start - w_date_start >= 0 and w_date_end - h_date_end >= 0):
            return 1
        elif (h_date_end - w_date_start >= 0 and h_date_end - w_date_end <= 0):
            return (h_date_end - w_date_start + 1)/(h_date_end - h_date_start + 1)
        elif (h_date_start - w_date_start >= 0 and h_date_start - w_date_end <= 0):
            return (w_date_end - h_date_start + 1)/(h_date_end - h_date_start + 1)
        else:
            return 0
    elif (w == 1):
        if (h_date_start - w_date_start >= 0 and w_date_end - h_date_end >= 0):
            return 1
        elif (h_date_end - w_date_start >= 0 and h_date_end - w_date_end <= 0):
            return (h_date_end - w_date_start + 1)/(h_date_end - h_date_start + 1)
        elif (h_date_start - w_date_start >= 0 and h_date_start - w_date_end <= 0):
            return (w_date_end - h_date_start + 1)/(h_date_end - h_date_start + 1)
        else:
            return 0
    else:
        print("Wrong value of w. It must be 0, 0.5 or 1.\n")
        return -1

def gr_eval_func():
    return 1


kalendar = [i for i in range(1,366)]
file = open("holidays2023.txt", "r")
weekends = list(map(str, file.read().strip().split()))
for i in range(len(weekends)):
    day_int = date_trans(weekends[i])
    ind = kalendar.index(day_int)
    kalendar = kalendar[:ind]+kalendar[ind + 1:]
print(kalendar)

a = hol_eval_func(1, 1, 8, 1, 7)
print(a)

