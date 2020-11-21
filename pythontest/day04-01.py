# 循环语句 range()
# range(11) =(0,1,2,3,4,5,6,7,8,9,10)

# 通过下标遍历元素/元组
# b = ["a","a","a","a","a","a","a","a","a","a","b"]
# b = ("a","a","a","a","a","a","a","a","a","b","b")
# for i in range(len(b)):
#     #print(i)
#     print(b[i])

# b = ["as","sh","hdjhd","12","d"]
# for i in b:
#     if "as" == i:
        
#         # continue        # 跳过循环
#         break             # 终止循环
#         print("12")
#     else:
#         print(i)



for i in range(1,10):         # 总共9条数据(1,2,3,4,5,6,7,8,9)
    for j in range(1, i+1):   # (1,2,3,4,5,6,7,8,9)
        print('{} x {} = {} \t'.format( j , i , i*j ) , end ="")
    print("")


