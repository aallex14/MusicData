import tarfile
import os

for filename in os.listdir():
    if filename.endswith(".tar.gz"): 
		tar=tarfile.open(filename) 
		name = tar.getnames()
		if os.path.isdir(file_name):
			pass
		else:
			os.mkdir(file_name)
		tar.extract(name, file_name + "_files/")

# for root,dir,files in os.walk('/path/to/dir/'):  
#     for file in files:  
#      	fullpath=os.path.join(root,file)
#      	tar.add(fullpath,arcname=file)  
# tar.close()  

# t = tarfile.open("/path/to/your.tar", "r:")  
# t.extractall(path = '/path/to/extractdir/')  
# t.close()

# def un_tar(file_name):
#     """untar zip file"""
#     tar = tarfile.open(file_name)
#     names = tar.getnames()
#     # 后面新建文件夹,先判断是否存在.
#     if os.path.isdir(file_name + "_files"):
#         pass
#     else:
#         os.mkdir(file_name + "_files")
#     #由于解压后是许多文件，预先建立同名文件夹
#     for name in names:
#         tar.extract(name, file_name + "_files/")
#     tar.close()
#         # print(os.path.join(directory, filename))
