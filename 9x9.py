for i in range(1, 10): # i循环1~~9
  for j in range(1, i+1): # j循环1~~(i-1)
    print ("%d*%d=%d" % (i, j, i*j),end=" ") # 输出乘法表 end=“” 空格
  print('') # 换行