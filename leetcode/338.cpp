#include <iostream>
#include <vector>
using namespace std ;
class Solution {
public:
    vector<int> countBits(int num) {
        vector <int> ret(num+1 , 0) ;
        for (int i = 1 ; i<=num ;i ++){
            if (ret[i]) continue ;
            ret[i] = ret[i-1] + 1 ;
            int j = i<<1 ;
            while (j<=num){
                ret[j] = ret[i] ;
                j <<= 1 ;
            }
        }
        return ret ;
    }
};
int main(){
    vector<int> ans =  Solution().countBits(5);
    for (int i=0 ; i<ans.size() ; i++)
        cout << ans[i] << " " ;
    return 0 ;
}