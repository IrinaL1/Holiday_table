import math
import random

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

def distr_holid(i):
    #выбираем начало длиного отпуска
    ind = random.randint(0,len(kalendar) - 10)
    day_start_end_personal_holidays.append([i, kalendar[ind], kalendar[ind + 9]])
    #выбираем начало короткого отпуска
    if ind - 10 < 0:
        ind1 = random.randint(ind + 15, len(kalendar) - 5)
    elif ind + 20 > len(kalendar):
        ind1 = random.randint(0, ind - 10)
    else:
        ind1_1 = random.randint(0, ind - 10)
        ind1_2 = random.randint(ind + 15, len(kalendar) - 5)
        ind1 = random.choice([ind1_1, ind1_2])
    day_start_end_personal_holidays.append([i, kalendar[ind1], kalendar[ind1 + 4]])
    buf = ind - ind1
    if buf < 20 and buf > -25:
        if buf > 0:
            if ind1 - 10 < 0:
                ind2 = random.randint(ind + 15, len(kalendar) - 5)
            elif ind + 20 > len(kalendar):
                ind2 = random.randint(0, ind1 - 10)
            else:
                ind2_1 = random.randint(0, ind1 - 10)
                ind2_2 = random.randint(ind + 15, len(kalendar) - 5)
                ind2 = random.choice([ind2_1, ind2_2])
        else:
            if ind - 10 < 0:
                ind2 = random.randint(ind1 + 10, len(kalendar) - 5)
            elif ind1 + 15 > len(kalendar):
                ind2 = random.randint(0, ind - 10)
            else:
                ind2_1 = random.randint(0, ind - 10)
                ind2_2 = random.randint(ind1 + 10, len(kalendar) - 5)
                ind2 = random.choice([ind2_1, ind2_2])
    else:
        if buf > 0:
            if ind1 - 10 < 0:
                ind2_2 = random.randint(ind + 15, len(kalendar) - 5)
                ind2_3 = random.randint(ind1 + 10, ind - 10)
                ind2 = random.choice([ind2_2, ind2_3])
            elif ind + 20 > len(kalendar):
                ind2_1 = random.randint(0, ind1 - 10)
                ind2_3 = random.randint(ind1 + 10, ind - 10)
                ind2 = random.choice([ind2_1, ind2_3])
            else:
                ind2_1 = random.randint(0, ind1 - 10)
                ind2_2 = random.randint(ind + 15, len(kalendar) - 5)
                ind2_3 = random.randint(ind1 + 10, ind - 10)
                ind2 = random.choice([ind2_1, ind2_2, ind2_3])
        else:
            if ind - 10 < 0:
                ind2_2 = random.randint(ind1 + 10, len(kalendar) - 5)
                ind2_3 = random.randint(ind + 15, ind1 - 10)
                ind2 = random.choice([ind2_2, ind2_3])
            elif ind1 + 15 > len(kalendar):
                ind2_1 = random.randint(0, ind - 10)
                ind2_3 = random.randint(ind + 15, ind1 - 10)
                ind2 = random.choice([ind2_1, ind2_3])
            else:
                ind2_1 = random.randint(0, ind - 10)
                ind2_2 = random.randint(ind1 + 10, len(kalendar) - 5)                
                ind2_3 = random.randint(ind + 15, ind1 - 10)
                ind2 = random.choice([ind2_1, ind2_2, ind2_3])
    day_start_end_personal_holidays.append([i, kalendar[ind2], kalendar[ind2 + 4]])

kalendar = [i for i in range(1,366)]
file = open("holidays2023.txt", "r")
weekends = list(map(str, file.read().strip().split()))
for i in range(len(weekends)):
    day_int = date_trans(weekends[i])
    ind = kalendar.index(day_int)
    kalendar = kalendar[:ind]+kalendar[ind + 1:]
#print(kalendar)

count_personal = 6
count_personal_holidays = [20] * count_personal
day_start_end_personal_holidays = []
for i in range(count_personal):
    distr_holid(i)
for i in day_start_end_personal_holidays:
    print(i)