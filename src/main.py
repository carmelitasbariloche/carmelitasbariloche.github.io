import sys

from pathlib import Path
home = str(Path.home())

# sys.path.append(home+'/projects/catalogo.simple/src')


import myfuncs as my




def main(*args):
	import render
	#render.main()

	conf_original_fname='config/conf.py'
	conf_original_data=my.join(conf_original_fname)
	
	for i,arg in enumerate(args[0]):		
	#genero el arg1-conf+conf-original
		if arg != '' and i>0:
			# aca configuro el conf_original (ya modificado con arg1) agregandole arg2
			aux=my.join(conf_original_fname,'config/'+arg+'.py')

		
	render.main()

	#regenero el conf original
	with open (conf_original_fname, 'w') as fp:
		fp.write(conf_original_data)


if __name__ == "__main__":
	main(sys.argv)


	# original=join('config/jorge_conf.py','config/conf.py','config/conf.py')
	# main()

	# with open ('config/conf.py', 'w') as fp:
	# 	fp.write(original)
