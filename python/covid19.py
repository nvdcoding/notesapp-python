import requests
from terminaltables import AsciiTable
import time
import schedule
# def getNation(key, world):
# 	for nation in world:
# 		if nation['Country'] == key:
# 			return nation
def main():
	result = requests.get('https://api.covid19api.com/summary')
	#globalInfor = result.json()['Global']
	localInfor  =  result.json()['Countries']
	table_data = [
    	['Quốc Gia','Ca nhiễm mới', 'Tổng ca nhiễm', 'Mới tử vong', 'Tổng tử vong', 'Mới hồi phục', 'Tổng hồi phục']
	]
	for nation in localInfor:
		dataList = [nation['Country'], nation['NewConfirmed'], nation['TotalConfirmed'], nation['NewDeaths'], nation['TotalDeaths'], nation['NewRecovered'], nation['TotalRecovered']]
		table_data.append(dataList)
	table = AsciiTable(table_data)
	print(table.table)
schedule.every().day.at("08:30").do(main)
main()
while True:
	schedule.run_pending()
	time.sleep(1)