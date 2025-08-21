import pandas as pd
from slugify import slugify
import subprocess,os
IMG_width='200'
WIDTH_dir='w'+IMG_width
IMG_extension='jpeg'

new_image_path='/Users/ruiz/projects/catalogo.simple/data/imgs/products/original'
if not os.path.exists(new_image_path):
	os.makedirs(new_image_path)

fname='../data/productos.WP'

# df=ReadImagesFromCSV(fname);
# CopyImages(df,new_image_path);
# SlugifyImagesToCSV(fname+'-slug',df);
ResizeImages(new_image_path);
# AddWebPathToImages(fname+'-slug')

#WordPress read
def ReadImagesFromCSV(fname):
	df = pd.read_csv(fname+'.csv', comment='#')
	#me quedo solo con la primer imagen (están separados por '|')
	df['images']=df['images'].apply(lambda x: x.split('|')[0])
	return df

def SlugifyImagesToCSV(fname,df):
	# todas las imagenes con nombradas como el titulo pero con slug
	df['images']=df['title'].apply(lambda x: slugify(x)+'.'+IMG_extension)
	# todas las imagenes con la misma extensión	
	df.to_csv(fname+'.csv', index=False, header=True)


#WordPress read
def AddWebPathToImages(fname):
	web_path='https://www.janus.bio/almacen/imgs/products/'+WIDTH_dir+'/'
	df = pd.read_csv(fname+'.csv', comment='#')
	#me quedo solo con la primer imagen (están separados por '|')
	df['images']=df['images'].apply(lambda x: web_path+x)
	df.to_csv(fname+'-web.csv', index=False, header=True)


def CopyImages(df,destination):
	web_path='https://www.janus.bio/wp-content/uploads/products'
	src_path='/Users/ruiz/projects/catalogo.simple/data/products'
	src_path='/Users/ruiz/projects/janus/nuthost/public/wp-content/uploads'
	import subprocess
	images=df['images'].values.tolist()
	images=[image.replace(web_path,src_path) for image in images]
	# todas las imagenes con nombradas como el titulo pero con slug
	slugs=df['title'].apply(lambda x: slugify(x)).values.tolist()
	for i,image in enumerate(images):
		extension=image.split('.')[-1]
		if extension=='jpg':
			extension='jpeg'
		if extension != IMG_extension:
			print(slugs[i],image)
			command='convert'
		else:
			command='cp'
		new_file=destination+'/'+slugs[i]+'.'+IMG_extension
		subprocess.run([command, image, new_file])

def ResizeImages(input_dir):	
	output_dir=input_dir+'/../'+WIDTH_dir
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
	#https://www.smashingmagazine.com/2015/06/efficient-image-resizing-with-imagemagick/
	command_string="mogrify -path "+output_dir+" -filter Triangle -define filter:support=2 -thumbnail "+IMG_width+" -unsharp 0.25x0.08+8.3+0.045 -dither None -posterize 136 -quality 82 -define jpeg:fancy-upsampling=off -define png:compression-filter=5 -define png:compression-level=9 -define png:compression-strategy=1 -define png:exclude-chunk=all -interlace none -colorspace sRGB "+input_dir+'/*.'+IMG_extension
	command=command_string.split(' ')
	subprocess.run(command)


