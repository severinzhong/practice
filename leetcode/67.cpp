#include <iostream>
#include <string>
using namespace std ;
class Solution {
public:
    string addBinary(string a, string b) {
        string ans = "";
        int la = a.size() - 1 , lb = b.size() - 1 , f = 0 ;
        while (la>=0 || lb>=0){
            int i=0,j=0 ;
            if (la>=0) {
                i = a[la]-'0' ;
                la -- ;
            }
            if (lb>=0) {
                j = b[lb]-'0' ;
                lb -- ;
            }
            f += i + j ;
            switch (f)
            {
                case 0 :
                    ans = '0' + ans;
                    break;
                case 1:
                    ans = '1' + ans;
                    f = 0 ;
                    break;
                case 2 :
                    ans = '0' + ans ;
                    f = 1 ;
                    break ;
                case 3 :
                    ans = '1' + ans;
                    f = 1 ;
                default:
                    break;
            } 
        }
        if (f>0) ans = '1' + ans;

        return ans ;
    }
};
int main(){
    string a = "11" ;
    string b = "1" ;
    Solution ret ;
    cout << a<<endl<<b<<endl<<ret.addBinary(a,b) <<endl ;
    return 0 ;
}