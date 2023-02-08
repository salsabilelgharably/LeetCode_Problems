class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        for(string opration : operations){
            if(opration[1] == '+'){
                x++;
            }
            else{
                x--;
            }
        }
        return x;
        
    }
};