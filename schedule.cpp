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

void Schedule::set_hol(Holiday h){
    this->gr.push_back(h);
}

//На вход подается массив рабочих дней согласно календарю и число сотрудников
double Schedule::calc_distr(std::vector<std::vector<int>> calendar, int emp){
    std::vector<int> all_works(12, 0);    //массив трудодней с учётом кол-ва работников
    std::vector<int> real_works(12, 0);   //массив реальных трудодней с учетом отпусков работников 
    std::vector<double> work_per(12, 0);  //не знаю, как лучше назвать. Отношение полезной работы к возможной работе
    std::vector<int>::iterator it1, it2;
    double min_w, max_w;
    for(int i = 0; i < calendar.size(); i++){
        all_works[i] = emp * calendar[i].size();
    }
    for(int i = 0; i < calendar.size(); i++){
        for(int j = 0; j < this->gr.size(); j++){
            it1 = find(calendar[i].begin(), calendar[i].end(), this->gr[j].get_start_date());
            if(it1 != calendar[i].end()){
                it2 = find(calendar[i].begin(), calendar[i].end(), this->gr[j].get_end_date());
                if(it2 != calendar[i].end()){
                    real_works[i] += it2 - it1 + 1;
                }
                else{
                    real_works[i] += it2 - it1;
                }
            }
            else{
                it2 = find(calendar[i].begin(), calendar[i].end(), this->gr[j].get_end_date());
                if(it2 != calendar[i].end()){
                    real_works[i] += it2 - calendar[i].begin() + 1;
                }
            }
        }
    }
    for(int i = 0; i < work_per.size(); i++){
        work_per[i] = static_cast<double>(real_works[i])/static_cast<double>(all_works[i]);
    }
    min_w = *min_element(work_per.begin(), work_per.begin());
    max_w = *max_element(work_per.begin(), work_per.begin());
    return (1 - (max_w - min_w));
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
                minim.push_back(1 - (gr[j].get_end_date() - imp_dates[i].first + 1)/workdays);
            }
            else if(gr[j].get_start_date() >= imp_dates[i].first && gr[j].get_start_date() <= imp_dates[i].second){
                minim.push_back(1 - (imp_dates[i].second - gr[j].get_start_date() + 1)/workdays);
            }
            else if(gr[j].get_start_date() >= imp_dates[i].first && gr[j].get_end_date() <= imp_dates[i].second){
                minim.push_back(1 - (gr[j].get_end_date() - gr[j].get_start_date() + 1)/workdays);
            }
            else
                minim.push_back(1);
        }
    }
    return *max_element(minim.begin(), minim.end());
}

extern "C" Schedule * create_S(Holiday* h){
	return new Schedule(*h);
}

extern "C"{
	int get_gr_destr(Schedule* S){
    	return S->get_gr_destr();
	};

	int get_gr_min(Schedule* S){
    	return S->get_gr_min();
	};

	int get_gr_cost(Schedule* S){
    	return S->get_gr_cost();
	};

    void set_gr_destr(Schedule* S, double new_d){
        S->set_gr_destr(new_d);
    };

    void set_gr_min(Schedule* S, double new_m){
        S->set_gr_min(new_m);
    };

    void set_gr_cost(Schedule* S, double new_cost){
        S->set_gr_cost(new_cost);
    };

    void set_hol(Schedule* S, Holiday h){
        S->set_hol(h);
    };

    double calc_distr(Schedule* S, std::vector<std::vector<int>> calendar, int emp){
        return S->calc_distr(calendar, emp);
    }

	double calc_min(Schedule* S, char* c_imp_dates, int emp){
        std::string s_imp_dates = c_imp_dates;
        std::vector<std::pair<int, int>> imp_dates;
		std::string buf = "";
		int d1, d2;

        if (s_imp_dates.size() == 0) return S->calc_min(imp_dates, emp);
		
		for (int i = 0; i <= s_imp_dates.size(); i++){
            if(s_imp_dates[i] == '-'){
                d1 = stoi(buf);
                buf.clear();
            }
            else if(s_imp_dates[i] == ';' || s_imp_dates[i] == '\0'){
                d2 = stoi(buf);
                imp_dates.push_back(std::make_pair(d1, d2));
                buf.clear();
            }
            else if(s_imp_dates[i] == ' '){
                continue;
            }
            else if(isdigit(s_imp_dates[i])){
                buf.push_back(s_imp_dates[i]);
            }
            else{
                std::cout << "Error:Indefined symbol. Check file.\n";
            }
        }
        
        return S->calc_min(imp_dates, emp);
    }
}