#include <iostream>
using namespace std ;
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0 ;
        while  (n){
            n -= n&(-n) ;
            cnt ++ ;
            }
        return cnt ;
    }
};
int main(){
    cout <<Solution().hammingWeight(7)<<endl ;
    return 0 ;
}