class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int sum =0, secondary = mat.size()-1, primary =0;
        for(int row =0; row<mat.size(); row++){
            if(primary==secondary){
                sum += mat[row][primary];
            }else{
                sum += mat[row][primary]+mat[row][secondary] ;
            }
            primary++;
            secondary--;
        }
        return sum;
    }
};