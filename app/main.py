import utils
import read_csv
import charts
import pandas as pd

def run():

#Código para generar el pie chart sin usar PANDAS
  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  # #Código equivalente usando PANDAS
  
  # df(dataframe) 
  df = pd.read_csv("data.csv")  # Nos ahorramos el método creado read_csv.py
  df = df[df['Continent'] == 'Europe']  
  # Equivalente a -> data = list(filter(lambda item : item['Continent'] == 'South America',data))
  countries = df['Country'].values
  # Equivalente a -> countries = list(map(lambda x: x['Country'], data))
  percentages = df['World Population Percentage'].values
  # Equivalente a -> percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)


  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()