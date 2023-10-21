import csv
import sys
from urllib.parse import urlparse

def red_str(msg:str):
    return '\033[31m' + msg + '\033[0m'

def red_print(msg:str):
    print(red_str(msg))


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
            type = int(row[3])
            line += f' <a href="{row[1]}" target="_blank">{self.type_mapping[type][:1]} {row[0]}</a> |'
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
        
        with open(support_name, 'r', encoding='utf-8') as f:
            md = f.read()
        md = md.replace('<!-- ASIO-EMBED-HERE -->', md_table)
        
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
    helper = ASIOHelper('data.csv')
    
    assert len(sys.argv) == 2, usage
    flag = sys.argv[1]

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
        helper.render2md('README.md', 'materials/README-support.md')
    else:
        raise NotImplementedError(red_str(f'Unknown flag: {flag}'))
        
    helper.write_data()
    