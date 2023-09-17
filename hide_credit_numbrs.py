def take_card(card):
    if len(card)==16:
        last_code=card[-4:]
        print("*************", last_code) 
    else:
        print("Invelid card number")                        
take_card("0123457891012734")