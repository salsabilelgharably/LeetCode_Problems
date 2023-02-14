class Solution {
public:
    void sortColors(vector<int>& nums) {
        bool isswapped= true;
        int temp=0;
        while(isswapped){
            isswapped= false;
            for(int i=0; i< nums.size()-1; i++){
                if(nums[i]>nums[i+1]){
                    temp = nums[i];
                    nums[i]= nums[i+1];
                    nums[i+1] = temp;
                    isswapped=true;
                }
        
            }
        }
        
    }
};