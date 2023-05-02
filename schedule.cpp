#include <iostream>
#include <vector>
#include <algorithm> 

#include "schedule.h"
#include "holiday.h"

Schedule::Schedule(Holiday h){
    this->gr.push_back(h);
    this->d = 0;
    this->m = 0;
    this->cost = 0;
}

Schedule::~Schedule(){
    gr.clear();
}

Holiday* Schedule::get_h(int i){
    return &(this->gr[i]);
}

void Schedule::del(int i){
    this->gr.erase(this->gr.begin() + i);
}

int Schedule::length(){
    return gr.size();
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
    std::vector<int> real_hol(12, 0);   //массив реальных трудодней с учетом отпусков работников 
    std::vector<double> hol_per(12, 0);  //не знаю, как лучше назвать. Отношение дыха к возможной полной работе
    std::vector<int>::iterator it1, it2;
    double min_h, max_h;
    for(int i = 0; i < calendar.size(); i++){
        all_works[i] = emp * calendar[i].size();
    }
    for(int i = 0; i < calendar.size(); i++){
        for(int j = 0; j < this->gr.size(); j++){
            it1 = find(calendar[i].begin(), calendar[i].end(), this->gr[j].get_start_date());
            if(it1 != calendar[i].end()){
                it2 = find(calendar[i].begin(), calendar[i].end(), this->gr[j].get_end_date());
                if(it2 != calendar[i].end()){
                    real_hol[i] += it2 - it1 + 1;
                }
                else{
                    real_hol[i] += it2 - it1;
                }
            }
            else{
                it2 = find(calendar[i].begin(), calendar[i].end(), this->gr[j].get_end_date());
                if(it2 != calendar[i].end()){
                    real_hol[i] += it2 - calendar[i].begin() + 1;
                }
            }
        }
    }
    //считаем отношение отдыходней ко всем возможным рабочим дням
    for(int i = 0; i < hol_per.size(); i++){
        hol_per[i] = static_cast<double>(real_hol[i])/static_cast<double>(all_works[i]);
    }
    //нужно,чтобы разница между днями отдыха (работы) в каждый месяц была минимальной
    min_h = *min_element(hol_per.begin(), hol_per.end());
    max_h = *max_element(hol_per.begin(), hol_per.end());
    return (1 - (max_h - min_h));
}

//На вход подаются важные даты со включением обеих границ (нач. дата, кон. дата), число сотрудников
double Schedule::calc_min(std::vector<std::pair<int, int>> imp_dates, int emp){
    if(imp_dates.size() == 0){
        printf("Список важных дат пуст\n");
        return 1;
    }

    std::vector <int> all_works(imp_dates.size(), 0);
    std::vector <int> real_hol(imp_dates.size(), 0);
    std::vector <double> hol_per(imp_dates.size(), 0);

    for(int i = 0; i < imp_dates.size(); i++){
        all_works[i] = emp * (imp_dates[i].second - imp_dates[i].first + 1);
        for(int j = 0; j < gr.size(); j++){
            if(gr[j].get_start_date() >= imp_dates[i].first && gr[j].get_end_date() <= imp_dates[i].second){
                real_hol[i] += gr[j].get_end_date() - gr[j].get_start_date();
            }  
            else if(gr[j].get_end_date() >= imp_dates[i].first && gr[j].get_end_date() <= imp_dates[i].second){
                real_hol[i] += gr[j].get_end_date() - imp_dates[i].first + 1;
            }
            else if(gr[j].get_start_date() >= imp_dates[i].first && gr[j].get_start_date() <= imp_dates[i].second){
                real_hol[i] += imp_dates[i].second - gr[j].get_start_date() + 1;
            }
        }
    }

    //real_hol - считаем отдыходни. Чем меньше отдыходней, тем лучше.
    for(int i = 0; i < imp_dates.size(); i++){
        hol_per[i] = static_cast<double>(real_hol[i])/static_cast<double>(all_works[i]);
    }
    return 1 - *max_element(hol_per.begin(), hol_per.end());
}

extern "C" Schedule * create_S(Holiday* h){
	return new Schedule(*h);
}

extern "C"{
    Holiday* get_h (Schedule* S, int i){
        return S->get_h(i);
    };

    int length(Schedule* S){
        return S->length();
    };

    void delit(Schedule* S, int i){
        S->del(i);
    }

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

    void set_hol(Schedule* S, Holiday *h){
        S->set_hol(*h);
    };

    double calc_distr(Schedule* S, char* s_cal, int emp){
        std::string a = s_cal;
        std:: string b;
        int bf;
        std::vector<std::vector<int>> calendar;
        std::vector<int> month;
        for(int i = 0; i <= a.size(); i++){
            if(a[i] != ' ' and a[i] != '\0'){
                b += a[i];
            }
            else{
                bf = stoi(b);
                b = "";
                if (bf != 0){
                    month.push_back(bf);
                }
                else{
                    calendar.push_back(month);
                    month.clear();
                }
            }
        };
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