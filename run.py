import argparse
import app


def parse_args():
    parser = argparse.ArgumentParser(description="Simple telegram bot",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--token-path", default="./token")

    return parser.parse_args()


def main():
    args = parse_args()
    app.init_bot('823664291:AAEfuC8rMJ4eRke2vSrdUsHy7h67RkPO3cE')
    app.bot.polling(none_stop=True, interval=1)


if __name__ == "__main__":
    main()