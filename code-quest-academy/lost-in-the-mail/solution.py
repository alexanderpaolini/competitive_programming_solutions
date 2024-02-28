# Submitted
cases = int(input())


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num


for _ in range(cases):
    package_count = int(input())

    info = []

    for _ in range(package_count):
        data_str = (((input().replace(
            'T', '00').replace('A', '01').replace('D', '10').replace('F', '11'))))
        while data_str[0] == '0':
            data_str = data_str[1::]
        data_str = (str(int(data_str, 2)))

        tracking_code = data_str[(len(data_str) - 18):]
        data_int = int(data_str[0:(len(data_str) - 18)])
        data_int //= 50
        data_int -= 100001
        routing_num = str(data_int)

        mail_type = ""

        mt = tracking_code[0:3]
        if mt == "042" or mt == "261":
            mail_type = "Standard Class Mail"
        elif mt == "040" or mt == "300":
            mail_type = "First Class Mail"
        else:
            mail_type = "Priority Mail"

        data_dict = {
            "zip_code": routing_num[0:5],
            "zip_extension": routing_num[5:9],
            "mail_type": mail_type,
            "mailer_id": tracking_code[3:9],
            "serial_number": tracking_code[9:17]
        }

        info.append(data_dict)

    num_sorted = len(info)
    num_standard = len(
        list(filter(lambda x: x['mail_type'] == "Standard Class Mail", info)))
    num_first = len(
        list(filter(lambda x: x['mail_type'] == "First Class Mail", info)))
    num_priority = len(
        list(filter(lambda x: x['mail_type'] == "Priority Mail", info)))
    most_frequent_mailer_id = most_frequent(
        list(map(lambda x: x['mailer_id'], info)))
    most_frequent_zip_code = most_frequent(
        list(map(lambda x: x['zip_code'], info)))

    print(f"Packages Sorted: {num_sorted}")
    print(f"Standard Class: {num_standard}")
    print(f"First Class: {num_first}")
    print(f"Priority Mail: {num_priority}")
    print(f"Most frequent mailer ID: {most_frequent_mailer_id}")
    print(f"Most frequent ZIP code: {most_frequent_zip_code}")
