class Solution {
public:
    bool isThree(int n) {
        int divisor = 0;
        for(int i= 1; i <n+1; i++){
            if(n%i == 0){
                ++divisor;
            }
        }
        return divisor == 3;
        
    }
};