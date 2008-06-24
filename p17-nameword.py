W = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}

for tengroup in [(20,'twenty'),(30,'thirty'),(40,'forty'),(50,'fifty'),(60,'sixty'),(70,'seventy'),(80,'eighty'),(90,'ninety')]:
  W[tengroup[0]] = tengroup[1]
  for i in xrange(1,10):
    W[tengroup[0]+i] = '-'.join([tengroup[1],W[i]])

for i in xrange(1,10):
  W[i*100] = ' '.join([W[i],'hundred'])
  for j in xrange(1,100):
    W[i*100 + j] = ' and '.join([W[i*100], W[j]])
    
W[1000] = "one thousand"

print sum([len(word.replace(" ","").replace("-","")) for word in W.values()])

sum(D.values())

len('ninety')