#encoding: UTF-8

import sys, os, cores, translate
from baterry import *
from numbers import *
from datetime import date
from datetime import datetime



def help():
	global global_help, help_c_note, help_d_note
	global_help = "Python Clock\n\nOptions:\n\n-h, --help\t\tShow this msg\n-n\t\t\tAdd new notes\n-d\t\t\tDelete a note\n--delete-all\t\tDelete all notes\n\n"
	help_c_note = "Exemple: python clock.py -n <1-3> '15h Get milk'"
	help_d_note = "Exemple: python clock.py -d <1-3>"

help()

def anot():
	os.system("echo $HOME > /tmp/.home")

	global home
	home = open("/tmp/.home").read().replace("\n", "")

	try:
		arg = sys.argv[1]

		if arg == "-n":
			try:
				note = sys.argv[2]
				data = sys.argv[3]
			except:
				print help_c_note
				exit(0)

			if note == "1":
				file = open(home+"/.clock/note1", 'w')
				file.write(data)
				file.close()

			elif note == "2":
				file = open(home+"/.clock/note2", 'w')
				file.write(data)
				file.close()

			elif note == "3":
				file = open(home+"/.clock/note3", 'w')
				file.write(data)
				file.close()

			else:
					print help_c_note
					exit(0)

		elif arg == "-d":
			try:
				note = sys.argv[2]
			except:
				print help_d_note
				exit(0)

			if note == "1":
				file = open(home+"/.clock/note1", 'w')
				file.close()

			elif note == "2":
				file = open(home+"/.clock/note2", 'w')
				file.close()

			elif note == "3":
				file = open(home+"/.clock/note3", 'w')
				file.close()

			else:
				print help_d_note
				exit(0)

		elif arg == "--delete-all":

			file = open(home+"/.clock/note1", 'w')
			file.close()

			file = open(home+"/.clock/note2", 'w')
			file.close()

			file = open(home+"/.clock/note3", 'w')
			file.close()

		elif arg == "-h" or arg == "--help":
			print global_help
			exit(0)

		else:
				print "Command ["+str(sys.argv[1])+"] not found"
				exit(0)

	except Exception as erro:
#		print erro
		None


def baterry():
	os.system("acpi > /tmp/.level 2> /tmp/.level")

	if os.path.exists(home+"/.clock") == False:
		os.mkdir(home+"/.clock")

	if os.path.exists(home+"/.clock/note1") == False:
		file = open(home+"/.clock/note1", 'w')
		file.close()
	if os.path.exists(home+"/.clock/note2") == False:
		file = open(home+"/.clock/note2", 'w')
		file.close()
	if os.path.exists(home+"/.clock/note3") == False:
		file = open(home+"/.clock/note3", 'w')
		file.close()

	note1 = open(home+"/.clock/note1").read().replace("\n", "")
	note2 = open(home+"/.clock/note2").read().replace("\n", "")
	note3 = open(home+"/.clock/note3").read().replace("\n", "")

	os.system("date > /tmp/.date")
	level = open("/tmp/.level", 'r').read()
	data = open("/tmp/.date").read().split(" ")

	d = translate.day(data[0])
	m = translate.month(data[2])
	m_number = str(date.today()).replace('-', '/')

	data = d.day+" "+m.month+" | "+m_number

	if "not found" in level:
		print "Pls install [acpi]"
		exit(0)

	elif 'No support' in level:
		porc = "pc"
		ba = pc()
		col = cor.negrito+cor.verde
                sys.stderr.write(col+ba.n1+cor.finaliza+"\t\t         "+cor.negrito+str(data)+cor.finaliza+'\n'+col+ba.n2+'\n'+ba.n3+cor.finaliza+cor.negrito+"Note: "+str(note1)+cor.finaliza+col+'\n'+ba.n4+'\n'+ba.n5+cor.finaliza+cor.negrito+"Note: "+str(note2)+cor.finaliza+col+'\n'+ba.n6+'\n'+ba.n7+cor.finaliza+cor.negrito+"Note: "+str(note3)+cor.finaliza+col+'\n'+ba.n8+'\n'+ba.n9+cor.finaliza+"\n")

	else:
			porc = str(level.split(" ")[3].replace("%", "").replace(",", "").replace("\n", ""))
			print level
			if level.split(" ")[2] == "Charging,":
				icon = "↑"
			elif level.split(" ")[2] == "Full,":
				icon = ""
			else:
				icon = "↓"

			if int(porc) >= 0 and int(porc) <= 10:
					ba = solow()
					col = cor.negrito+cor.vermelho
			elif int(porc) >= 11 and int(porc) <= 20:
					ba = low()
					col = cor.vermelho
			elif int(porc) >= 21 and int(porc) <= 60:
					ba = good()
					col = cor.amarelo
			elif int(porc) >= 41 and int(porc) <= 99:
					ba = sogood()
					col = cor.verde
			elif int(porc) == 100:
					ba = full()
					col = cor.negrito+cor.verde

			sys.stderr.write(col+ba.n1+cor.finaliza+"\t\t         "+cor.negrito+str(data)+cor.finaliza+'\n'+col+ba.n2+'\n'+ba.n3+cor.finaliza+cor.negrito+"Note: "+str(note1)+cor.finaliza+col+'\n'+ba.n4+'\n'+ba.n5+cor.finaliza+cor.negrito+"Note: "+str(note2)+cor.finaliza+col+'\n'+ba.n6+'\n'+ba.n7+cor.finaliza+cor.negrito+"Note: "+str(note3)+cor.finaliza+col+'\n'+ba.n8+'\n'+ba.n9+cor.finaliza+"\n"+"    "+cor.negrito+icon+porc+"%\n"+cor.finaliza)


def ttime():

	time = datetime.now()

	global hour,minu,seco

	hour = str(time.hour)

	if hour == "24":
		hour = "00"

	minu = str(time.minute)
	seco = str(time.second)

	if len(str(hour)) == 1:
		hour = '0'+str(hour)
        if len(str(minu)) == 1:
                minu = '0'+str(minu)
        if len(str(seco)) == 1:
                seco = '0'+str(seco)



def hou():
	ttime()

	if hour[0] == '0':
		num = zero()

	elif hour[0] == '1':
		num = one()

	elif hour[0] == '2':
        	num = two()

    	elif hour[0] == '3':
		num = thr()

	elif hour[0] == '4':
		num = fou()

    	elif hour[0] == '5':
		num = fiv()

    	elif hour[0] == '6':
		num = six()

	elif hour[0] == '7':
		num = sev()

    	elif hour[0] == '8':
		num = eig()

    	elif hour[0] == '9':
		num = nin()

	global h11,h12,h13,h14,h15,h16,h17,h18,h19

	h11 = num.n1
	h12 = num.n2
	h13 = num.n3
	h14 = num.n4
	h15 = num.n5
	h16 = num.n6
	h17 = num.n7
	h18 = num.n8
	h19 = num.n9


    	if hour[1] == '0':
            	num = zero()

    	elif hour[1] == '1':
            	num = one()

    	elif hour[1] == '2':
            	num = two()

    	elif hour[1] == '3':
            	num = thr()

    	elif hour[1] == '4':
            	num = fou()

    	elif hour[1] == '5':
            	num = fiv()

      	elif hour[1] == '6':
            	num = six()

    	elif hour[1] == '7':
            	num = sev()

    	elif hour[1] == '8':
            	num = eig()

    	elif hour[1] == '9':
            	num = nin()

    	global h21,h22,h23,h24,h25,h26,h27,h28,h29

    	h21 = str(num.n1)
    	h22 = str(num.n2)
    	h23 = str(num.n3)
    	h24 = str(num.n4)
    	h25 = str(num.n5)
    	h26 = str(num.n6)
    	h27 = str(num.n7)
    	h28 = str(num.n8)
    	h29 = str(num.n9)




def min():
        hou()

        if minu[0] == '0':
                num = zero()

        elif minu[0] == '1':
                num = one()

        elif minu[0] == '2':
                num = two()

        elif minu[0] == '3':
                num = thr()

        elif minu[0] == '4':
                num = fou()

        elif minu[0] == '5':
                num = fiv()

        elif minu[0] == '6':
                num = six()

        elif minu[0] == '7':
                num = sev()

        elif minu[0] == '8':
                num = eig()

        elif minu[0] == '9':
                num = nin()


	global m11,m12,m13,m14,m15,m16,m17,m18,m19,m21,m22,m23,m24,m25,m26,m27,m28,m29
        m11 = num.n1
        m12 = num.n2
        m13 = num.n3
        m14 = num.n4
        m15 = num.n5
        m16 = num.n6
        m17 = num.n7
        m18 = num.n8
        m19 = num.n9


        if minu[1] == '0':
                num = zero()

        elif minu[1] == '1':
                num = one()

        elif minu[1] == '2':
                num = two()

        elif minu[1] == '3':
                num = thr()

        elif minu[1] == '4':
                num = fou()

        elif minu[1] == '5':
                num = fiv()

        elif minu[1] == '6':
                num = six()

        elif minu[1] == '7':
                num = sev()

        elif minu[1] == '8':
                num = eig()

        elif minu[1] == '9':
                num = nin()

        m21 = str(num.n1)
        m22 = str(num.n2)
        m23 = str(num.n3)
        m24 = str(num.n4)
        m25 = str(num.n5)
        m26 = str(num.n6)
        m27 = str(num.n7)
        m28 = str(num.n8)
        m29 = str(num.n9)

def seg():
	min()

        if seco[0] == '0':
                num = zero()

        elif seco[0] == '1':
                num = one()

        elif seco[0] == '2':
                num = two()

        elif seco[0] == '3':
                num = thr()

        elif seco[0] == '4':
                num = fou()

        elif seco[0] == '5':
                num = fiv()

        elif seco[0] == '6':
                num = six()

        elif seco[0] == '7':
                num = sev()

        elif seco[0] == '8':
                num = eig()

        elif seco[0] == '9':
                num = nin()


        s11 = num.n1
        s12 = num.n2
        s13 = num.n3
        s14 = num.n4
        s15 = num.n5
        s16 = num.n6
        s17 = num.n7
        s18 = num.n8
        s19 = num.n9

        if seco[1] == '0':
                num = zero()

        elif seco[1] == '1':
                num = one()

        elif seco[1] == '2':
                num = two()

        elif seco[1] == '3':
                num = thr()

        elif seco[1] == '4':
                num = fou()

        elif seco[1] == '5':
                num = fiv()

        elif seco[1] == '6':
                num = six()

        elif seco[1] == '7':
                num = sev()

        elif seco[1] == '8':
                num = eig()

        elif seco[1] == '9':
                num = nin()

        s21 = str(num.n1)
        s22 = str(num.n2)
        s23 = str(num.n3)
        s24 = str(num.n4)
        s25 = str(num.n5)
        s26 = str(num.n6)
        s27 = str(num.n7)
        s28 = str(num.n8)
        s29 = str(num.n9)



	sys.stderr.write(cor.negrito+"--------------------------------------------------------------------------------\n\n"+cor.finaliza+h11+h21+"    "+m11+m21+"    "+s11+s21+'\n'+h12+h22+" ## "+m12+m22+" ## "+s12+s22+'\n'+h13+h23+" ## "+m13+m23+" ## "+s13+s23+'\n'+h14+h24+"    "+m14+m24+"    "+s14+s24+'\n'+h15+h25+"    "+m15+m25+"    "+s15+s25+'\n'+h16+h26+" ## "+m16+m26+" ## "+s16+s26+'\n'+h17+h27+" ## "+m17+m27+" ## "+s17+s27+'\n'+h18+h28+"    "+m18+m28+"    "+s18+s28+'\n'+h19+h29+"    "+m19+m29+"    "+s19+s29+cor.negrito+"\n\n--------------------------------------------------------------------------------\n"+cor.finaliza)

	baterry()
	print cor.negrito+"--------------------------------------------------------------------------------\n\n"+cor.finaliza
def init():
	anot()
	global cor
	cor = cores.cores()
	seg()


init()
