paketi_himikali = int(input())
broi_markeri = int(input())
litri_preparat_za_duska = int(input())
procent_namalenie = int(input()) / 100

cena_himikali = paketi_himikali * 5.80
cena_markeri = broi_markeri * 7.20
cena_preparat = litri_preparat_za_duska * 1.20
obshta_cena = cena_himikali + cena_markeri + cena_preparat
cena_s_namalenie = obshta_cena - (obshta_cena * procent_namalenie)
print(cena_s_namalenie)