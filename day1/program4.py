cp = eval( input( " Cost Price : "))
sp = eval( input( " Selling Price : "))
profit = sp - cp
new_profit =  profit + 0.05*profit
new_sp = new_profit + cp

print(" Profit : {} \n New SP : {}".format(profit , new_profit))

