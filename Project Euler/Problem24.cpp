#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    string num = "0123456789";
    int count = -1;
    bool val = true;
    while(val && count != 1000000){
        count++;
        bool val = next_permutation(num.begin(), num.end());
    }
    cout<<num;
    return 0;
}