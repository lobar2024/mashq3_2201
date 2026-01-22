sonlar = list(map(int, input().split()))

eng_katta = sonlar[0]
eng_kichik = sonlar[0]

for s in sonlar:
    if s > eng_katta:
        eng_katta = s
    if s < eng_kichik:
        eng_kichik = s

print("Eng katta:", eng_katta)
print("Eng kichik:", eng_kichik)
