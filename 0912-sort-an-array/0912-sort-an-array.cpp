class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        vector<int>ans;
        priority_queue<int,vector<int>,greater<int>>maxi;

        for(int i=0;i<nums.size();i++){
            maxi.push(nums[i]);
        }
        // after heapify we get an sorted array ; 
        while(!maxi.empty()){
            ans.push_back(maxi.top());
            maxi.pop();
        }
        return ans;
       
    }
};