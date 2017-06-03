class TrieNode{
public:
    TrieNode* children[26];
    bool isWord;
    TrieNode():isWord(false){
        memset(children,NULL,sizeof(TrieNode*)*26);
    }
    
};
class WordDictionary {
private:
    TrieNode* root;
public:
    /** Initialize your data structure here. */
    
    WordDictionary() {
        root = new TrieNode();
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        TrieNode* node = root;
        for(char c : word){
            if(!(node->children[c-'a'])){
                node->children[c-'a'] = new TrieNode();
            }
            node = node->children[c-'a'];
        }
        node->isWord = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return query(word.c_str(),root);
    }
    bool query(const char* word,TrieNode* node){
        for(int i=0 ; word[i] ; i++){
            if (!node)
                return false;
            if(word[i] == '.'){
                TrieNode* tmp = node;
                for(int j=0; j<26 ;j++){
                    node = tmp->children[j];
                    if(query(word+i+1,node))
                        return true;
                }
            }else{
                node = node->children[word[i]-'a'];
            }
        }
        return node&&node->isWord;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * bool param_2 = obj.search(word);
 */
