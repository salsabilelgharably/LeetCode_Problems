class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int j =1,i=0, n = nums.size();
        while(j<n){
            if(nums[i] ==0 && nums[j] != 0) {
                nums[i] = nums[j];
                nums[j] =0;
                i++;
                j++;
            }
            else if(nums[i] == 0 && nums[j]==0){
                j++;
            }
            else{
                j++;
                i++;
            }
        }
    }
};