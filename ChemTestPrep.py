import requests
import lxml
from bs4 import BeautifulSoup
import random

url = 'https://www.science.co.il/elements/'
requests_url = requests.get(url)

text = requests_url.text

parsed_text = BeautifulSoup(text,'lxml')

elements = parsed_text.find_all('td',class_='lft')

def generator(iterator):
  for phrase in iterator:
    yield phrase.get_text() + ' ' + iterator[iterator.index(phrase) + 1].get_text()

elements_list = []
for item in generator(elements):
  elements_list.append(item)

test_dict = {}

for i in range(0,len(elements_list),3):
  periodic_elem = elements_list[i].split(' ')
  test_dict[periodic_elem[0]] = periodic_elem[1]
  

prefix_list = [value for value in test_dict]


  
requests_url.close()
# print(test_dict)
# prior setup
Test = True
score = 0

while Test:
  element_value = random.choice(prefix_list)
  computer_key = test_dict[element_value]
  print(computer_key)
  user = input('Ans or Q to quit: ')
  if user.lower() == element_value.lower():
    print('Correct!')
    score += 1
  elif user.lower() == 'q':
    print()
    print(f"Here is your score!: {score}")
    Test = False
  else:
    print('Wrong')

