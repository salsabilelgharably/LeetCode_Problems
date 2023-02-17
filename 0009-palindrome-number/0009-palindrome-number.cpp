class Solution {
public:
    bool isPalindrome(int x) {
        string newx =to_string(x);
        int n = newx.size();
        for(int i =0; i < newx.size()/2; i++){
            n--;
            if(newx[i] != newx[n] ){
                return false;
            }
        }
        return true;
        
    }
};