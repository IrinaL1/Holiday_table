import math
import random
import copy
import ctypes

def date_trans(date_string):
    if date_string[:4].count(".") == 0:
        year, month, day = map(int, date_string.strip().split('.'))
    else:
        day, month, year = map(int, date_string.strip().split('.'))
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

def distr_holid(i, grafic):
    global flag
    global dict_wish_date
    #выбираем начало длиного отпуска
    ind = random.randint(0,len(kalendar) - 10)
    b = lib.create_H(kalendar[ind], kalendar[ind + 9], i)
    string = dict_wish_date.get(lib.get_person(b), ["",0])
    a = ctypes.create_string_buffer(str.encode(string[0]))
    v = lib.hol_eval(b, string[1], a)
    lib.set_v(b, v)
    if flag:
        grafic = lib.create_S(b)
        flag = False
    else:
        lib.set_hol(grafic, b)
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
    b = lib.create_H(kalendar[ind1], kalendar[ind1 + 4], i)
    string = dict_wish_date.get(lib.get_person(b), ["",0])
    a = ctypes.create_string_buffer(str.encode(string[0]))
    v = lib.hol_eval(b, string[1], a)
    lib.set_v(b, v)
    lib.set_hol(grafic, b)
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
    b = lib.create_H(kalendar[ind2], kalendar[ind2 + 4], i)
    string = dict_wish_date.get(lib.get_person(b), ["",0])
    a = ctypes.create_string_buffer(str.encode(string[0]))
    v = lib.hol_eval(b, string[1], a)
    lib.set_v(b, v)
    lib.set_hol(grafic, b)
    return grafic
   # return day_start_end_personal_holidays

def mutation(count_pers):
    global mutant
    global population
    global grafic
    global flag
    for i in range(len(mutant)):
        buf = random.randint(0, count_pers - 1)
        j = 0
        while j < lib.length(mutant[i]):
            if lib.get_person(lib.get_h(mutant[i], j)) == buf:
                lib.delit(mutant[i], j)
                continue
            j += 1
        flag = False
        mutant[i] = distr_holid(buf, mutant[i])
    population += mutant

def reproduction():
    global childrens
    global population
    global count_personal
    children = 0
    parent = copy.deepcopy(population)
    while len(parent) > 1:
        ind_parent_A = random.randint(0, len(parent) // 2 - 1)
        ind_parent_B = random.randint(len(parent) // 2, len(parent) - 1)
        parent_A = parent[ind_parent_A]
        parent_B = parent[ind_parent_B]
        l_a = lib.length(parent_A)
        l_b = lib.length(parent_B)
        flag = True
        for i in range(0, count_personal):
            chek = random.random()
            if chek < 0.5:
                for j in range(l_a):
                    b = lib.get_h(parent_A, j)
                    if i == 0 and flag:
                        if i == lib.get_person(b):
                            children = lib.create_S(b)
                            flag = False 
                    else:
                        if i == lib.get_person(b):
                            lib.set_hol(children, b)
            else:
                for j in range(l_b):
                    b = lib.get_h(parent_B, j)
                    if i == 0 and flag:
                        if i == lib.get_person(b):
                            children = lib.create_S(b)
                            flag = False 
                    else:
                        if i == lib.get_person(b):
                            lib.set_hol(children, b)
        parent = parent[:min(ind_parent_A, ind_parent_B)] + parent[min(ind_parent_A, ind_parent_B) + 1:max(ind_parent_A, ind_parent_B)] + parent[max(ind_parent_A, ind_parent_B) + 1:]
        childrens.append(children)
        children = 0
    population += childrens

def choise():
    global k1
    global k2
    global k3
    global population
    global count_population
    for i in range(len(population)):
        grafic = population[i]
        l = lib.length(grafic)
        if lib.get_gr_cost(grafic) == 0:
            sum_f = 0
            for j in range(l):
                b = lib.get_h(grafic, j)
                f_w = k3 * lib.get_v(b)
                sum_f += f_w
            sum_f /= l
            d = lib.get_gr_destr(grafic)
            m = lib.get_gr_min(grafic)
            A = sum_f + k1 * d + k2 * m
            lib.set_gr_cost(grafic, A)
        for j in range(i):
            A1 = lib.get_gr_cost(population[i])
            A2 = lib.get_gr_cost(population[j])
            if A1 > A2:
                population = population[:j] + [population[i]] + population[j:i] + population[i + 1:]
                break
    for i in range(count_population, len(population)):
        lib.clean(population[i])
    population = population[:count_population]
        

def input_date(inp):
    flag = False
    s_imp_date = ""
    for i in inp:
        if i == "-":
            s_imp_date += i
            flag = True
        else:
            if i[-1] == ";": i = i[:-1]
            if flag:
                if buff > date_trans(i):
                    print("error impotant date")
                    exit()
                flag = False
                buff = date_trans(i)
                s_imp_date += str(buff) + ';'
                continue
            buff = date_trans(i)
            s_imp_date += str(buff)
    return s_imp_date

k1 = 5
k2 = 3
k3 = 3

kalendar = [i for i in range(1,366)]
work_days = [[] for i in range(12)]
file = open("holidays2023.txt", "r")
weekends = list(map(str, file.read().strip().split()))
file.close()
file = open("imp_dates.txt", "r")
inp = list(map(str, file.read().strip().split()))
s_imp_date = input_date(inp)
s_imp_date = s_imp_date[:-1]
file.close()
file = open("information.txt", "r")
count_personal = int(file.readline())
inp = list(map(str, file.read().strip().split("\n")))
person_ind = {}
dict_wish_date = {}
for i in range(len(inp)):
    inp_1, inp_2 = inp[i].split("-")
    inp_2 = float(inp_2)
    if not(inp_1[-1].isalpha()): inp_1 = inp_1[:-1]
    person_ind[inp_1] = i
    dict_wish_date[i] = ["", inp_2]
file.close()
file = open("wishes_date.txt", "r")
inp = list(map(str, file.read().strip().split("\n")))
for i in inp:
    inp_1 = list(map(str, i.strip().split()))
    inp_1 = [(inp_1[0] + " " + inp_1[1])] + inp_1[2:]
    ind = person_ind[inp_1[0][:-1]]
    s_wishes_date = input_date(inp_1[1:])
    dict_wish_date[ind][0] = s_wishes_date[:-1]
file.close()

for i in range(len(weekends)):
    day_int = date_trans(weekends[i])
    ind = kalendar.index(day_int)
    kalendar = kalendar[:ind]+kalendar[ind + 1:]
#print(kalendar)
for i in kalendar:
    if i <= 31: work_days[0].append(i)
    elif i <= 31 + 28: work_days[1].append(i)
    elif i <= 31 + 28 + 31: work_days[2].append(i)
    elif i <= 31 + 28 + 31 + 30: work_days[3].append(i)
    elif i <= 31 + 28 + 31 + 30 + 31: work_days[4].append(i)
    elif i <= 31 + 28 + 31 + 30 + 31 + 30: work_days[5].append(i)
    elif i <= 31 + 28 + 31 + 30 + 31 + 30 + 31: work_days[6].append(i)
    elif i <= 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31: work_days[7].append(i)
    elif i <= 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30: work_days[8].append(i)
    elif i <= 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31: work_days[9].append(i)
    elif i <= 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30: work_days[10].append(i)
    else: work_days[11].append(i)

str_calendar = ""
for i in work_days:
    for j in i:
        str_calendar += str(j) + ' '
    str_calendar += "0 "
str_calendar = str_calendar[:-3]

lib = ctypes.CDLL('./lib.so')
lib.create_H.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.create_H.restype = ctypes.c_void_p
lib.get_start_date.argtypes = [ctypes.c_void_p]
lib.get_start_date.restype = ctypes.c_int
lib.get_end_date.argtypes = [ctypes.c_void_p]
lib.get_end_date.restype = ctypes.c_int
lib.get_person.argtypes = [ctypes.c_void_p]
lib.get_person.restype = ctypes.c_int
lib.get_v.argtypes = [ctypes.c_void_p]
lib.get_v.restype = ctypes.c_double
lib.hol_eval.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_char_p]
lib.hol_eval.restype = ctypes.c_double
lib.set_v.argtypes = [ctypes.c_void_p, ctypes.c_double]
lib.create_S.argtypes = [ctypes.c_void_p]
lib.create_S.restype = ctypes.c_void_p
lib.get_gr_destr.argtypes = [ctypes.c_void_p]
lib.get_gr_destr.restype = ctypes.c_double
lib.get_gr_min.argtypes = [ctypes.c_void_p]
lib.get_gr_min.restype = ctypes.c_double
lib.get_gr_cost.argtypes = [ctypes.c_void_p]
lib.get_gr_cost.restype = ctypes.c_double
lib.set_gr_destr.argtypes = [ctypes.c_void_p, ctypes.c_double]
lib.set_gr_min.argtypes = [ctypes.c_void_p, ctypes.c_double]
lib.set_gr_cost.argtypes = [ctypes.c_void_p, ctypes.c_double]
lib.calc_min.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
lib.calc_min.restype = ctypes.c_double
lib.set_hol.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.calc_distr.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
lib.calc_distr.restype = ctypes.c_double
lib.length.argtypes = [ctypes.c_void_p]
lib.length.restype = ctypes.c_int
lib.get_h.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.get_h.restype = ctypes.c_void_p
lib.delit.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.clean.argtypes = [ctypes.c_void_p]

count_personal_holidays = [20] * count_personal
day_start_end_personal_holidays = []
population = []
wishes = []
grafic = 0
count_population = 4
for j in range(count_population):
    flag = True
    for i in range(count_personal):
        grafic = distr_holid(i, grafic)
    population.append(grafic)
    grafic = 0
k = 0
while True:

    childrens = []
    reproduction()

    mutant = []
    for i in population:
        l = lib.length(i)
        for j in range(l):
            if j == 0:
                b = lib.get_h(i, j)
                mut = lib.create_S(b)
            else:
                b = lib.get_h(i, j)
                lib.set_hol(mut, b)
        mutant.append(mut)
    mutation(count_personal)
    
    for i in population:
        a = ctypes.create_string_buffer(str.encode(str_calendar))
        b = ctypes.create_string_buffer(str.encode(s_imp_date))
        d = lib.calc_distr(i, a, count_personal)
        m = lib.calc_min(i, b, count_personal)
        lib.set_gr_destr(i, d)
        lib.set_gr_min(i, m)
    
    choise()

    if k % 10000 == 0:
        print("destr = ", lib.get_gr_destr(population[0]))
        print("minim = ", lib.get_gr_min(population[0]))
        print("cost = ", lib.get_gr_cost(population[0]))
        i = population[0]
        for j_ in range(lib.length(i)):
            j = lib.get_h(i, j_)
            print(lib.get_start_date(j), end = ' ')
            print(lib.get_end_date(j), end = ' ')
            print(lib.get_person(j), end = ' ')
            print(lib.get_v(j))
        y_n = input("Если хотите закончить вычисление введите n: y/n ")
        if y_n == "n": break

'''
k=0
for i in population:
    print(k)
    k += 1
    a = ctypes.create_string_buffer(str.encode(str_calendar))
    b = ctypes.create_string_buffer(str.encode(s_imp_date))
    print(lib.calc_distr(i, a, count_personal), end = ' ')
    print(lib.calc_min(i, b, count_personal))
    for j_ in range(lib.length(i)):
        j = lib.get_h(i, j_)
        string = dict_wish_date.get(lib.get_person(j), ["",0])
        a = ctypes.create_string_buffer(str.encode(string[0]))
        print(lib.get_start_date(j), end = ' ')
        print(lib.get_end_date(j), end = ' ')
        print(lib.get_person(j), end = ' ')
        print(lib.get_v(j))
    print("-------------------------------------------------")
'''  