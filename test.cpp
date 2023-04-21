#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>
#include <string>
#include <vector>

int main(){
    char s_wishes[] = "12-24;56-78;99-100";
    std::vector<std::pair<int, int>> wishes;
    int d1, d2;
	char* buf = strtok(s_wishes, " -;");
		while (buf != NULL){
            char* buf1 = strtok(NULL, "-");
            d1 = std::stoi(buf);
            d2 = std::stoi(buf1);
			wishes.push_back(std::make_pair(d1, d2));
		}
    for (int i = 0; i < wishes.size(); i++){
        printf("%d %d\n", wishes[i].first, wishes[i].second);
    }
    return 0;
}