class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map <int, int> mp;
        int temp =0;
        for(int i=0; i<nums.size();i++){
            temp = target - nums[i];
            if(mp.find(temp) != mp.end() ){
                return {mp[temp], i};
            }
            else{
                mp[nums[i]]= i;
            }
        }
        return {0};
    }
};


