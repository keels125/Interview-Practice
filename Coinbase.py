#interview question

import json

def bitcoinPrice(asks, amt):
    i=0 #use for list of lists
    
    
    current_amt=0
    price = 0
    
    while (current_amt<amt and i<len(asks)):
        
        if (float(asks[i][1])<=(amt-current_amt)): #if we can add the whole amount
            current_amt+=float(asks[i][1])
            price+=float(asks[i][0])*float(asks[i][1])
            i+=1
        else:
            #add a fraction
            price+= float(asks[i][0]) * (amt-current_amt)
            current_amt=amt #done
            return price
    return 0
    


def main():
    with open('book.json') as data_file:
        data = json.load(data_file)
    asks = data.get('asks')

    print(bitcoinPrice(asks, -1))

main()
