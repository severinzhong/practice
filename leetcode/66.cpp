#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        if (digits.size()==0) {digits.insert(digits.end() , 1) ;  return digits ;}
        digits[digits.size()-1] ++ ;
        for (int i=digits.size()-1 ;i>0;i--){
            if (digits[i]>9 ){
                digits[i] = digits[i]-10 ;
                digits[i-1] ++ ;
            }
        }
        if (digits[0]>9){
            digits[0] -= 10 ;
            digits.insert(digits.begin(),1,1) ;
        }
        return digits;
    }
};
int main(){
    Solution ret ;
    int arr[] = {9,9,9} ;
    vector <int > digits(arr , arr+3) ;
    vector<int> a = ret.plusOne(digits) ;
    for (int i=0;i<a.size();i++)cout<<a[i]<<endl ;
    return 0 ;
}