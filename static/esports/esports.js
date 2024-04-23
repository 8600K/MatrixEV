/* Working static file */



function HelloYou() {
    alert("Hello World!!!!!");
}

// Variables used by oddsConverter
var savedSpread = [];
var savedWin = [];
var savedTotal = [];


function work() {
    alert(savedScores);
}


function convertOdds() {
    let checkBox = document.getElementById('odds-switch');
    let spreadTexts = document.getElementsByClassName('scores-spread');
    let winTexts = document.getElementsByClassName('scores-win');
    let totalTexts = document.getElementsByClassName('scores-total');
    let oddsText = document.getElementById('odds-text');
    let initial_text = '';
    let converted_text = '';

    // TODO I need to make sure initial data from algorithm is rounded
    // This lets us know where we are with the checkbox
    if (checkBox.checked) {
        oddsText.textContent = 'American Odds'

        // First we loop through all the spreadTexts length or range. We then grab the spread text tag from query selector (Note: The (+1.5) or (4.5) is NOT part of spread-text. Made things much eaiser.)
        // Then we send spreadText which contains the query selector spreadtext.textContent and the actual number we want it to be changed to to animateOdds. Simple as that!
        // This first for loop is Spread
        for (let i = 0; i < spreadTexts.length; i++) {
            let spreadText = spreadTexts[i].querySelector('#spread-text');
            initial_text = spreadText.textContent;
            if (initial_text >= 2) {
                converted_text = ((initial_text - 1) * 100)
            } else {
                converted_text = (-100 / (initial_text - 1))
            }
            // Saves the decimal odds to a list and then animates to American
            savedSpread.push(initial_text) 
            animateOdds(spreadText, converted_text)
        }

        // Win
        for (let i = 0; i < winTexts.length; i++) {
            let winText = winTexts[i].querySelector('#win-text');
            initial_text = winText.textContent;
            if (initial_text >= 2) {
                converted_text = ((initial_text - 1) * 100)
            } else {
                converted_text = (-100 / (initial_text - 1))
            } 
            // Saves the decimal odds to a list and then animates to American
            savedWin.push(initial_text)
            animateOdds(winText, converted_text)
        }

        // Total
        for (let i = 0; i < totalTexts.length; i++) {
            let totalText = totalTexts[i].querySelector('#total-text');
            initial_text = totalText.textContent;
            if (initial_text >= 2) {
                converted_text = ((initial_text - 1) * 100)
            } else {
                converted_text = (-100 / (initial_text - 1))
            } 
            // Saves the decimal odds to a list and then animates to American
            savedTotal.push(initial_text)
            animateOdds(totalText, converted_text)
        }
        

        
    } else {
        oddsText.textContent = 'Decimal Odds'
        // This means we are converting from American back to the original. I could have used the formula for converting American to decimal however
        // There can be rounding errors and other such issues. Ultimately I settled on using a list containing the decimal data to animate. 
        for (let i = 0; i < spreadTexts.length; i++) {
            let spreadText = spreadTexts[i].querySelector('#spread-text');
            animateOdds(spreadText, savedSpread[i])
        }

        for (let i = 0; i < winTexts.length; i++) {
            let winText =winTexts[i].querySelector('#win-text');
            animateOdds(winText, savedWin[i])
        }

        for (let i = 0; i < totalTexts.length; i++) {
            let totalText = totalTexts[i].querySelector('#total-text');
            animateOdds(totalText, savedTotal[i])
        }

    }
    
    

}


// Handles the animation for shifting the text.
function animateOdds(elem, number) {

    let battery = {
    cycles: 0
    }

    anime({
    targets: battery,
    charged: number,
    cycles: number,
    round: 100,
    easing: 'linear',
    update: function() {
        /*Think we add the +1.5 (+/- ) Here */
        elem.innerText = `${battery.cycles}`;
    }
    });
}



/*
function refreshTable() {
    $.ajax({
        url: '/path/to/server',
        success: function(data) {
            $('#table-id').html(data);
        }
    });
}*/