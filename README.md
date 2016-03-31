pyCalculater
=============

This is a calculator in Python

Have fun with it~

###[Class] Calculator:

####Quick view:

-Calculation logic
-Button clicked event
-Store number for Calculation

####Param:

-current :

current number use to calculate.

-store   :

store number to be op with the next current.

-new_num :

if the number is new, put the current into store.

-combo   :

execute using two ops. ex: 2+2 '+'

-op      :

store operation

####Method:
-num_press(num)

accept parameters : numbers

-oper(op)

accept parameters : '+', '-', '\*', '/'

-execute()

execute with 'store' 'op' 'current' pattern, and save the result to [ResultBox].

-final()

trigger while '=' is clicked.

-display(number)

display number to [text_box].

-clear()

C button,clear current

-all_clear()

AC button

###[Class] ResultBox:

####Quick view:
-Result box logic
####Param:
none

####Method:
-clicked(event)
trigger when user clicked on a list item, should be bind with <ButtonRelease-1>.
-clear()
clear the result box
