#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>
#include <string>
#include <vector>

int main(){
    std::string s_wishes = "12-24;56-78; 99-100";
    std::string buf = "";
    std::vector<std::pair<int, int>> wishes;
    int d1, d2;
    
	for (int i = 0; i <= s_wishes.size(); i++){
        if(s_wishes[i] == '-'){
            d1 = stoi(buf);
            buf.clear();
        }
        else if(s_wishes[i] == ';' || s_wishes[i] == '\0'){
            d2 = stoi(buf);
            wishes.push_back(std::make_pair(d1, d2));
            std::cout << "d1: " << d1 << " " << "d2: " << d2 << std::endl; 
            buf.clear();
        }
        else if(s_wishes[i] == ' '){
            continue;
        }
        else if(isdigit(s_wishes[i])){
            buf.push_back(s_wishes[i]);
            std::cout << buf << std::endl;
        }
        else{
            std::cout << "Error:Indefined symbol. Check file.\n";
        }
    }
    
    for (int i = 0; i < wishes.size(); i++){
        std::cout << wishes[i].first << ", " << wishes[i].second << std::endl;
    }
    return 0;
}