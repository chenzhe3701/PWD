import json

# get cookie from console, write it to json file


def cookie_to_json():
    all_dict = {}

    with open("C:/Users/ZheChen/Desktop/usr_cookie.txt", "r") as f:
        data = f.read()
        data = data.split('===')

        i = 0
        for sub_data in data:
            sub_data = sub_data.replace('\n', '')
            sub_data = sub_data.replace(' ', '')
            my_string = sub_data.split(';')
            my_dict = {}
            for sub_str in my_string:

                key, value = sub_str.split('=')
                my_dict.update({key: value})

            all_dict.update({str(i): my_dict})
            i = i + 1
    f.close()

    with open("C:/Users/ZheChen/Desktop/usr_cookie.json", "w+") as f:
        json.dump(all_dict, f, indent=4)
        f.close()


if __name__ == '__main__':
    cookie_to_json()