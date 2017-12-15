def jinwei(M,K):
    m = ord(M)
    if m > 65 and m <= 82 or m > 96 and m <= 122:
        m = 97 + ((m - 97) + K )% 26  #循环
    else:
        print("输入错误!")
        main()
    return chr(m)

def jiami(M,K):
    string = ''
    for i in M:
        string += jinwei(i,K)
    print("加密字符为："+string)
    return string

def main():
    M = input('请输入明文字符M：')
    K = int(input('请输入密钥K：'))
    jiami(M,K)
    print("重来请按1")
    print("退出请按2")
    choice=input()
    if choice=='1':
        main()
    if choice=='2':
        exit()
    
if __name__ == '__main__':
    main()