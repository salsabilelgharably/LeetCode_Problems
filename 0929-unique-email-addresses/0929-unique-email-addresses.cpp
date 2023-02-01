class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        int res =0;
        map<string,bool>mp;
        string temp= "";
        for(string email: emails){
            temp="";
            for(char c: email){
                if(c == '.'){
                    continue;
                }
                else if(c == '+' || c=='@'){
                    break;
                }
                
                else{
                    temp += c;
                }
            }
            
            temp += email.substr(email.find('@'), email.size()-1);
            
            if(!mp[temp]){
                res +=1;
                mp[temp] = true;
            }
            
        }
        return res;
        
    }
};