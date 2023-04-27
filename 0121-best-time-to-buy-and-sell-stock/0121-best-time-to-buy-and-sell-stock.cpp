class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0, right = 1,mx =0;
        
        while(right< prices.size()){
            if(prices[left] > prices[right]){
                left = right;
            }
            else{
                mx = max(mx, prices[right]- prices[left]);
            }
            right ++;
        }
        return mx;
        
    }
};