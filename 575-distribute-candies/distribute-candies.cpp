class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        set<int> newset(candyType.begin(),candyType.end());
        int s = newset.size();
        int n = candyType.size() / 2;

        return min(s,n);
        
    }
};