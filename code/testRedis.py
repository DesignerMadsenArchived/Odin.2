import redis


def main():
    r = redis.Redis(
        host='127.0.0.1',
        port=6379,
        password=''
    )

    print("main")


if __name__ == '__main__':
    main()