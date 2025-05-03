def swap(lst):
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
        print(lst[i])
    return lst

lt1 = [3, 4, 5, 6]
print("Original List is:", lt1)
lt2 = swap(lt1[:]) 
print("List after swapping:", lt2)
