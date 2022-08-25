given_string = """One morning, when Gregor Samsa woke from troubled dreams, 
he found himself transformed in his bed into a horrible vermin.
 He lay on his armour-like back, and if he lifted his head a 
little he could see his brown belly, slightly domed and divided by 
arches into stiff sections. The bedding was hardly able to cover 
it and seemed ready to slide off any moment. His many legs, pitifully 
thin compared with the size of the rest of him, waved about helplessly 
as he looked."""

first_index = given_string.index("Gregor")
string_length = len("Gregor")
second_index = first_index+string_length
user_name = (given_string[first_index:second_index])
print(user_name)

h = given_string.index("H")
e = given_string.index("e")
l = given_string.index("ll")
o = given_string.index("o")

Hello = (given_string[h]
        +given_string[e]
        +given_string[l]
        +given_string[l]
        +given_string[o])

print(Hello,user_name)




