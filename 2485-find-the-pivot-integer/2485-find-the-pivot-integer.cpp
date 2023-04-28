class Solution {
public:
    int pivotInteger(int n) {
        int sumOfN = n*(n+1)/2, currentSum= 0;
        for(int i =1; i <= n; i++){
            currentSum += i;
            if(currentSum == sumOfN - currentSum + i){
                return i;
            }
        }
        return -1;
    }
};