"""Dado um vetor de 20 elementos, divida este em dois sub-vetores de 10 elementos"""
vetor = list(range(20))

sub1 = []
sub2 = []

for i in range(len(vetor)):
    if i < 10:
        sub1.append(vetor[i])
    elif i >= 10:
        sub2.append(vetor[i])

print(f"Vetor original{vetor}")
print()
print(f"Subvetor 1: {sub1}\n"
      f"Subvetor 2: {sub2}")

print(len(sub2))
