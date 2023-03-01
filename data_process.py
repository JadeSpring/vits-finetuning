from utils import load_filepaths_and_text
import os

if __name__ == '__main__':
    xx = load_filepaths_and_text("filelists/wave_info.txt")

    # train_text = [f'{x[0]}|10|{x[1]}' for x in xx]
    all_clean = [f'Wave/{x[0]}.wav|10|{x[1]}' for x in xx]
    train_clean = all_clean[:160]
    val_clean = all_clean[-32:]

    train_file_path = 'filelist/train.text'
    val_file_path = 'filelist/val.text'

    with open(train_file_path, "w", encoding="utf-8") as f:
        f.writelines([x + "\n" for x in train_clean])

    with open(val_file_path, "w", encoding="utf-8") as f:
        f.writelines([x + "\n" for x in val_clean])
