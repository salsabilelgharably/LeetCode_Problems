class Solution {
public:
    bool isPerfectSquare(int num) {
        long l =0, r=num, mid=(l+r)/2 , s=0;
        while(l<=r){
            s = mid*mid;
            if(s == num){
                return mid;
            }
            else if(s > num){
                r = mid-1;
            }
            else{
                l = mid+1;
            }
            mid = (l+r)/2;
        }
        return 0;
        
    }
};