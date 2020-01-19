type_of_pppl=10
x=f"There are {type_of_pppl} type of people"

binary=f"Binary"
do_not=f"don't"
y=f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious=False
joke_evaluation="Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w="This is the left side of.....0"
e="a string with a right side"
print(w+e)