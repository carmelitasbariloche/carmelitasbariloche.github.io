import sys

from pathlib import Path
home = str(Path.home())

# sys.path.append(home+'/projects/catalogo.simple/src')


import myfuncs as my


def main():
	import render
	#render.main()

	# conf_original=my.join('config/conf.py','config/conf_jorge.py')
	conf_original=my.join('config/conf.py')
	
	render.main()

	with open ('config/conf.py', 'w') as fp:
		fp.write(conf_original)


if __name__ == "__main__":
	main()


	# original=join('config/jorge_conf.py','config/conf.py','config/conf.py')
	# main()

	# with open ('config/conf.py', 'w') as fp:
	# 	fp.write(original)
