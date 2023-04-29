class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        if ( nums.size() == 0 )
            return 0; // We do not actaully need this condition cause that Constraints say that
                      // the size of the array must be more that 1 and less than 3 * 10^4
                      // but I put it anyways
        
        int index = 1;
        
        for ( int i = 1, len = nums.size(); i < len; i++ ) {
            if ( nums[ i ] != nums[ i-1 ]){
                nums[ index ++ ] = nums[ i ];
            }
        }
        
        return index;
    }
};