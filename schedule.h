#include <iostream>
#include <vector>
#include "holiday.h"

#ifndef SCHEDULE_H_
#define SCHEDULE_H_

class Schedule {
    std::vector<Holiday> gr;
    double d;   //"хорошесть" графика отпусков относительно распределния
    double m;   //"хорошесть" графика отпусков относительно минимизации числа отпусков в важные даты
    double cost;    //стоимость графика (значениие функции оценки)

    public:
    Schedule(Holiday h);
    virtual ~Schedule();
    double get_gr_destr();
    double get_gr_min();
    double get_gr_cost();
    Holiday* get_h(int i);
    void del(int i);
    int length();
    void set_gr_destr(double d_new);
    void set_gr_min(double m_new);
    void set_gr_cost(double cost_new);
    void set_hol(Holiday h);
    double calc_distr(std::vector<std::vector<int>>, int emp);
    double calc_min(std::vector<std::pair<int, int>> imp_dates, int emp);
    double calc_cost();
};


#endif //SCHEDULE_H_
