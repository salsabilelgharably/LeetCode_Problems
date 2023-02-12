bool com(int a,int b){
    return a>b;
}
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        sort(nums.begin(), nums.end(), com);
        int prev = nums[0];
        int c = 1;
        for(int i =1; i < nums.size(); i++){
            if(nums[i] != prev){
                c++;
                prev = nums[i];
            }
            if(c==3){
                return prev;
            }   
        }
        return nums[0];
    }
};