def make_local_variable():
    local_variable = "I can only exist inside this function"
    print(local_variable)

make_local_variable()

#print the local value
#make sure to name the error 'local_value" is not going to be defined

def make_and_return_value():
    local_value = "I was created inside the function"
    return local_value

outer_value = make_and_return_value()
print(outer_value)
