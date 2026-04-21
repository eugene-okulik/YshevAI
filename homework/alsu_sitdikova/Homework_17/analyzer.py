import argparse
import os
import logging
import collections

from datetime import datetime
from colorama import Fore, Back, Style
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
LOGGER = logging.getLogger(__name__)


class LogFiles:
    def __init__(self, pth, text):
        self.pth = pth
        self.text = text

    def _if_path_exist(self):
        if os.path.exists(self.pth):
            if os.path.isdir(self.pth):
                LOGGER.info('Каталог с файлами')
                fls = os.listdir(self.pth)
                log_fls = [os.path.join(self.pth, file) for file in fls if file.endswith(".log")]
                if not log_fls:
                    LOGGER.info("В каталоге нет файлов с расширениеv .log")
                    return None
                return log_fls

            elif os.path.isfile(self.pth):
                LOGGER.info('Файл')
                file_path = os.path.basename(self.pth)
                if file_path.endswith(".log"):
                    LOGGER.info("Лог файл")
                    return self.pth
                else:
                    LOGGER.info("Файл не с расширением .log")
                    return None
        else:
            LOGGER.info(f"Не удается найти файл по указанному пути: {self.pth}")
            exit()

    def _get_block_by_date(self):
        file = self._if_path_exist()
        if file:
            if isinstance(file, str):
                return {os.path.basename(self.pth): self._get_data_dict(file)}

            elif isinstance(file, list):
                file_dict = dict()
                for f in file:
                    file_dict.update({os.path.basename(f): self._get_data_dict(f)})
                return file_dict

    @staticmethod
    def file_str(pth):
        with open(os.path.normpath(pth), 'r', encoding="utf-8") as f:
            for fline in f:
                yield fline

    @staticmethod
    def is_date(supposed_key):
        try:
            datetime.strptime(supposed_key, "%Y-%m-%d %H:%M:%S.%f")
            return True

        except ValueError:
            return False

    def _get_neighbourhood(self, line):
        """Будем иметь в виду, что каждое слово в тексте отделено пробелом, будет считываться одна строка
        line: строка по которой ведется поиск
        word: принимает слово, по которому ведется поиск
        """
        word_count = 1
        word_dict = {}
        leftside_remains = []
        while len(line) > len(self.text):
            if self.text in line:
                word_start = line.find(self.text)
                word_end = word_start + len(self.text)
                left_neighbours = line[:word_end].replace(',', ' ').split()
                leftside_remains.extend(left_neighbours)
                right_neighbours = line[word_end:].replace(',', ' ').split()
                if len(leftside_remains) > 5:
                    ln = ' '.join(leftside_remains[-6:])
                else:
                    ln = ' '.join(leftside_remains)
                if len(right_neighbours) > 5:
                    rn = ' '.join(right_neighbours[:5])
                else:
                    rn = ' '.join(right_neighbours)
                line = line[word_end:]
                word_dict.update({f"found_{word_count}":
                                  f"{ln[:-len(self.text)]}{Back.GREEN + self.text + Style.RESET_ALL} {rn}"})
                LOGGER.debug(f"{ln[:-len(self.text)]}{Back.GREEN + self.text + Style.RESET_ALL} {rn}")

                word_count += 1

            else:
                break

        return word_dict

    def _get_data_dict(self, pth):
        file_dict = collections.defaultdict(list)
        line = 1
        key = ''
        for fline in self.file_str(pth):
            if self.is_date(fline[:23]):
                key = fline[:23]

            if self.text in fline:
                res = self._get_neighbourhood(fline)
                file_dict[key].append({f"line_{line}": res})  # Тут строки содержащие слова поиска

            line += 1
        return file_dict

    @staticmethod
    def _unpack_res(res: list):
        for i in res:
            for k, kv in i.items():
                print("\t\t", k)
                for vk, v in kv.items():
                    print(f"\t\t\t{vk}: {v}")

    def show_line_with_text(self):
        for outer_key, inner_dict in self._get_block_by_date().items():
            if inner_dict:
                print("LOG FILE NAME:", Fore.BLUE + outer_key + Style.RESET_ALL)
            for inner_key, value in inner_dict.items():
                print("\tThe time:", Fore.CYAN + inner_key + Style.RESET_ALL)
                print(self._unpack_res(value))

    def __repr__(self):
        return self._get_block_by_date()


def main():
    parser = argparse.ArgumentParser(
        prog='analyzer',
        description='Ищет требуемое слово построчно, регистрозависимо',
        epilog='Введите путь до файла/каталога с файлами и слово для поиска через пробел')

    parser.add_argument('filename', type=str, help='Абсолютный путь до логов')
    parser.add_argument('word', type=str, help='Слово для поиска')
    args = parser.parse_args()

    lf = LogFiles(pth=args.filename, text=args.word)
    lf.show_line_with_text()
    # print(lf.__repr__())


if __name__ == '__main__':
    main()
