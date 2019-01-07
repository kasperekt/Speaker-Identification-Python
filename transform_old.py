import os
import glob
import soundfile as sf
import scipy.io
import scipy.io.wavfile

# DEST_DIR = 'names-train'
DEST_DIR = 'names-train-better'
SRC_DIR = 'Imiona'

# Format: <person>_<name>.wav
FILE_FORMAT = '{}_{}.wav'


def extract_names(file_path):
    person = file_path[:5]
    name = file_path[5:8]
    return person, name


def main():
    all_paths = glob.glob(os.path.join(SRC_DIR, '*.WAV'))

    training_files_fp = open('names-training-path.txt', 'w')

    for wave_path in sorted(all_paths):
        base_name = wave_path.split('/')[-1]
        person, name = extract_names(base_name)

        if name == 'BOZ':
            continue

        dest_base_name = FILE_FORMAT.format(person, name)

        wav, sr = sf.read(wave_path)

        dest_base_dir = os.path.join(DEST_DIR, person)
        if not os.path.exists(dest_base_dir):
            os.mkdir(dest_base_dir)

        training_files_fp.write('{}\n'.format(
            os.path.join(person, dest_base_name)))

        scipy.io.wavfile.write(os.path.join(
            dest_base_dir, dest_base_name), sr, wav)

    training_files_fp.close()


if __name__ == '__main__':
    main()
