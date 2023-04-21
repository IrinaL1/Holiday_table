#include <iostream>
#include <vector>
#include <algorithm> 

#include "schedule.h"

Schedule::Schedule(Holiday h){
    this->gr.push_back(h);
    this->d = 0;
    this->m = 0;
    this->cost = 0;
}

Schedule::~Schedule(){
    gr.clear();
}

double Schedule::get_gr_destr(){
    return d;
}

double Schedule::get_gr_min(){
    return m;
}

double Schedule::get_gr_cost(){
    return cost;
}

void Schedule::set_gr_destr(double d_new){
    d = d_new;
}

void Schedule::set_gr_min(double m_new){
    m = m_new;
}

void Schedule::set_gr_cost(double cost_new){
    cost = cost_new;
}

double Schedule::calc_distr(){

}

//На вход подаются важные даты со включением обеих границ (нач. дата, кон. дата), число сотрудников
double Schedule::calc_min(std::vector<std::pair<int, int>> imp_dates, int emp){
    std::vector <double> minim;
    if(imp_dates.size() == 0){
        printf("Список важных дат пуст\n");
        return 1;
    }
    for(int i = 0; i < imp_dates.size(); i++){
        int workdays = emp * (imp_dates[i].second - imp_dates[i].first + 1);
        for(int j = 0; j < gr.size(); j++){
            if(gr[j].get_end_date() >= imp_dates[i].first && gr[j].get_end_date() <= imp_dates[i].second){
                minim[i] = 1 - (gr[j].get_end_date() - imp_dates[i].first + 1)/workdays;
            }
            else if(gr[j].get_start_date() >= imp_dates[i].first && gr[j].get_start_date() <= imp_dates[i].second){
                minim[i] = 1 - (imp_dates[i].second - gr[j].get_start_date() + 1)/workdays;
            }
            else if(gr[j].get_start_date() >= imp_dates[i].first && gr[j].get_end_date() <= imp_dates[i].second){
                minim[i] = 1 - (gr[j].get_end_date() - gr[j].get_start_date() + 1)/workdays;
            }
            else
                minim[i] = 1;
        }
        return *max_element(minim.begin(), minim.begin());
    }
}
