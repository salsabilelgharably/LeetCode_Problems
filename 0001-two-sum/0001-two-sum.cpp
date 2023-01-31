class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int>mp;
        for(int i=0; i < nums.size(); i++)
        {
            int temp=target-nums[i];
            if(mp.find(temp)!=mp.end())
            {
                return vector<int>{i,mp[temp]};
            }
            mp[nums[i]]=i;
        }
        return vector<int>{-1,-1};
    }
    
};