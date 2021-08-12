import unittest
import pandas as pd
from src.module.jobs import importdata as T

class ImportTest(unittest.TestCase):
    def test_file_ready(self):
        df = T.LerAquivo()
        self.assertEqual(df, df)
        #print(df)

# if __name__ == "__main__":
#     unittest.main()
