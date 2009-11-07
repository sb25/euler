# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
converter = {
  "1": "one",
  "2": "two",
  "3": "three",
  "4": "four",
  "5": "five",
  "6": "six",
  "7": "seven",
  "8": "eight",
  "9": "nine",
  "10": "ten",
  "11": "eleven",
  "12": "twelve",
  "13": "thirteen",
  "15": "fifteen",
  "18": "eighteen",
  "20": "twenty",
  "30": "thirty",
  "40": "forty",
  "50": "fifty",
  "80": "eighty",
  "1000": "onethousand"
}

def number_to_letter(nb):
  nb = str(nb)
  if nb in converter.keys():
    return converter[nb]
    
  if len(nb) == 2:
    if nb[0] == "0":
      return converter[nb[1]]
      
    if nb[0] == "1":
      return converter[nb[1]] + "teen"
    elif nb[0] in ["2", "3", "4", "5", "8"]:
      return converter["%s0"%nb[0]] + converter[nb[1]]
    elif nb[1] == "0":
      return "%sty"%converter[nb[0]]
    else:
      return "%sty %s"%(converter[nb[0]], converter[nb[1]])
  
  elif len(nb) == 3:
    if nb[1:] == "00":
      return converter[nb[0]] + "hundred"
    else:
      return converter[nb[0]] + " hundred and " + number_to_letter(nb[1:])

nb_of_letters = 0
for nb in range(1, 1001):
  letters = number_to_letter(nb)
  nb_of_letters += len(letters.replace(' ',''))
print nb_of_letters