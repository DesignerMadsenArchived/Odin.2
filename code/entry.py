from application \
    import Application

application = None


def main():
    global application

    application = Application()
    application.initiate()
    application.execute()
    application.cleanup()


if __name__ == '__main__':
    main()