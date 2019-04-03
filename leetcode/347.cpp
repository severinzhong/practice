#include <queue>
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
using namespace std ;
typedef pair<int, int> PAIR;  
int cmp(PAIR x , PAIR y){return x.second > y.second ;}
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector <int> ans ;
        map<int , int > dict ;
        for(int i=0;i<nums.size() ; i ++) {
            if (dict[nums[i]]) dict[nums[i]] ++ ;
            else dict[nums[i]] = 1 ;
        }
        vector <PAIR> num(dict.begin() , dict.end()) ;
        sort(num.begin() , num.end() , cmp) ;
        for(int i = 0; i<k ; i++){
            ans.push_back(num[i].first) ;
        }
        return ans ;
    }
    vector<int> topKFrequent2(vector<int>& nums, int k) { // https://leetcode.com/problems/top-k-frequent-elements/discuss/249575/C%2B%2B-solution-(99)
        unordered_map<int, int> m;
        vector<int> v;
        
        for (auto i: nums)
            m[i]++;
        
        auto comp = [](const pair<int, int> &l, const pair<int, int> &r) {
            return l.second < r.second;
        };

        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)> pq(comp);

        for (auto i: m)
            pq.push(i);
        
        while (k-- > 0 && !pq.empty()) {
            v.push_back(pq.top().first);
            pq.pop();
        }

        return v;
    }
};
int main(){
    int a[] = {1,1,1,2,2,3} ;
    vector <int> nums(a,a+1) ;
    vector <int> ret = Solution().topKFrequent(nums , 1) ;
    for (int i=0;i<ret.size() ; i++) cout << ret[i] <<" " ;
    return 0 ;
}