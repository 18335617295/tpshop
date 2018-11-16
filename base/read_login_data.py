import yaml


def read_login_data():
    with open("..\data\login_data.yaml", "r") as f:
        data = yaml.load(f)
        print(type(data))


if __name__ == '__main__':
    read_login_data()
