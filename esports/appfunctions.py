def helloThere(num):
    return num

# Name will be spread1, win1, total2, etc.
def probability(db, name): 
    problist = []
    spreadlist1 = db.values_list(name) # OKAY WE CAN WORK WITH THIS. RETURN THE LIST OF PROBABILITIES.
    for spread in spreadlist1:              # ENSURE THE ROUNDING IS WORKING PROPERLY.
        spread = [i[-4:-1] for i in spread]
        spread = int(spread[0])
        if spread < 0:
            spread = (spread * -1)
            spread = (spread / (spread + 100) * 100)
        else:
            spread = (100 / (spread + 100) * 100)

        spread = round(spread, 1)
        problist.append(spread)
    return problist 

def win_probability(db, name):
    problist = []
    winlist = db.values_list(name)
    for win in winlist:
        win = [i[1:] for i in win]
        win = int(win[0])
        if win < 0:
            win = (win * -1)
            win = (win / (win + 100) * 100)
        else:
            win = (100 / (win + 100) * 100)

        win = round(win, 1)
        problist.append(win)

    return(problist)

def int_from_float(db, name):
    ev_list = []
    float_list = db.values_list(name)
    for float_num in float_list:
        # x = int(float_num[0] * 5) # Quick little note, this is just to make the +EV progress bar look a little nicer. Might play around with the numbers.  Might make this a different function for decimal and ev.
        x = int(float_num[0] * 6)
        if x >= 0:
            ev_list.append(x)
        else:
            x = (x * (-1))
            ev_list.append(x)

    return(ev_list)




def pick_of_day(win, spread, total):
    # Spread and Total [9] and [10]
    # Win is [7] and [8]
 
    # WIN --------------------------------------------------------------
    win1_ev = -100
    win2_ev = -100

    for value in win.values_list():

        if win1_ev < value[7]:
            win1_ev = value[7]
            win1_best = value
        
        if win2_ev < value[8]: 
            win2_ev = value[8]
            win2_best = value
        
        if win1_ev >= win2_ev:
            win_best_final = win1_best # Entire value
            win_best_ev = win1_ev # Floating point number
        else: 
            win_best_final = win2_best # Entire value
            win_best_final = list(win_best_final)
            win_best_ev = win2_ev # Floating point number
        
    # Spread ------------------------------------------------------------
    spread1_ev = -100
    spread2_ev = -100
    for value in spread.values_list():

        if spread1_ev < value[9]:
            spread1_ev = value[9]
            spread1_best = value

        if spread2_ev < value[10]:
            spread2_ev = value[10]
            spread2_best = value

        if spread1_ev >= spread2_ev:
            spread_best_final = spread1_best # Entire value
            spread_best_final = list(spread_best_final)
            spread_best_ev = spread1_ev # Floating point number
        else:
            spread_best_final = spread2_best # Entire value
            spread_best_ev = spread2_ev # Floating point number

    # Total ------------------------------------------------------------
    total1_ev = -100
    total2_ev = -100
    for value in total.values_list():

        if total1_ev < value[9]:
            total1_ev = value[9]
            total1_best = value
        
        if total2_ev < value[10]:
            total2_ev = value[10]
            total2_best = value 
        
        if total1_ev >= total2_ev:
            total_best_final = total1_best # Entire value
            total_best_ev = total1_ev # Floating point number
        else: 
            total_best_final = total2_best # Entire value
            total_best_final = list(total_best_final)
            total_best_ev = total2_ev # Floating point number

    # Now all the variables are set, we just need to compare win, spread, and total.

    print("Win", win_best_final, len(win_best_final))
    print("Spread", spread_best_final, len(spread_best_final))
    print("Total", total_best_final, len(total_best_final))
    if win_best_ev > total_best_ev and win_best_ev > spread_best_ev:
        return win_best_final
    elif spread_best_ev > win_best_ev and spread_best_ev > total_best_ev:
        # Concatenating the spreadou to the spread and deleting the original spreadou so all the lists are the same length
        print("Hi!", str(spread_best_final[5]))
        spread_best_final[3] = str(spread_best_final[5]) + ' (' + str(spread_best_final[3]) + ')'
        spread_best_final[4] = str(spread_best_final[6]) + ' (' + str(spread_best_final[4]) + ')'
        del spread_best_final[5]
        del spread_best_final[5]
        
        return spread_best_final
    elif total_best_ev > win_best_ev and total_best_ev > spread_best_ev:
        # Concatenating the total over under to the total and deleting the original over under so all the lists are the same length
        total_best_final[3] = str(total_best_final[5]) + ' (' + str(total_best_final[3]) + ')'
        total_best_final[4] = str(total_best_final[6]) + ' (' + str(total_best_final[4]) + ')'
        del total_best_final[5]
        del total_best_final[5]

        return total_best_final
    else:
        return None



# TODO ADD 2 '', into the win list so they are all 13 length or whatever length.
# For Pick of the Day use both values into the decimal so even if it's win it won't matter. Then we should be able to hook up the animated feature to that.
# PUSH or POP or whatever syntax it is onto a list using the same way I found the BEST, take the 3 best of each. Uhhhhh this won't quite work. But I'm close to a breakthrough here. Keep at it for a bit! 




