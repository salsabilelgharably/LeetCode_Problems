// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long left =1;
        long right =n;
        long mid=(left+right)/2;
        while(left<=right){
            mid=(right+left)/2;
            if(isBadVersion(mid) && !isBadVersion(mid-1)){
                return mid;
            }
            else if(!isBadVersion(mid) && isBadVersion(mid+1)){
                return mid+1;
            }
            else if(isBadVersion(mid)){
                right =mid-1;
            }
            else{
                left = mid+1;
            }
            

        }
        return mid;
    }
};

