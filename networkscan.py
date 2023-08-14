#SEBEKEYE AXTARIS TOOL-U
import scapy.all as sc
import optparse
def istifadeci_inputu():
    parser=optparse.OptionParser()
    parser.add_option("-i","--ip",dest="IP_UNVAN",help="IP unvan daxil etmek uchun istifade olunur")
    return parser.parse_args()

def input_yoxlama(IP_UNVAN):
    if not IP_UNVAN:
        IP_UNVAN=input("IP UNVANI daxil edin: ")
    return IP_UNVAN


def arp_paket(IP_UNVAN):
    arp_sorgu_paketi=sc.ARP(pdst=IP_UNVAN)
    broadcast_mac=sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    son_paket=broadcast_mac/arp_sorgu_paketi
    (answered,unanswered)=sc.srp(son_paket,timeout=1)
    print(answered.summary())

print("""
  _   _          _                               _         _____                                              
 | \ | |        | |                             | |       / ____|                                             
 |  \| |   ___  | |_  __      __   ___    _ __  | | __   | (___     ___    __ _   _ __    _ __     ___   _ __ 
 | . ` |  / _ \ | __| \ \ /\ / /  / _ \  | '__| | |/ /    \___ \   / __|  / _` | | '_ \  | '_ \   / _ \ | '__|
 | |\  | |  __/ | |_   \ V  V /  | (_) | | |    |   <     ____) | | (__  | (_| | | | | | | | | | |  __/ | |   
 |_| \_|  \___|  \__|   \_/\_/    \___/  |_|    |_|\_\   |_____/   \___|  \__,_| |_| |_| |_| |_|  \___| |_|   
                                                                                   BY: NICAT ABBASOV                                                                                                              
""")

(istifadeci_inputu,args)=istifadeci_inputu()
IP_UNVAN=input_yoxlama(istifadeci_inputu.IP_UNVAN)
arp_paket(IP_UNVAN)
