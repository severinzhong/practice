#include <iostream>
#include <vector>
using namespace std ;
class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int ret = 0 ;
        sort(timeSeries.begin() , timeSeries.end()) ;
        for (int i=1 ; i < timeSeries.size() ; i ++){
            if (timeSeries[i]-timeSeries[i-1]>=duration){
                ret += duration ;
            }else{
                ret += timeSeries[i]-timeSeries[i-1];
            }
        }
        return timeSeries.size()?ret+duration:ret ;
    }
};
int main(){
    int a[] = {1,2};
    vector<int> timeSeries(a , a+2) ;
    cout << Solution().findPoisonedDuration(timeSeries,2)<<endl ;
    return 0 ;
}
