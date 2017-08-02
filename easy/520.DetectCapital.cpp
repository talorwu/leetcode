class Solution {
public:
    bool detectCapitalUse(string word) {
        if(word.length() == 0)
            return true;
        if(word[0] > 90){
            for( int i=1;i<word.length();i++){
                if(word[i] <= 90)
                    return false;
            }
        }else{
            if(word.length() == 1)
                return true;
            if(word[1] <= 90){
                for(int i=2;i<word.length();i++)
                    if(word[i] > 90)
                        return false;
                
            }else
                for(int i=2;i<word.length();i++)
                    if(word[i] <= 90)
                        return false;
        }
        return true;
    }
};
