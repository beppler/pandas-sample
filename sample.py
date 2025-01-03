import pandas as pd

def main():
    data = pd.read_excel('data.xlsx', na_filter = False)
    data['valor'].replace('', 0, inplace=True)
    data['sigla'] = data['nome'].str.split('-', n=2, expand=True)[0]
    data['nome'].replace('', 'N/I', inplace=True)
    data['sigla'].replace('', 'NI', inplace=True)

    print(data)


if __name__ == "__main__":
    main()
