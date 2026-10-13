class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num): return "0"
        remove_list = []
        stack = []
        for i in range(len(num)):
            while stack and num[stack[-1]] > num[i]:
                remove_list.append(stack.pop())
            stack.append(i)

        num = list(num)
        for i in remove_list:
            num[i] = "r"
            k -= 1
            if k == 0: break

        num = "".join(num).replace("r", "")
        if k: num = num[:len(num) - k]

        for start_index in range(len(num)):
            if num[start_index] != "0": break

        return num[start_index:]