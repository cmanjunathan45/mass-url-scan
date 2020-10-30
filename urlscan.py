import requests
def single():
	url=input("Enter the URL with HTTP : ")
	try:
		scan=requests.get(url)
		print(url," -------> ",scan.status_code)
	except:
		print(url," -------> URL Error")
def bulk():
	fileName=input("Enter The txt PATH : ")
	urList = open(fileName, 'r')
	url=(urList.readlines())
	for i in range(len(url)):
		a=url[i]
		a=a.replace("\n","")
		a="http://"+a
		try:
			scan=requests.get(a)
			print(a," -------> ",scan.status_code)
		except:
			print(a," -------> URL Error")
def main():
	choice=input("Which Action You Want to Perform : \n1.Single URL\n2.Bulk URL Scan\n")
	if(choice=="1"):
		single()
	elif(choice=="2"):
		bulk()
	else:
		print("Choose 1 or 2 Only\nThank You")
		exit()
main()