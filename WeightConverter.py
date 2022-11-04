ansWeight = input("Hur mycket väger du?")
ansKorL = input("Är det i (K)g eller (L)bs?")

if ansKorL == "l" or ansKorL == "L":
    weightKg = float(ansWeight) / 2.2
    print("Din vikt i Kg är", weightKg)
else:
    weightLbs = float(ansWeight) * 2.2
    print("Din vikt i Lbs är", weightLbs)
    

    