import csv
from translate import Translator

class connectCSV:

    @classmethod
    def read_file(cls):
        endpint: str = "position_and_skills.csv"
        table_from_endpint_csv_file = []
        with open(endpint, "r", newline="") as csv_file:
            read_csv_file = csv.reader(csv_file)
            for row in read_csv_file:
                table_from_endpint_csv_file.append(row)
        return table_from_endpint_csv_file

    @classmethod
    def writer_file(cls, list_for_writer: list, new_file_name: str = "new_file"):
        new_file_name += ".csv"
        try:
            with open(new_file_name, "w") as csv_file:
                write_scv_file = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                write_scv_file.writerow(list_for_writer)
            print("[INFO] all make OK")
        except Exception as _ex:
            print("[ERROR] some one do wrong:\n", _ex)

class translator:
    def __init__(cls, columns: int = 2, from_lang: str = "ru", to_lang: str = "en"):
        cls.example_of_translator = Translator(from_lang=from_lang, to_lang=to_lang)
        cls.from_lang = from_lang
        cls.to_lang = to_lang

    def translate (cls, data_list: list):
        try:
            translate_list = []
            data_list_len = len(data_list)
            for row_id in range(0, data_list_len):
                print(f"[INFO] ready {row_id}/{data_list_len}")
                time_list = []
                for item_id in range(0, 2):
                    time_list.append(cls.example_of_translator.translate(data_list[row_id][item_id]))
                translate_list.append(time_list)
            return translate_list
        except Exception as _ex:
            print("[ERROR] some one do wrong:\n", _ex)

if __name__ == '__main__':
    connectCSV.writer_file(translator().translate(connectCSV.read_file()))