class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map <int, int> mp;
        for(int num: nums){
            if(mp.find(num) == mp.end()){
                mp[num]=1;
            }
            else{
                mp[num] +=1;
            }
        }
        for(int num: nums){
            if(mp[num] == 1){
                return num;
            }
        }
        return 0;
    }
};