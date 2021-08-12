import pandas as pd
class LerAquivo:
    def leitura(self):
        df = pd.read_csv('tests/locallake/raw/df.csv')
        #return df
        print(df)

objeto = LerAquivo()

objeto.leitura()
