def shout(text):
    return text.upper()
 
print(shout('Hello'))

yell = shout
print(yell('Hello'))

 
def whisper(text):
    return text.lower()
 
def greet(func):
    greeting = func("Hi, I am created by a function passed as an argument.")
    print (greeting)
 
greet(shout)
greet(whisper)