#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
int checkAbundant(int num){
    int tot = 1;
    for(int i = 2; i< num/2 + 1; i++)
        if(num%i) continue;
        else tot+=i;
    if(tot>num) return 1;
    return 0;
}
int main(){
    int i;
    long int sum = 28123*28124/2;
    unordered_map<int, int> checked;
    vector<int> v;
    for(i=12; i<=28123; i++)
        if(checkAbundant(i)) v.push_back(i);   
    for(auto i = v.begin(); i!=v.end()-1; i++)
        for(auto j = i; j!=v.end(); j++)
            if(checked.find(*j+*i)==checked.end() && *j+*i<=28123){
                checked[*i+*j] = 1;
                sum-=(*i+*j);
            }
    cout<<sum;
}