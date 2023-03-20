import utils
import readcsv
import grafica

def run():
  data = readcsv.read_csv('./app/data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  grafica.generate_bar_chart(countries, percentages)

'''
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    grafica.generate_bar_chart(labels, values)
'''


if __name__ == '__main__':
  run()



