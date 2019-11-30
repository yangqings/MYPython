#带刷新的文本进度条
import time
scale = 50

#字符串的 .center处理方法
print("执行开始".center(scale//2,'-'))

#计时  适用于各种需要计时的应用
start = time.perf_counter()
for i in range(scale+1):
    a = '*'*i
    b = '.'*(scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start

    #/r实现光标向行首的移动 end参数赋值为空字符串 每次输出后不换行
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))
