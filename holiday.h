#include <cstdio>
#include <vector>

#ifndef HOLIDAY_H_
#define HOLIDAY_H_

class Holiday {
    int start_date;
    int end_date;
    int person;
    double v; //"хорошесть" отпуска относительно пожеланий сотрудника (см. v(w))

    public:
    Holiday(int new_start_date, int new_end_date, int new_person);
    int get_start_date();
    int get_end_date();
    int get_person();
    double get_v();
    void set_v(double new_v);
    double hol_eval(double w, std::vector<std::pair<int, int>> wishes); //функция расчета v(w)
};

#endif //HOLIDAY_H_