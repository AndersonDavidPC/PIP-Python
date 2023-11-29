import read_csv
import utils
import charts

def run():
    data = read_csv.read_csv('data.csv')

    country = input('Enter a country: ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country_data = result[0]
        labels, values = utils.get_population(country_data)
        charts.generate_bar_chart(country_data['Country/Territory'], labels, values)
        print(f"Bar chart for {country} population saved as {country}.png in imgs folder.")
    else:
        print("Country not found in the dataset.")

if __name__ == '__main__':
    run()
