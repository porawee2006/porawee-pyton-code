#Personal Finance Calculator
#Student: Porawee Lammana
#Date: 27/07/2568
#Purpose: Calculate monthly budget and savings

income = float(input("User's monthly income in (THB): "))
rent = float(input("Monthly rent/housing cost: "))
food = float(input("Monthly food budget in (THB): "))
transportation = float(input("Monthly transportation expenses: "))
entertainment = float(input("Monthly entertainment budget: "))
emergency_percent = float(input("Percentage to save for emergency : "))
investment_percent = float(input("Percentage to invest : "))
#รับ input ข้อมูลจากผู้ใช้

Total_Fixed = rent + transportation
Total_Variable = food + entertainment
Total_Expenses = Total_Fixed + Total_Variable
Remaining_Income = income - Total_Expenses
EmergencyFund = income * (emergency_percent / 100)
Investment = income * (investment_percent / 100)
Available_Savings = Remaining_Income - EmergencyFund - Investment
Expense_Ratio = (Total_Expenses / income) * 100
#เป็นที่คำนวนข้อมูลที่ได้รับมาจากการ input

print("\n=== MONTHLY BUDGET REPORT ===")  # รายงานงบประมาณรายเดือน
print(f"Income: {income:.2f} THB")  # แสดงรายได้ต่อเดือน
print(f"Fixed Expenses: {Total_Fixed:.2f} THB")  # แสดงค่าใช้จ่ายคงที่
print(f"Variable Expenses: {Total_Variable:.2f} THB")  # แสดงค่าใช้จ่ายผันแปร
print(f"Total Expenses: {Total_Expenses:.2f} THB")  # แสดงค่าใช้จ่ายทั้งหมด
print(f"Remaining: {Remaining_Income:.2f} THB")  # แสดงรายได้ที่เหลือ

print("\n=== SAVINGS BREAKDOWN ===")  # แสดงรายละเอียดเงินเก็บออม
print(f"Emergency Fund ({emergency_percent}%): {EmergencyFund:.2f} THB")  # แสดงจำนวนเงินสำหรับกองทุนฉุกเฉิน
print(f"Investments ({investment_percent}%): {Investment:.2f} THB")  # แสดงจำนวนเงินสำหรับการลงทุน
print(f"Available for Savings: {Available_Savings:.2f} THB")  # แสดงจำนวนเงินที่สามารถเก็บออมได้

print("\n=== ANALYSIS ===")  # วิเคราะห์งบประมาณ
print(f"Expense Ratio: {Expense_Ratio:.2f}%")  # คำนวนสัดส่วนค่าใช้จ่ายต่อรายได้