#include <cstdio>
#include <vector>

#ifndef HOLIDAY_H_
#define HOLIDAY_H_

class Holiday {
    int start_date;
    int end_date;
    int person;
    double v;

    public:
    Holiday(int new_start_date, int new_end_date, int new_person);
    ~Holiday();
    int get_start_date();
    int get_end_date();
    int get_person();
    double get_v();
    void set_v(double new_v);
    double hol_eval(double w, std::vector<std::pair<int, int>>);
};

#endif //HOLIDAY_H_