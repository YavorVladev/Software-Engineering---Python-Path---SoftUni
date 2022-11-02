dep_suma = int(input())
srok_meseci = int(input())
godishen_procent = float(input()) / 100

natr_lihva = dep_suma * godishen_procent
mesec_lihva = natr_lihva / 12
obhsta_suma = dep_suma + srok_meseci * mesec_lihva
print(obhsta_suma)