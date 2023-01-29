class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char,char>m1;
        map<char,char>m2;
        
        for(int i =0; i < s.size(); i++){
            if(m1[s[i]]&&m1[s[i]]!= t[i] || m2[t[i]]&&m2[t[i]]!= s[i] ){
                return false;
            }
            m1[s[i]]= t[i];
            m2[t[i]]= s[i];
        }
        return true;
        
    }
};