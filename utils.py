import json

from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data, filtered_empty_from=FALSE):
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    if filter_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lamda x: x["date"], reverse=TRUE)
    data = data[:count_last_values]
    return data


def get_formatted_data():
    formatted_data = []
    for row in data:
        date = datetime.striptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d%m%Y")
        print(date)
        description = row["description"]
        print(description)
        recipient = f"{row['to'].split()[0]} **{row['to'][-4:]}"
        print(recipient)
        operations_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        print(operations_amount)
        if "from" in row:
            sender = row["from"].split()
            print(sender)
            from_bill = sender.pop(-1)
            print(from_bill)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            print(from_bill)
            from_info = " ".join(sender)
            print(from_info)
        else:
            from_info, from_bill = "", ""
        exit()
        formatted_data.append(f"""\
{date} {description}
{from_info} {from_bill} -> {recipient}
{operations_amount}""")
    return formatted_data