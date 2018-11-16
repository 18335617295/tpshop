import yaml


def read_login_data(key):
    with open("..\data\login_data.yaml", "r", encoding="utf-8") as f:
        data = yaml.load(f)[key]
        data_list = list()
        for i in data.values():
            data_list.append(i)
        return data_list


if __name__ == '__main__':
    read_login_data('test_login')
