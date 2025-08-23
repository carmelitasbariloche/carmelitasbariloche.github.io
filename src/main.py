import sys

from pathlib import Path
home = str(Path.home())

# sys.path.append(home+'/projects/catalogo.simple/src')


import myfuncs as my




def main(arg1):
	import render
	#render.main()

	#genero el json-conf+conf-original
	if arg1 != '':
		conf_original=my.join('config/conf.py','config/'+arg1+'.py')
	else:
		conf_original=my.join('config/conf.py')
	
	render.main()

	#regenero el conf original
	with open ('config/conf.py', 'w') as fp:
		fp.write(conf_original)


if __name__ == "__main__":
	if len(sys.argv) == 2:
		argument1 = sys.argv[1]
	else:
		argument1 = ''
	main(argument1)


	# original=join('config/jorge_conf.py','config/conf.py','config/conf.py')
	# main()

	# with open ('config/conf.py', 'w') as fp:
	# 	fp.write(original)
