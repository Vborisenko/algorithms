class Solution1:
    def decodeString(self, s: str) -> str:
        """
        To collect the result string we will use the list object called result_s_list

        1) We can iterate through the loop and extend current last element of result_s_list untill:

            a) We get the digit. In this case we can normalise the digit
            into the integer and add to the k_stack
            Based on the description the next element is "[".
            So we have to add emty string to our result_s_list as a nested object

            b) We get the "]". Then we have to get last element in result_s_list and
            get the product of last element of k_stack
        """

        k_stack = []
        s_stack = []

        current_k = ""
        current_s = ""
        i = 0

        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    current_k += s[i]
                    i += 1
                continue

            if s[i] == "[":
                k_stack.append(int(current_k))
                s_stack.append(current_s)
                current_k = ""
                current_s = ""

            elif s[i] == "]":
                last_k = k_stack.pop()
                prev_s = s_stack.pop()
                current_s = prev_s + current_s * last_k
            else:
                current_s += s[i]

            i += 1

        return current_s


class Solution:
    def decodeString(self, s: str) -> str:
        k_stack = []
        s_stack = []
        current_k = ""
        current_s = ""
        i = 0

        while i < len(s):
            if s[i].isdigit():
                while s[i].isdigit():
                    current_k += s[i]
                    i += 1
                continue
            elif s[i] == "[":
                k_stack.append(int(current_k))
                s_stack.append(current_s)
                current_k = ""
                current_s = ""
                i += 1
            elif s[i] == "]":
                last_k = k_stack.pop()
                prev_s = s_stack.pop()
                current_s = prev_s + current_s * last_k
                i += 1
            else:
                current_s += s[i]
            i += 1

        return current_s


if __name__ == "__main__":
    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    Solution().decodeString(s)
