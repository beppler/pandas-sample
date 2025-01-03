import pandas as pd

def main():
    data = pd.read_excel('data.xlsx', na_filter = False)
    data['sigla'] = data['nome'].str.split('-', n=2, expand=True)[0].replace('', 'NI')
    data['nome'] = data['nome'].replace('', 'N/I')
    data['valor'] = data['valor'].replace('', '0')

    print(data)


if __name__ == "__main__":
    main()
