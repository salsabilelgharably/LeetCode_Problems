class Solution {
public:
    bool isPalindrome(string s) {
        string newS= "";
        for(char i: s){
            if(isalnum(i)){
                newS += tolower(i);
            }
        }
        int sizeOfS= newS.size();
        for(int i= 0; i< newS.size()/2  ; i++){
            sizeOfS--;
            if(newS[i] != newS[sizeOfS]){
                return false;
            }
        }
        return true;
    }
};