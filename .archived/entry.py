from application \
    import Application as \
    Program

application = None


def main():
    global application

    application = Program()
    application.initiate()
    application.execute()
    application.cleanup()


if __name__ == '__main__':
    main()