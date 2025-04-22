stock_prices = {'amzn':500,'tsla':900,'goog':790,99:100}
print(stock_prices)
print(stock_prices['tsla'])
print(stock_prices[99])

# add a new element/update a new element 
stock_prices.update({'tsla':990})
print(stock_prices)
stock_prices['banknifty']=660
print(stock_prices)

#deleting the key value pair from the dictionary new way and old way explained below 
stock_prices.pop('amzn')
print(stock_prices)
del stock_prices['tsla']
print(stock_prices)

#now again add both using new way wand old way 
stock_prices.update({'amzn':500})
print(stock_prices)
stock_prices['tsla']=990
print(stock_prices)

#calling or getting the value - new way 
print(stock_prices.get(('goog')))

#calling or getting the value - old way 
print(stock_prices['tsla'])

#value keys items 
print(list(stock_prices.keys()))
print(list(stock_prices.values()))
print(list(stock_prices.items()))

#sets

s1={1,2,3}
print(s1)
print(type(s1)) # This shows that it is a class set 

# Another way of creating a set

s2=([4,5,6])
print(s2)
print(type(s2))

# sets will always return the value one time i.e. it wont allow duplicate values 

s3={1,2,2,3,4,5,5,6}
print(s3)
s3.pop()  #removes the 1st value
print(s3)

#add and remove elements in set

s3.add(7)
s3.remove(4)
print(s3)

#split and join 
l1=['abc','def','ghi']
print(l1)
ans1='-'.join(l1)
print(ans1) 
# so join function takes the list and returns the string 
# the split function takes the string and returns the list 

l2='abcdefghi'
ans2=l2.split('f')
print(ans2)

# in the above function f will be removed 

#truthy value and falsy value
a= 5=6
print(a)
if a:
    print('inside if')
else:
    print('inside else')

#following are the falsy values 0, False, [],{},(),""
#when you compare 2 things you will get a boolean value

#one more way of how truthy and falsy values are obtained 
stock_prices={'amzn':500,'tsla':900,'goog':900,99:100}
print(stock_prices)
