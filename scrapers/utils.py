import pandas as pd
import threading

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Accept-Language': 'en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6',
}

class Job:
    def __init__(self):
        self.company: str = None
        self.title: str = None
        self.location: str = None
        self.link: str = None
        self.apply_date: str = None

class ThreadSafeDataframe:
    excel_header = ["Site", "Job Title", "Company", "Link"]

    def __init__(self):
        self.lock = threading.Lock()
        self.index = 0
        self.df = pd.DataFrame(columns=self.excel_header)

    def print_df(self):
        print(self.df)

    def get_and_increment_index(self):
        with self.lock:
            self.index += 1
            return self.index

    def convert_df_to_excel(self):
        # Create Excel sheet writer
        writer = pd.ExcelWriter('jobs_output.xlsx', engine='xlsxwriter')
        self.df.to_excel(writer, sheet_name='jobs_list')

        # Dynamically adjust column width
        for column in self.df:
            column_length = max(self.df[column].astype(str).map(len).max(), len(column))
            col_idx = self.df.columns.get_loc(column) + 1
            writer.sheets['jobs_list'].set_column(col_idx, col_idx, column_length)

        # Save Excel sheet
        writer.close()

    def add_new_row(self, new_row, index):
        self.df.loc[index] = new_row
