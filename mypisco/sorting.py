def bubble_sort(items):
   for passnum in range(len(items)-1,0,-1):
       for i in range(passnum):
           if items[i]>items[i+1]:
               temp = items[i]
               items[i] = items[i+1]
               items[i+1] = temp
   return items

def merge_sort(items):
    def merge_sort(items):
        len_i = len(items)

        if len_i == 1:
            return items
 
        mid_point = int(len_i / 2)
        
        i1 = merge_sort(items[:mid_point])
        i2 = merge_sort(items[mid_point:])

        return merge(i1, i2)

    def merge(A, B):
        new_list = []
        while len(A) > 0 and len(B) > 0:
            if A[0] < B[0]:
                new_list.append(A[0])
                A.pop(0)
            else:
                new_list.append(B[0])
                B.pop(0)

        if len(A) == 0:
            new_list = new_list + B
        if len(B) == 0:
            new_list = new_list + A

        return new_list
    return merge_sort(items)


def quick_sort(items):

   if len(items) == 2:
       if items[0] > items[1]:
           return [items[1], items[0]]
       else:
           return items
   else:
       pivot_val = items[0]
       left_list = []
       right_list = []
       equal_list = []

       for idx in range(len(items)):
           if items[idx] == pivot_val:
               equal_list.append(items[idx])
           elif items[idx] < pivot_val:
               left_list.append(items[idx])
           else:
               right_list.append(items[idx])

       if len(left_list) > 1:
           left_list = quick_sort(left_list)
       if len(right_list) > 1:
           right_list = quick_sort(right_list)

       return_list = left_list + equal_list + right_list

   return return_list