from src.database.init_database import DB


def load(file):
    with open(file, 'r') as f:
        data = f.read().split('\n')
        res = []
        for d in data:
            if len(d) != 0:
                dd = {}
                d_split = d.split(':')
                dd["email"] = d_split[0]
                dd["password"] = d_split[1]
                dd["second_email"] = d_split[2]
                dd["second_password"] = d_split[3]
                res.append(dd)
        # data = [(d.split(':')) for d in data if len(d) != 0]
        return res

def upload(email: str, password: str, second_email: str = None, second_password: str = None):
    DB.add_bind_session(email, password, second_email, second_password)


if __name__ == "__main__":
    for d_args in load("resources\mails/bing_mail.txt"):
        upload(**d_args)
