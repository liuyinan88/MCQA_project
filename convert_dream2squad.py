import os
import json
import argparse
from tqdm import tqdm


def convert_dream_to_squad(data_root, data_type):
    squad_formatted_content = {"data": [], "version": f"{data_type}.json"}
    # data = load_json_file(os.path.join(data_root, f"{data_type}.json"))
    data_path = os.path.join(data_root, f"{data_type}.json")
    f = open(data_path)
    data = json.loads(f.read())
    # Iterating through the json
    # list
    for i in data:
        for j in i[0]:
            context = j
        for m in i[1]:
            qas = []
            qas.append({
                "answers": [{
                    "answer_start": -1,
                    "text": None,
                    "answer": m['answer'],
                }],
                "question": m['question'],
                "id": i[2],
                "options": m['choice'][1:],
            })
        paragraphs = {
            "title": 'dreaming',
            "paragraphs": [{
                "context": context,
                "qas": qas,
            }]
        }
        squad_formatted_content["data"].append(paragraphs)
    return squad_formatted_content


def save(data, dir_root, data_type):
    file_path = os.path.join(dir_root, '{}.json'.format(data_type))
    with open(file_path, 'w') as fout:
        print("Saving {}".format(file_path))
        json.dump(data, fout, indent=4)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='/data/DREAM')
    parser.add_argument('--data_type', type=str, default='train')
    args = parser.parse_args()

    data = convert_dream_to_squad(args.data_dir, args.data_type)
    save(data, args.data_dir, args.data_type)


if __name__ == "__main__":
    # convert_dream_to_squad('data/DREAM', 'train')
    # f = open('data/DREAM/train.json')
    # data = json.loads(f.read())
    # print(data)
    main()

