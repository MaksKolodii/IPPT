print ("Hello World")
slogan = str(input ("Write your sentence "))
sentence = slogan [::-1]
world = sentence.split()
sentence_rev = " ".join(reversed(world))
print (sentence_rev)