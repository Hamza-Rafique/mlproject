import pandas as pd

def load_data():
    def read_csv_with_fallback(filepath):
        try:
            return pd.read_csv(filepath, encoding='utf-8')
        except UnicodeDecodeError:
            return pd.read_csv(filepath, encoding='latin1')
    
    bo_collections_data = pd.read_csv('./data/bo_collections_data.csv')
    bo_releases_id = pd.read_csv('./data/bo_releases_id.csv')
    bo_summary = pd.read_csv('./data/bo_summary.csv')
    currency_data = pd.read_csv('./data/currency_data.csv')
    movie_crew_data = pd.read_csv('./data/movie_crew_data.csv')
    movie_summary = pd.read_csv('./data/movie_summary.csv')
    movie_ticket_price = pd.read_csv('./data/movie_ticket_prices.csv')
    inflation_data = read_csv_with_fallback('./data/Inflation_Data_v2.csv')
    mapping_file = pd.read_csv('./data/Mapping_file.csv')
    
    return bo_collections_data, bo_releases_id, bo_summary, currency_data, movie_crew_data, movie_summary, movie_ticket_price, inflation_data, mapping_file


def main():
    # Load data
    (bo_collections_data, bo_releases_id, bo_summary, currency_data,
     movie_crew_data, movie_summary, movie_ticket_price, inflation_data,
     mapping_file) = load_data()
    
    print(bo_collections_data.isnull().sum())
    print(bo_releases_id.isnull().sum())
    print(bo_summary.isnull().sum())
    print(currency_data.isnull().sum())
    print(movie_crew_data.isnull().sum())
    print(movie_summary.isnull().sum())
    print(movie_ticket_price.isnull().sum())
    print(inflation_data.isnull().sum())
    print(mapping_file.isnull().sum())

    # print(bo_collections_data.head())
    # print(bo_releases_id.head())
    # print(bo_summary.head())
    # print(currency_data.head())
    # print(movie_crew_data.head())
    # print(movie_summary.head())
    # print(movie_ticket_price.head())
    # print(inflation_data.head())
    # print(mapping_file.head())

if __name__ == "__main__":
    main()
