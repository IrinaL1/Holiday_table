#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>
#include <string>
#include <vector>

#include "holiday.h"

Holiday::Holiday(int new_start_date, int new_end_date, int new_person){
    if (new_end_date - new_start_date > 0){
        start_date = new_start_date;
        end_date = new_end_date;
    }
    else if(new_end_date - new_start_date < 0){
        start_date = new_end_date;
        end_date = new_start_date;
    }
    else {
        printf("Error: end_date = start_date.");
    }
    v = 1;
    person = new_person;
}

int Holiday::get_start_date(){
    return start_date;
}

int Holiday::get_end_date(){
    return end_date;
}

int Holiday::get_person(){
    return person;
}

double Holiday::get_v(){
    return v;
}

void Holiday::set_v(double new_v){
    v = new_v;
}

double hol_eval_func(double w, int h_date_start, int h_date_end, int w_date_start, int w_date_end){
	if (h_date_end - h_date_start <= 0){
		std::cout << "Wrong holiday. Change start = " << h_date_start << "and end date = " << h_date_end << "or check the lenght\n";
		return -1;
	}
	if (w_date_end - w_date_start <= 0){
		std::cout << "Wrong holiday. Change start = " << w_date_start << "and end date = " << w_date_end << "or check the lenght\n";
		return -1;
	}
	if (w == 0){
		return 1;
	}
	if (w == 0.5){
		w_date_start = w_date_start - 5;
		w_date_end = w_date_end + 5;
		if (h_date_start - w_date_start >= 0 && w_date_end - h_date_end >= 0){
			return 1;
		}
		else if (h_date_end - w_date_start >= 0 && h_date_end - w_date_end <= 0){
			return (h_date_end - w_date_start + 1.0)/(h_date_end - h_date_start + 1);
		}
		else if (h_date_start - w_date_start >= 0 && h_date_start - w_date_end <= 0){
			return (w_date_end - h_date_start + 1.0)/(h_date_end - h_date_start + 1);
		}
		else{
			return 0;
		}
    }
    if (w == 1){
		if ((h_date_start - w_date_start >= 0) && (w_date_end - h_date_end >= 0)){
			return 1;
		}
		else if ((h_date_end - w_date_start >= 0) && (h_date_end - w_date_end <= 0)){
			return (h_date_end - w_date_start + 1.0)/(h_date_end - h_date_start + 1);
		}
		else if ((h_date_start - w_date_start >= 0) && (h_date_start - w_date_end <= 0)){
			return (w_date_end - h_date_start + 1.0)/(h_date_end - h_date_start + 1);
		}
		else{
			return 0;
		}
	}
	else{
		std::cout << "Wrong value of w. It must be 0, 0.5 or 1.\n";
		return -1;
	}
}

double Holiday::hol_eval(double w, std::vector<std::pair<int, int>> wishes){
	std::vector <double> v = {-1.0, -1.0, -1.0};
    if (w == 0){
        return 1;
    }
	if (wishes.size() == 0){
		return 1;
	}
	else { 
		for (int i = 0; i < wishes.size(); i++){
			v[i] = hol_eval_func(w, this->start_date, this->end_date, wishes[i].first, wishes[i].second);
		}
	}
	return *max_element(v.begin(), v.end());
}


extern "C" Holiday * create_H(int new_start_date, int new_end_date, int new_person){

	return new Holiday(new_start_date, new_end_date, new_person);
}

extern "C"{
	int get_start_date(Holiday* H){
    	return H->get_start_date();
	};

	int get_end_date(Holiday* H){
    	return H->get_end_date();
	};

	int get_person(Holiday* H){
    	return H->get_person();
	};

	double get_v(Holiday* H){
    	return H->get_v();
	};
    
    void set_v(Holiday *H, double new_v){
        H->set_v(new_v);     
    };

        

	double hol_eval(Holiday* H, double w, char * c_wishes){
		std::string s_wishes = c_wishes;
		std::vector<std::pair<int, int>> wishes;
		std::string buf = "";
		int d1, d2;
		
		if (s_wishes.size() == 0) return H->hol_eval(w, wishes);
		for (int i = 0; i <= s_wishes.size(); i++){
        if(s_wishes[i] == '-'){
            d1 = stoi(buf);
            buf.clear();
        }
        else if(s_wishes[i] == ';' || s_wishes[i] == '\0'){
            d2 = stoi(buf);
            wishes.push_back(std::make_pair(d1, d2));
            buf.clear();
        }
        else if(s_wishes[i] == ' '){
            continue;
        }
        else if(isdigit(s_wishes[i])){
            buf.push_back(s_wishes[i]);
        }
        else{
            std::cout << "Error:Indefined symbol. Check file.\n";
        }
    }
	
	return H->hol_eval(w, wishes);
	};
}

