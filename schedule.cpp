#include <iostream>
#include <vector>
#include "schedule.h"

Schedule::Schedule(Holiday h){
    this->gr.push_back(h);
    this->d = 0;
    this->m = 0;
}

Schedule::~Schedule(){
    gr.clear();
}

