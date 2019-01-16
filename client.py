from ftplib import FTP


ftp = FTP('')
# connect server
ftp.connect('localhost',1026)
# try to login
ftp.login()
# setting the path
ftp.cwd('directory_name') 
ftp.retrlines('LIST')

# prepare for upload file
def uploadFile():
  # set file name   
  filename = 'testfile.txt' 
  # file store 
  ftp.storbinary('STOR '+filename, open(filename, 'rb'))
  ftp.quit()

# prepare for download file
def downloadFile():
 filename = 'testfile.txt' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

uploadFile()
#downloadFile()