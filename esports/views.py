from django.shortcuts import render
from django.http import HttpResponse

from .models import LolWin, LolSpread, LolTotal
from esports import appfunctions 

# Create your views here.

def league_of_legends(request):
    #spread_scores = Lol.objects.exclude(spread1__exact='') # And this works much better!

    win_scores = LolWin.objects.all()
    spread_scores = LolSpread.objects.all()
    total_scores = LolTotal.objects.all()

    # Win lists for progress bars
    win1_progress_bar_ev = appfunctions.int_from_float(win_scores, 'win1_ev')
    win2_progress_bar_ev = appfunctions.int_from_float(win_scores, 'win2_ev')

    win1_progress_bar_decimal = appfunctions.int_from_float(win_scores, 'win1_decimal')
    win2_progress_bar_decimal = appfunctions.int_from_float(win_scores, 'win2_decimal')

    # Spread lists for progress bars
    spread1_progress_bar_ev = appfunctions.int_from_float(spread_scores, 'spread1_ev')
    spread2_progress_bar_ev = appfunctions.int_from_float(spread_scores, 'spread2_ev')

    spread1_progress_bar_decimal = appfunctions.int_from_float(spread_scores, 'spread1_decimal')
    spread2_progress_bar_deciaml = appfunctions.int_from_float(spread_scores, 'spread2_decimal')

    # Total lists for progress bars
    total1_progress_bar_ev = appfunctions.int_from_float(total_scores, 'total1_ev')
    total2_progress_bar_ev = appfunctions.int_from_float(total_scores, 'total2_ev')

    total1_progress_bar_decimal = appfunctions.int_from_float(total_scores, 'total1_decimal')
    total2_proress_bar_decimal = appfunctions.int_from_float(total_scores, 'total2_decimal')

    

    # Best Tab and Pick of the Day ----------------------------------
    pick_of_the_day = appfunctions.pick_of_day(win_scores, spread_scores, total_scores)

    print(pick_of_the_day)
    print(len(pick_of_the_day)) # Length of 13 means Spread or Total, Length or 11 means Win.


    
        

        


        # No. Skip this sorted thing, maybe use it for best tab. 
        # Instead, grab all values, compare spread 1 and spread 2, keep the highest, do the next values, repeat. At the end compare the highest spread, win, and total.
        # Use that for best tab.

    
    #print(spread1ev)
    #print(spread2ev)

    #print(best)
        
            # Append this into a list, sort by highest. Done. 


    win_lists = zip(win_scores, win1_progress_bar_ev, win2_progress_bar_ev, win1_progress_bar_decimal, win2_progress_bar_decimal)
    spread_lists = zip(spread_scores, spread1_progress_bar_ev, spread2_progress_bar_ev, spread1_progress_bar_decimal, spread2_progress_bar_deciaml)
    total_lists = zip(total_scores, total1_progress_bar_ev, total2_progress_bar_ev, total1_progress_bar_decimal, total2_proress_bar_decimal)
    #picks = zip(pick_of_the_day)



    return render(request, 'esports/league-of-legends.html', {'win_zip': win_lists, 'total_zip': total_lists, 'spread_zip': spread_lists, 'day_pick': pick_of_the_day})






