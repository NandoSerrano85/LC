
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 2 and nums[0]+nums[1] == target:
            return [0,1]
        elif len(nums) > 2:
            result = dict()
            for n in range(0,len(nums)):
                comp = target - nums[n]
                if comp in result:
                    return [result[comp], n]
                result[nums[n]] = n
            print(result)
        else:
            return "no sums"


def main():
    nums = [1,2,7,11,15]
    target = 9

    print(twoSum(nums,target))
    nums = [3,2,4]
    target = 6

    print(twoSum(nums,target))
    nums = [3,2,3]
    target = 6

    print(twoSum(nums,target))

main()



# optimal = list()
#         results = list()
#         for n in range(0,len(nums)):
#             if nums[n] < target:
#                 optimal.append(nums[n])
#                 results.append(n)
#             if len(optimal) == 2:
#                 if optimal.sum() == target:
#                     return results


# num1 = 0
#         num2 = 0
#         results = list()
#         if len(nums) == 2:
#             return [0,1]
#         else:
#             for n in range(0,len(nums)):
#                 if nums[n] < target:
#                     if num1 == 0:
#                         num1 = nums[n]
#                         results.append(n)
#                     else:
#                         num2 = nums[n]
#                         results.append(n)
#                 if num1+num2 == target:
#                     return results
#                 elif num1 != 0 and num2 != 0:
#                     num1 = num2
#                     num2 = 0
#                     del results[0]