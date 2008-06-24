wordline = open("words.txt","r").readlines()[0]
words = [word[1:-1] for word in wordline.split(',')]

def score(contestant):
  return sum([ord(c) - 64 for c in contestant])

def triangle(n):
  return int(.5*n*(n+1))

triangles = [1]
biggest = max([score(word) for word in words])
while (max(triangles) < biggest):
  triangles.append(triangle(len(triangles)+1))

passes = [word for word in words if (score(word) in triangles)]
print len(passes)