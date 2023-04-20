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
    void set_gr_destr();
    void set_gr_min();
};

#endif //SCHEDULE_H_