from utils import load_filepaths_and_text
import re

if __name__ == '__main__':
    xx = load_filepaths_and_text("filelists/wave_info.txt")

    xx = xx[:160]
    for a in xx:
        a[1] = re.sub(r'#\d+', '', a[1])

    all_clean = [f'Wave/{x[0]}.wav|10|[ZH]{x[1]}[ZH]' for x in xx]
    all_clean = all_clean[:160]
    train_clean = all_clean[:128]
    val_clean = all_clean[-32:]

    train_file_path = 'filelists/train.text'
    val_file_path = 'filelists/val.text'

    with open(train_file_path, "w", encoding="utf-8") as f:
        f.writelines([x + "\n" for x in train_clean])

    with open(val_file_path, "w", encoding="utf-8") as f:
        f.writelines([x + "\n" for x in val_clean])
