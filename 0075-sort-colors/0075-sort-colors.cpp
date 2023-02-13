class Solution {
public:
    void sortColors(vector<int>& nums) {
        int zero=0,one=0,two=0;
        for(auto it: nums){
            if(it==0)
                zero++;
            else if(it==1)
                one++;
            else
                two++;
        }
        int i=0;
        while(zero){
            nums[i]=0;
            i++;
            zero--;
        }
        while(one){
            nums[i]=1;
            i++;
            one--;
        }
        while(two){
            nums[i]=2;
            i++;
            two--;
        }
    }
};