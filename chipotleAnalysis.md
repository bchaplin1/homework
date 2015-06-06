# Analysis of Chipotle data

<ol>
<li>  head and tail analysis
<ol>
<li> looks like well organized data with a header and organized domain.
I see several lines per order ID.  The quantity appears to be an integer value. The item name is a enumerated domain.  The choice description appears to be always missing.  I wonder what its purpose is and how useful it is.  Item price is currency format in dollars and is actually the item price times the quantity.
<li> Looking at the tail, it looks like a reasonable amount of data to fit in memory, 1834 orders. 
<li> 4,623 lines in the file which means that probably all the orders would be there of the 1 through 1834, at about 2 to three items per order which makes sense
<li>  Just by counting the lines, of the 1,172 burrito lines, 553 are chicken and 368 are steak.  So chicken is more popular which I prefer anyway so that makes a little sense to me. It's not weighted for quantity but probably the ratios of chicken to beef would still hold.
<li>  282 of the 553 chicken are black beans and 105 are pinto beans.  That adds up 387, hmm, seems too low.  But black beans are almost 3 times more popular that pinto.
</ol>
<li>  ls *.?sv
<li> looks like 4 occurrences in the ham file
</ol>



