class Solution:
    @staticmethod
    def productExceptSelf(nums: list[int]) -> list[int]:
        product_of_all_nums_elements = 1
        unzero_product_of_all_nums_elements = 1
        zero_count = 0
        result = []

        if not nums:
            return nums

        for element in nums:
            if element == 0:
                zero_count += 1
            else:
                unzero_product_of_all_nums_elements *= element
            product_of_all_nums_elements *= element

        for element in nums:
            if zero_count > 1:
                return [0 for i in nums]

            if zero_count == 0:
                return [int(product_of_all_nums_elements / element) for element in nums]

            if element == 0:
                result.append(unzero_product_of_all_nums_elements)
            else:
                result.append(0)

        return result


if __name__ == '__main__':
    nums = input()
    print(Solution.productExceptSelf(nums=nums))
