from utils import load_filepaths_and_text, resample_rate

import re

if __name__ == '__main__':
    xx = load_filepaths_and_text("filelists/wave_info.txt")

    xx = xx[:160]
    for a in xx:
        a[1] = re.sub(r'#\d+', '', a[1])
        resample_rate(f'Wave/{a[0]}.wav', new_sample_rate=22050)

    all_clean = [f'Wave/{x[0]}_new.wav|10|[ZH]{x[1]}[ZH]' for x in xx]
    train_clean = all_clean[:144]
    val_clean = all_clean[-16:]

    train_file_path = 'filelists/train.txt'
    val_file_path = 'filelists/val.txt'

    with open(train_file_path, "w", encoding="utf-8") as f:
        f.writelines([x + "\n" for x in train_clean])

    with open(val_file_path, "w", encoding="utf-8") as f:
        f.writelines([x + "\n" for x in val_clean])
