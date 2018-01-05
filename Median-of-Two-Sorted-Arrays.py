class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        result_list = []
        while(nums1 or nums2):
            if len(nums1)==0 and len(nums2)!=0:
                for num in nums2:
                    result_list.append(num)
                nums2 = []
            elif len(nums2)==0 and len(nums1)!=0:
                for num in nums1:
                    result_list.append(num)
                nums1 = []
            elif nums1[0] > nums2[0]:
                result_list.append(nums2[0])
                nums2.pop(0)
            elif nums1[0] < nums2[0]:
                result_list.append(nums1[0])
                nums1.pop(0)
            else:
                result_list.append(nums1[0])
                result_list.append(nums2[0])
                nums1.pop(0)
                nums2.pop(0)

        result = float(0)
        if len(result_list)%2==0:
            m_index = len(result_list)/2
            result = float(result_list[m_index-1]+result_list[m_index])/2
        else:
            m_index = len(result_list)/2
            result = float(result_list[m_index])
        return result




