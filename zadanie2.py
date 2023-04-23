sentence  = input("Podaj zdanie: ")
sentence2 = sentence.split(' ')
print(' '.join(sentence2[-1::-1]))