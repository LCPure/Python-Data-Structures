text = "X-DSPAM-Confidence:    0.8475";
number_found = text.find('.')
number_offset = 5
number_string = text[number_found:number_found + number_offset]
final_number = float(number_string)
print('Final Number is ', final_number)
