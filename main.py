import os
import shutil

def get_folders_path(topic_file: str) -> list:

    with open(topic_file, mode="r", encoding="utf-8") as file:

        topics = []
        count = 0

        for topic in file:
            if topic[0] == " ":
                topic = f"/{topics[-count]}/{topic.lstrip()}"
                count += 1
            else:
                count = 1
            topics.append(f"/{topic.rstrip()}")
    return topics


def set_forlder(forlder_path: str, topics: list) -> None:
    for topic in topics:
        try:
            os.makedirs(forlder_path + topic)
        except FileExistsError:
            pass
    else:
        print("Файлы созданы")


def main() -> None:
    forlder_path = f"{os.getcwd()}/Работа/"
    topics_file = "topics.txt"

    topics = get_folders_path(topics_file)
    set_forlder(forlder_path, topics)

    shutil.copy('help.txt', f"{forlder_path}/help.txt")

if __name__ == "__main__":
    main()
