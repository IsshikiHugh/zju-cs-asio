import os
import csv
import sys
from urllib.parse import urlparse

def red_str(msg:str):
    return '\033[31m' + msg + '\033[0m'

def orange_str(msg:str):
    return '\033[33m' + msg + '\033[0m'

def red_print(msg:str):
    print(red_str(msg))

def orange_print(msg:str):
    print(orange_str(msg))


DESC_LIMIT = 256  # the max length of description to be displayed in the table

class ASIOHelper:
    def __init__(self, file_name:str):
        self.file_name = file_name
        self.titles = {
            "Title"      : f"The title of the resource.",
            "URL"        : f"The available URL of the resource.",
            "Description": f"What you might find in the resource. (No longer than {DESC_LIMIT} characters, otherwise it will be truncated.)",
            "Type"       : f"`0` for personal website; `1` for student's organization website; `2` for official course resources; `3` for others.",
        }
        self.type_mapping = ["💎 个人", "🔮 组织", "🧲 课程", "🎉 其他"]
        self.rows = []  # consists the title row

        self.load_data()
        assert len(self.rows) > 0, "Empty file!"

    def valid_url(self, url:str) -> bool:
        """ Check if a url is valid. """
        try:
            result = urlparse(row[1])
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def valid_row(self, row:list) -> bool:
        # check items number
        if len(row) != len(self.titles):
            red_print(f'Row length mismatch: {len(row)} != {len(self.titles)}')

            return False
        # check title
        if row[0] == '':
            # print red line
            red_print('Title cannot be empty!')
            return False
        # check URL
        if not self.valid_url(row[1]):
            red_print('Invalid URL!')
            return False
        # check description
        pass
        # check type
        if row[3] not in ['0', '1', '2', '3']:
            red_print('Invalid type! Only `0`, `1`, `2`, `3` are allowed.')
            return False

        # all passed
        return True

    def load_data(self):
        with open(self.file_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = self.format_row(row)
                if len(row) != len(self.titles):
                    orange_print(f'Illegal row detected in `data.csv`: {row}, it will be ignored and overwritten!')
                else:
                    self.rows.append(row)

    def write_data(self):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            for row in self.rows:
                row = self.format_row(row)
                writer.writerow(row)

    def format_row(self, row:list):
        n = len(row)
        for i in range(n):
            row[i] = row[i].strip()
        return row

    def append_row(self, row:list):
        row = self.format_row(row)
        assert len(row) == len(self.titles), red_str("Row length mismatch!")
        assert self.valid_row(row) == True, red_str("Invalid row! Append failed!")
        self.rows.append(row)

    def get_titles(self):
        return self.titles

    def sort_rows(self):
        self.rows.sort(key=lambda x: x[3])

    def render2md(self, output_name:str, support_name:str):
        assert len(self.rows) > 0, red_str("Haven't load a file yet or the file is empty!")
        self.sort_rows()

        # ============================== #
        # prepare statistics information #
        # ============================== #
        type_cnt = {}
        for row in self.rows:
            type_cnt[row[3]] = type_cnt.get(row[3], 0) + 1
        stat_items = []
        for type_id, cnt in type_cnt.items():
            stat_items.append(f' {self.type_mapping[int(type_id)]} {cnt} 项')
        md_stat = '**条目统计**：' + ' / '.join(stat_items) + '！'

        # ============================ #
        # prepare table to be embedded #
        # ============================ #
        md_table = ''
        # render the title rows
        line_title = '| Title | Description |'
        line_split = '| :--- | :--- |'
        md_table += line_title + '\n'
        md_table += line_split + '\n'
        # render the data rows
        for row in self.rows:
            line = '|'
            # title, URL and type
            type_id = int(row[3])
            line += f' <a href="{row[1]}" target="_blank">{self.type_mapping[type_id][:1]} {row[0]}</a> |'
            # description
            desc = row[2]
            if len(desc) > DESC_LIMIT:
                desc = desc[:DESC_LIMIT] + '...'
            line += f' 🥑 {desc} |'
            # finish line
            md_table += line + '\n'

        # ==================================== #
        # embed and render the new `README.md` #
        # ==================================== #
        embed = f'{md_stat}\n\n{md_table}'

        with open(support_name, 'r', encoding='utf-8') as f:
            md = f.read()
        md = md.replace('<!-- ASIO-EMBED-HERE -->', embed)

        with open(output_name, 'w', encoding='utf-8') as f:
            f.write(md)


if __name__ == '__main__':
    usage = """
    Usage: python scripts/asio_helper.py <flag>
    Available flags:
        -f: format `data.csv`
        -a: append a row to `data.csv`
        -r: render `data.csv`
    """
    # check arguments
    assert len(sys.argv) == 2, usage
    flag = sys.argv[1]

    # prepare the file paths and names
    scripts_dir   = os.path.dirname(__file__)
    repo_root_dir = os.path.dirname(scripts_dir)
    data_path       = os.path.join(repo_root_dir, 'data.csv')
    md_support_path = os.path.join(repo_root_dir, 'materials/README-support.md')
    md_output_path  = os.path.join(repo_root_dir, 'README.md')

    helper = ASIOHelper(data_path)

    # process the flag
    if flag == '-f':
        pass
    elif flag == '-a':
        row = []
        columns = helper.get_titles()
        # read new row
        for col_name, col_desc in columns.items():
            item = input(f'Please enter resource [{col_name.lower()}]:\n> {col_desc}\n')
            row.append(item)
        # save the information
        helper.append_row(row)
    elif flag == '-r':
        helper.render2md(
            output_name  = md_output_path,
            support_name = md_support_path
        )
    else:
        raise NotImplementedError(red_str(f'Unknown flag: {flag}'))

    # save the data
    helper.write_data()