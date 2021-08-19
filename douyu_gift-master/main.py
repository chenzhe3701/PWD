from douyu.douyu_main_app import start
from tools.my_log import MyLog
import sys
from tools.utls import *
import json
from douyu.api import *

def init_app():
    MyLog.set_status(0)


def cookie_to_json():
    all_dict = {}
    for i in range(1):
        with open("C:/Users/ZheChen/Desktop/usr_cookie.txt", "r") as f:
            data = f.read()
            my_string = data.split(';')
            my_dict = {}
            for sub_str in my_string:
                sub_str = sub_str.replace('\n', '')
                sub_str = sub_str.replace(' ', '')
                key, value = sub_str.split('=')
                my_dict.update({key: value})

            f.close()
        all_dict.update({str(i): my_dict})

    with open("C:/Users/ZheChen/Desktop/usr_cookie.json", "w+") as f:
        json.dump(all_dict, f, indent=4)
        f.close()


def main():

    # The following is to directly look through cookies for multiple users.
    with open("C:/Users/ZheChen/Desktop/usr_cookie.json", "r") as f:
        cookies = json.load(f)

    for key in cookies.keys():
        cookie = cookies[key]  # for each user
        rid = 2454442 # 3725015 # xiong # 319435 qiqi # 3331957    # 弹幕 2006457
        did = query_did(rid)
        dy_did = cookie['acf_did']
        sid = cookie['acf_uid']
        default_gift_id = 20643
        gift_num = 1

        # dy:               dy_did
        # prop_id: 268      礼物id   粉丝荧光棒 prop_id=268,rel_id=824, 水晶 id=20643, 小星星 prop_id=940，rel_id=20596, 办卡 prop_id=20212, dan prop_id = 20624
        # num: 1            数量
        # sid: xxx          acf_uid
        # did: xx           主播的uid
        # did               获取地址：https://www.douyu.com/ztCache/WebM/room/196 ,\"owner_uid\":5748,\
        # rid: xx           房间id
        send_dy_gift_with_cookie(dy_did, sid, did, rid, default_gift_id, gift_num, cookie)
    return 0


if __name__ == "__main__":
    main()
    # start(1)

    """
    init_app()
    start_type = -1
    print('************************')
    print('*   0: 退出' + my_align(u'0: 退出', 18) + '*')
    print('*   1: 每日续牌' + my_align(u'0: 每日续牌', 17) + '*')
    print('*   2: 均分续牌' + my_align(u'0: 均分续牌', 17) + '*')
    print('*                      *')
    print('*                      *')
    print('*   version: 1.3       *')
    print('************************')
    start_type = int(input("请输入："))
    # while start_type != 0:
    try:
        start(start_type)
    except:
        print("Unexpected error:", sys.exc_info())

    input("Press <enter> to END")
    """

