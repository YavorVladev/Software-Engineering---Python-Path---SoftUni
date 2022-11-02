kv_m_price = 7.61
kv_m_house = float(input()) * kv_m_price
disc = 0.18 * kv_m_house
final = kv_m_house - disc
print(f"The final price is: {final} lv.")
print(f"The discount is: {disc} lv.")