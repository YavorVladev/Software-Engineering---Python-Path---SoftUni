dlj_cm = int(input())
shir_cm = int(input())
vis_cm = int(input())
procent = float(input()) / 100

obem = dlj_cm * shir_cm * vis_cm
obem_v_litri = obem / 1000

zaet_prost = obem_v_litri * procent
nujni_litri = obem_v_litri - zaet_prost
print(nujni_litri)