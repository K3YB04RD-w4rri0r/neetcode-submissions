class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ".".join([str(len(word)) for word in strs])
        return  str(len(encoding)) + "." + encoding + "".join(strs)



    def decode(self, s: str) -> List[str]:
        n_encoding = s[0]
        # print(n_encoding)
        i = 1
        while s[i] != ".":
            print(s[i])
            n_encoding += s[i]
            i += 1

        str_indexes = s[len(n_encoding) + 1:len(n_encoding) + 1 + int(n_encoding)].split(".")
        if str_indexes == [""]:
            return []
        current_index = len(n_encoding) + 1 + int(n_encoding)
        str_list = []
        for i in str_indexes:
            str_list.append(s[current_index:current_index + int(i)])
            current_index = current_index + int(i)

        return str_list


        
