import csv
from googletrans import Translator 
import codecs
import time
import gc

class connectCSV:

    @classmethod
    def read_file(cls, endpoint: str) -> list[list]:
        if endpoint.find(".scv"): endpoint += ".csv"
        table_from_endpoint_csv_file = []
        with codecs.open(endpoint, "r", "utf_8_sig") as csv_file:
            read_csv_file = csv.reader(csv_file)
            for row in read_csv_file:
                table_from_endpoint_csv_file.append(row)
        return table_from_endpoint_csv_file

    @classmethod
    def writer_file(cls, list_for_writer: list, new_file_name: str = "eng_positions_and_skills") -> None:
        new_file_name += ".csv"
        try:
            with open(new_file_name, "a", newline='') as csv_file:
                write_scv_file = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                write_scv_file.writerow(list_for_writer)
        except Exception as _ex:
            print("[ERROR] some one do wrong:\n", _ex)

class translator:
    def __init__(self, start_pint_id: int = 0, columns: int = 2, to_lang: str = "en"):
        self.example_of_translator = Translator()
        self.to_lang = to_lang
        self.columns = columns
        self.start_pint_id = start_pint_id

    def translate (self, data_list: list) -> str:
        data_list_len = len(data_list)
        optimiztion_dict = {}
        for row_id in range(self.start_pint_id, data_list_len):
            try:
                gc.collect()
                start_iteration_time = time.time()
                time_list = []
                for item_id in range(0, len(data_list[row_id])):
                    item = data_list[row_id][item_id]
                    if item_id < self.columns:
                        if not optimiztion_dict.get (item):
                            optimiztion_dict.update ({item : self.example_of_translator.translate(item, dest=self.to_lang).text})
                        time_list.append (optimiztion_dict.get (item))
                        if len(optimiztion_dict) > 1000:
                            optimiztion_dict.clear()
                    else: 
                        time_list.append(item)
                connectCSV.writer_file(time_list)
                print(f"[INFO] ready {row_id + 1}/{data_list_len} for {round(time.time() - start_iteration_time, 2)}s")
            except Exception as _ex:
                print("[ERROR] some one do wrong:\n", _ex)
        return "[INFO] congratulations, congratulations, congratulations"

if __name__ == '__main__':
    translator().translate(connectCSV.read_file("test"))