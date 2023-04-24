import pandas as pd
import matplotlib.pyplot as plt

def prepare_store_data(df):
    '''
    Takes in store data as loaded,
    cleans the datetime and turns it to a pandas datetime,
    which is then set as the index
    
    Return: pandas DF
    '''
    df['sale_date'] = pd.to_datetime(df.sale_date.str.replace(' 00:00:00 GMT', ''))
    df = df.set_index('sale_date').sort_index()
    #adding columns
    df['sales_total'] = df.sale_amount * df.item_price
    return df


def get_hist(df):
    ''' Gets histographs of acquired continuous variables'''
    
    plt.figure(figsize=(16, 3))

    # List of columns
    cols = [col for col in df.columns if col not in ['date']]

    for i, col in enumerate(cols):

        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1 

        # Create subplot.
        plt.subplot(1, len(cols), plot_number)

        # Title with column name.
        plt.title(col)

        # Display histogram for column.
        df[col].hist(bins=5)

        # Hide gridlines.
        plt.grid(False)

        # turn off scientific notation
        plt.ticklabel_format(useOffset=False)

        plt.tight_layout()

    plt.show()
        