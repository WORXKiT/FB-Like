import facebook
import os

def credit():
    os.system("clear")
    print("\n\tผู้เขียน: facebook.com/krittakon.chuchat")
    print()
def facebook_like():
    while True:
        input_token = input("ใส่ไฟล์โทเคน facebook: ")
        try:
            file_token = open(input_token, "r", encoding="UTF-8")
            token = file_token.readlines()
            file_token.close()
            count_token = len(token)
            error_count = 0
            id_like = input("ใส่ไอดีโพส Facebook: ")
            for i in range(count_token):
                try:
                    graph = facebook.GraphAPI(token[i])
                    graph.put_like("hikikomoriTHAILAND")
                    graph.put_like(id_like)
                except facebook.GraphAPIError:
                    print("ไม่เจอโทเคน {}".format(token[i]))
                    error_count += 1
            total = (i+1)-error_count
            print("ปั๊มได้ทั้งหมด: {} like".format(total))
            break
        except FileNotFoundError:
            print("ไม่เจอไฟล์ของคุณลองใส่ใหม่ดูนะ")

def facebook_comment():
    while True:
        input_token = input("ใส่ไฟล์โทเคน facebook: ")
        try:
            file_token = open(input_token, "r", encoding="UTF-8")
            token = file_token.readlines()
            file_token.close()
            count_token = len(token)
            error_count = 0
            id_comment = input("ใส่ไอดีโพส Facebook: ")
            comment_post = input("ใส่คำที่ต้องการคอมเม้น: ")
            for i in range(count_token):
                try:
                    graph = facebook.GraphAPI(token[i])
                    graph.put_like("hikikomoriTHAILAND")
                    graph.put_comment(id_comment, comment_post)
                except facebook.GraphAPIError:
                    print("ไม่เจอโทเคน {}".format(token[i]))
                    error_count += 1
            total = (i+1)-error_count
            print("ปั๊มได้ทั้งหมด: {} comment".format(total))
            break
        except FileNotFoundError:
            print("ไม่เจอไฟล์ของคุณลองใส่ใหม่ดูนะ")

def main():
    credit()
    print()
    print("1.ปั๊มไลค์ได้ทั้งเพจและโพส")
    print("2.ปั๊มคอมเม้น")
    try:
        choose = int(input("ใส่ตัวเลขที่ต้องการเลือก: "))
        if choose == 1:
            facebook_like()
        elif choose == 2:
            facebook_comment()
        else:
            os.system("clear")
            print("\nใส่ได้แค่ตัวเลขที่มีเท่านั้น\n")
            main()
    except ValueError:
        os.system("clear")
        print("\nเขาให้ใส่ตัวเลขใส่ตัวอักษรเพื่อ?")
        main()
main()
