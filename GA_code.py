import math
import random
import copy
import ctypes

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
    global day_start_end_personal_holidays
    #выбираем начало длиного отпуска
    ind = random.randint(0,len(kalendar) - 10)
    b = lib.create(kalendar[ind], kalendar[ind + 9], i)
    day_start_end_personal_holidays.append(b)
    #выбираем начало короткого отпуска, если его нельзя вставить перед длинным
    if ind - 10 < 0:
        ind1 = random.randint(ind + 15, len(kalendar) - 5)
    #1-ый кор.отп. если нельзя вставить после длинного 
    elif ind + 20 > len(kalendar):
        ind1 = random.randint(0, ind - 10)
    #если можем вставить и до и после
    else:
        ind1_1 = random.randint(0, ind - 10)
        ind1_2 = random.randint(ind + 15, len(kalendar) - 5)
        ind1 = random.choice([ind1_1, ind1_2])
    b = lib.create(kalendar[ind1], kalendar[ind1 + 4], i)
    day_start_end_personal_holidays.append(b)
    buf = ind - ind1
    #если не можем вставить между отпусками
    if buf < 20 and buf > -25:
    #если длинный позже короткого
        if buf > 0:
    #если нельзя перед коротким вставить
            if ind1 - 10 < 0:
                ind2 = random.randint(ind + 15, len(kalendar) - 5)
    #если нельзя после длинного вставить
            elif ind + 20 > len(kalendar):
                ind2 = random.randint(0, ind1 - 10)
    #если можно вставить и до и после
            else:
                ind2_1 = random.randint(0, ind1 - 10)
                ind2_2 = random.randint(ind + 15, len(kalendar) - 5)
                ind2 = random.choice([ind2_1, ind2_2])
    #если короткий позже
        else:
    #если нельзя вставить перед длинным
            if ind - 10 < 0:
                ind2 = random.randint(ind1 + 10, len(kalendar) - 5)
    #если нельзя вставить после короткого
            elif ind1 + 15 > len(kalendar):
                ind2 = random.randint(0, ind - 10)
    #если можно встаивть и до и после
            else:
                ind2_1 = random.randint(0, ind - 10)
                ind2_2 = random.randint(ind1 + 10, len(kalendar) - 5)
                ind2 = random.choice([ind2_1, ind2_2])
    #если можно вставить между отпусками
    else:
    #если длинный позже короткого
        if buf > 0:
    #если можно вставить только между отпусками
            if ind1 - 10 < 0 and ind + 20 > len(kalendar):
                ind2 = random.randint(ind1 + 10, ind - 10)
    #если нельзя вставить до короткого
            elif ind1 - 10 < 0:
                ind2_2 = random.randint(ind + 15, len(kalendar) - 5)
                ind2_3 = random.randint(ind1 + 10, ind - 10)
                ind2 = random.choice([ind2_2, ind2_3])
    #если нельзя вставить после длинного
            elif ind + 20 > len(kalendar):
                ind2_1 = random.randint(0, ind1 - 10)
                ind2_3 = random.randint(ind1 + 10, ind - 10)
                ind2 = random.choice([ind2_1, ind2_3])
    #если можно вставить куда угодно
            else:
                ind2_1 = random.randint(0, ind1 - 10)
                ind2_2 = random.randint(ind + 15, len(kalendar) - 5)
                ind2_3 = random.randint(ind1 + 10, ind - 10)
                ind2 = random.choice([ind2_1, ind2_2, ind2_3])
    #если короткий позже
        else:
    #если можно всавить только между
            if ind - 10 < 0 and ind1 + 15 > len(kalendar):
                ind2 = random.randint(ind + 15, ind1 - 10)
    #если нельзя вставить до длинного
            elif ind - 10 < 0:
                ind2_2 = random.randint(ind1 + 10, len(kalendar) - 5)
                ind2_3 = random.randint(ind + 15, ind1 - 10)
                ind2 = random.choice([ind2_2, ind2_3])
    #если нельзя вставить после короткого
            elif ind1 + 15 > len(kalendar):
                ind2_1 = random.randint(0, ind - 10)
                ind2_3 = random.randint(ind + 15, ind1 - 10)
                ind2 = random.choice([ind2_1, ind2_3])
    #если можно вставить куда угодно
            else:
                ind2_1 = random.randint(0, ind - 10)
                ind2_2 = random.randint(ind1 + 10, len(kalendar) - 5)                
                ind2_3 = random.randint(ind + 15, ind1 - 10)
                ind2 = random.choice([ind2_1, ind2_2, ind2_3])
    b = lib.create(kalendar[ind2], kalendar[ind2 + 4], i)
    day_start_end_personal_holidays.append(b)
   # return day_start_end_personal_holidays

def mutation(count_pers):
    global mutant
    global day_start_end_personal_holidays
    for i in range(len(mutant)):
        buf = random.randint(0, count_pers - 1)
        j = 0
        while j < len(mutant[i]):
            if mutant[i][j][0] == buf:
                mutant[i] = mutant[i][:j] + mutant[i][j + 1:]
                continue
            j += 1
        distr_holid(buf)
        mutant[i] += day_start_end_personal_holidays
        day_start_end_personal_holidays = []

def reproduction():
    global children
    parent_A = random.choice(population)
    

kalendar = [i for i in range(1,366)]
file = open("holidays2023.txt", "r")
weekends = list(map(str, file.read().strip().split()))
for i in range(len(weekends)):
    day_int = date_trans(weekends[i])
    ind = kalendar.index(day_int)
    kalendar = kalendar[:ind]+kalendar[ind + 1:]
#print(kalendar)

lib = ctypes.CDLL('./lib.so')
lib.create.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.create.restype = ctypes.c_void_p
lib.get_start_date.argtypes = [ctypes.c_void_p]
lib.get_start_date.restype = ctypes.c_int
lib.get_end_date.argtypes = [ctypes.c_void_p]
lib.get_end_date.restype = ctypes.c_int
lib.get_person.argtypes = [ctypes.c_void_p]
lib.get_person.restype = ctypes.c_int
lib.get_v.argtypes = [ctypes.c_void_p]
lib.get_v.restype = ctypes.c_double
#lib.hol_eval.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_void_p]
#lib.hol_eval.restype = ctypes.c_double

count_personal = 40
count_personal_holidays = [20] * count_personal
day_start_end_personal_holidays = []
population = []
wishes = []
for j in range(100):
    for i in range(count_personal):
        distr_holid(i)
    population.append(copy.deepcopy(day_start_end_personal_holidays))
    day_start_end_personal_holidays = []
for i in population:
    for j in i:
        print(lib.get_start_date(j), end = ' ')
        print(lib.get_end_date(j), end = ' ')
        print(lib.get_person(j), end = ' ')
        print(lib.get_v(j))
    print("-------------------------------------------------")

mutant = copy.deepcopy(population)
#mutation(count_personal)
#print("##########################################")
#for i in mutant:
#    for j in i:
#        print(j)
#    print("-------------------------------------------------")
#children = []
