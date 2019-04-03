#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std ;
typedef pair<char, int> PAIR;  
int cmp(PAIR x, PAIR y)//针对PAIR的比较函数
{  
    return x.second > y.second;  //从大到小
} 
class Solution {
public: 
    string frequencySort(string s) {
        int a[26],A[26] ;
        string ans = "" ;
        memset(a , 0 ,sizeof(a)) ;
        memset(A , 0 ,sizeof(A)) ;
        map <char , int> dict ;
        for (int i = 0 ; i < s.size() ; i ++) {
            if (dict[s[i]])  dict[s[i]]++ ;
            else dict[s[i]] = 1 ;
        }

        vector <PAIR> l(dict.begin() ,dict.end()) ;
        sort(l.begin() , l.end() ,cmp) ;
        for(vector<PAIR>::iterator it = l.begin();it!=l.end();it ++){
            int t = it->second ;
            char c = it->first ;
            for (int i=0;i<t;i++) ans += c ; 
        }
        return ans ;
    }
};
int main(){
    cout << Solution().frequencySort("tree") <<endl ;
    return 0 ;
}