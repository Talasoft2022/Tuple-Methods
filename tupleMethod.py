 #Akeem Abiodun 
#Creating a sample tuple

sample_tuple = (1,5,9,2)

#performing tuple methods

#1. Index() method
item_index = sample_tuple.index(2)
print(item_index)
# output : 3


#2. Len() method
tuple_length = len(sample_tuple)
print (tuple_length)

#output: 4

#3. Count() method
item_count= sample_tuple.count(2)
print(item_count)

#output: 1

#4. Slice() method
sliced_tuple = sample_tuple[1:3]
print(sliced_tuple)

#output: (5,9)

#5. Repetition method
repeated_tuple = sliced_tuple * 3
print(repeated_tuple)

#output: (5,9,5,9,5,9)

#6 reversed() method

reversed_tuple= reversed(sample_tuple)
#converting the iterator to a tuple we use the tuple() function
print(tuple(reversed_tuple))

#output: (2,9,5,1)
