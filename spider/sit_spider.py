#coding=utf-8
import requests
# import itertools
from lxml import etree
from MySQLdb import *

# student_list = []

def add_to_mysql(nost_list):
    # try:
    conn = connect(host = 'localhost', port = 3306, user = 'root', passwd = '13671958740', db = 'python', charset = 'utf8')
    cursorl = conn.cursor()
    sql = "insert into sit(name, id, gender, nation, birthday, place, status, identity, home, postcode, college, major) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursorl.execute(sql, [nost_list[0].encode("utf-8"), nost_list[1].encode("utf-8"), nost_list[2].encode("utf-8"), nost_list[3].encode("utf-8"), nost_list[4].encode("utf-8"), nost_list[5].encode("utf-8"), nost_list[6].encode("utf-8"), nost_list[7].encode("utf-8"), nost_list[8].encode("utf-8"), nost_list[9].encode("utf-8"), nost_list[10].encode("utf-8"), nost_list[11].encode("utf-8")])
    conn.commit()
    cursorl.close()
    conn.close()
    # except Exception, e:
    #     print("e.massage")
            

def main(user, password):
    # words = "1234567890"
    # passwd = itertools.product(words, repeat = 6)
    # with open("sit.txt", "a") as dic:
    #     for word in passwd:
    #         dic.write("".join(word))
    #         dic.write("\n")
    # lines = open("sit.txt", "r") 
    # for password in lines:
    sess = requests.session()
    url = "http://my.sit.edu.cn/userPasswordValidate.portal"
    headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/58.0"}
    data = {
        "Login.Token1" : user,
        "Login.Token2" : password,
        "goto" : "http://my.sit.edu.cn/loginSuccess.portal",
        "gotoOnFail" : "http://my.sit.edu.cn/loginFailure.portal"
    }
    response = sess.post(url, headers = headers, data = data)
    # print(response.text)  
    a = len(response.cookies)
    if a == 1:
        print("Login Success")
        url1 = "http://ems.sit.edu.cn:85/student/left.jsp"
        url2 = "http://ems.sit.edu.cn:85/student/card.jsp"
        content1 = sess.get(url1, headers = headers).text
        content2 = sess.get(url2, headers = headers).text
        #print(content2)
        HTML_content = etree.HTML(content2)
        nost_list = HTML_content.xpath('//td[@style="padding-left:10px;"]/text()')
        picture_list = HTML_content.xpath('//img/@src')
        print(picture_list)
        # print(nost_list[0].encode('utf-8'))
        # i=0
        # for a in nost_list:
            # print(str(i) + a.encode("utf-8"))
            # student_list.append(c)
            # i+=1
        add_to_mysql(nost_list)            
    else:
        print("Password Error")   


if __name__ == "__main__":
    user = raw_input("Please input ID :")
    password = raw_input("Please input Password :")
    main(user, password)