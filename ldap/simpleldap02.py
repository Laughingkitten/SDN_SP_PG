# -*- coding: utf-8 -*-
import sys
import Tkinter
from ldap3 import Server,Connection,AUTO_BIND_NO_TLS,SUBTREE,ALL_ATTRIBUTES
#s = Server('ldap://ldap.ie.u-ryukyu.ac.jp', 389)


#Buttonが押された時に呼び出されるはずのメソッド
def ldapaute(EditBox,EditBox2):

        user = EditBox.get()
        passwd = EditBox2.get()

        user = 'e155728'
        passwd = 'R!tukachan666!D'




        try:
	        # 認証
                s = Server('ldap://ldap.ie.u-ryukyu.ac.jp', 389)
	        c = Connection( s, user=('uid='+user+',ou=cc,ou=ie,o=u-ryukyu,c=jp'), password=(passwd), check_names=True, read_only=True, auto_bind=AUTO_BIND_NO_TLS)

	        print('result',c.result)
                #以下に、Djangoにuid送信のスクリプト

        except:
                #認証失敗
	        print("unsuccesssful")

        return


def printff():
    print("test")
    return


if __name__ == "__main__":
    root = Tkinter.Tk()
    root.title(u"Software Title")
    root.geometry("500x400")

    lab_uid = Tkinter.Label(text=u'ユーザーidを入力')
    lab_uid.place(x=200,y=75)

    #エントリー
    EditBox = Tkinter.Entry(width=50)
    EditBox.insert(Tkinter.END,"id")
    #EditBox.pack(pady=40)
    EditBox.place(x=10,y=100)

    #value = EditBox.get()

    lab_pass = Tkinter.Label(text=u'パスワードを入力')
    lab_pass.place(x=200,y=225)

    #エントリー
    EditBox2 = Tkinter.Entry(width=50)
    EditBox2.insert(Tkinter.END,"password")
    #EditBox2.pack(pady=40)
    EditBox2.place(x=10,y=250)

    #ここで，valueにEntryの中身が入る
    #value2 = EditBox2.get()

    #Button = Tkinter.Button(text=u'登録', width=25)
    Button = Tkinter.Button(root,text=u'test',width=25,command=ldapaute(EditBox,EditBox2))
    #Button.bind("<Button-1>",printff())
    #左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
    Button.place(x=10,y=300)


    root.mainloop()

