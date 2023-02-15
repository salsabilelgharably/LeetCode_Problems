class Solution {
public:
    void reverseString(vector<char>& s) {
        char temp =' ';
        int sizeOfS =s.size();
        for(int i =0; i< s.size()/2; i++){
            sizeOfS--;
            temp = s[sizeOfS];
            s[sizeOfS] = s[i];
            s[i] = temp;
        }
        
    }
};