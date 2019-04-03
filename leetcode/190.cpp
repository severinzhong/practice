#include <iostream>
using namespace std ;
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
            uint32_t ans = 0;
            int p = 31 ;
            while(p>=0){
                ans = ans | ((n&1)<<p) ;
                p -- ;
                n= n>>1 ;
            }
            return ans ;
    }
};
int main(){
    Solution ret ;
    uint32_t a = 1001;
    cout<<ret.reverseBits(a)<<endl ;
    return 0 ;
}