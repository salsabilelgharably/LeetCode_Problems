class Solution {
public:
    int vowelStrings(vector<string>& words, int left, int right) {
        string vow = "aeiou";
        int count = 0;
        for(int i= left; i<=right;i++)
        {
            int wordlen = words[i].size()-1;
            if(vow.find(words[i][0]) != string::npos && vow.find(words[i][wordlen]) != string::npos)
                count++;
        }
        return count;
    }
};