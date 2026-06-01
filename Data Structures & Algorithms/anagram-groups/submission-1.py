class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = []
        for word in strs:
            is_seen = False
            word_set = sorted(word)
            for set_indexes in range(len(groups)):
                if sorted(groups[set_indexes][0]) == word_set:
                    is_seen = True
                    groups[set_indexes].append(word)
                    break
            if not is_seen:
                groups.append([word])

        return sorted(groups, key=len)

            

        