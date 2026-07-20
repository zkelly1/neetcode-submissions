class Solution:
    import collections 
    def isAnagram(self, s: str, t: str) -> bool:
        c_s: collections.Counter = Counter(s)
        c_t: collections.Counter = Counter(t)
        
        # if all keys in s are in t and their frequency is the same 
        # as in t and vice versa
        return (all(k_s in c_t and v_s == c_t[k_s] for k_s, v_s in c_s.items())) and (all(k_t in c_s and v_t == c_s[k_t] for k_t, v_t in c_t.items()))