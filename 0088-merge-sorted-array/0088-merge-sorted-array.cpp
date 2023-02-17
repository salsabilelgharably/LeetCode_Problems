class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> newArr;
        int i = 0,j = 0;
        while(i < m and j < n){
            if(nums1[i] <= nums2[j]){
                newArr.push_back(nums1[i]);
                i++;
            }else{
                newArr.push_back(nums2[j]);
                j++;
            }
        }
        while(i < m){
            newArr.push_back(nums1[i]);
            i++;
        }
        while(j < n){
            newArr.push_back(nums2[j]);
            j++;
        }
        nums1 = newArr;
    }
};