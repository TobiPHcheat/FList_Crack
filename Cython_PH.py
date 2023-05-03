if __name__ == "__main__":

    try:

        __import__("enc_Run.py").security()

    except Exception as e:

        exit(str(e))
