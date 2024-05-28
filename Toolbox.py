try:  
  import random , string
  import hashlib
  import re , phonenumbers
  import requests , socket , platform , psutil
  import time
  import wikipedia
  import qrcode
  import traceback
  from getmac import get_mac_address
  from datetime import datetime
  from deep_translator import GoogleTranslator
  from colorama import Fore , init , Back , Style

  init(autoreset=True)


  print(f"""{Fore.CYAN}
  _|_|_|_|_|                    _|      _|_|_|                        
      _|      _|_|      _|_|    _|      _|    _|    _|_|    _|    _|  
      _|    _|    _|  _|    _|  _|      _|_|_|    _|    _|    _|_|    
      _|    _|    _|  _|    _|  _|      _|    _|  _|    _|  _|    _|  
      _|      _|_|      _|_|    _|      _|_|_|      _|_|    _|    _| 
          """)
  date = datetime.now()
  gcelender = date.strftime('%Y/%m/%d - %H:%M:%S')
  print(f"{Fore.BLACK}Gregorion Date and Time:" + gcelender)
  while True:
    print(f"{Fore.YELLOW}Welvomr to Toolbox🖥️"
          "\n Choose Tool"
          "\n [0] Help"
          "\n [1] Redix Base Converter"
          "\n [2] Password Generator"
          "\n [3] Hash Generator"
          "\n [4] Validations"
          "\n [5] Search Tools"
          "\n [6] Link Tools"
          "\n [7] Your Computer Info"
          "\n [8] Exit")
    choose = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
    match choose:
      case 0:
        print(f"{Fore.MAGENTA} [*] Help:"
            "\n [*] Redix Base Convertor: conver Binary , Octal , Decimal , Hexadecimal Together"
            "\n [*] Password Generator: Create Strong Random Password or Custom Password"
            "\n [*] Hash Generator: Convert Text to MD5 , SHA1 , SHA256 , SHA512 Hash or Reverse"
            "\n [*] Validations: Check Validation of [+] National Code , Mobile Number , E-mail Address"
            "\n [*] Searching Tools: Translate , Wikipedia"
            "\n [*] Link Tools: Convert Link to Qrcode and Shorting Link"
            "\n [*] Your Computer Info: Show Your Computer Netwrok , OS , Software and Hardware Info"
            "\n")
        time.sleep(7)
        continue
      case 1:
        print(f"{Fore.YELLOW}Welcome to the Redix Base Converter")
        print(f"{Fore.YELLOW}choose Convetation"
          "\n [0] Help"
          "\n [1] Binary to Other"
          "\n [2] Octal to Other"
          "\n [3] Decimal to Other"
          "\n [4] Hexadecimal to Other"
          "\n [5] Fibonacchi Series"
          "\n [6] Back"
          "\n [7] Exit")
        check1 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
        match check1:
          case 0:
            print(f"{Fore.MAGENTA}[*] Help: "
              "\n [*] Binary to Other: Convert Binary Number to Octal , Decimal or Hexadecimal Number"
              "\n [*] Octal to Other: Convert Octal Number to Binary , Decimal or Hexadecimal Number"
              "\n [*] Decimal to Other: Convert Decimal Number to Binary , Octal or Hexadecimal Number"
              "\n [*] Hexadecimal to Other: Convert Hexadecimal Number to Binary , Octal or Decimal Number"
              "\n [*] Fibonacchi Series: Fibonacchi Numbers"
              "\n")
            time.sleep(7)
            continue
          case 1:
            # binary to other
            # bn = binary
            bn = list(input(f"{Fore.BLUE}Enter Binary Number: "))
            bnvalue = 0
            for i in range(len(bn)):
              bndigit = bn.pop()
              if bndigit == '1':
                bnvalue = bnvalue + pow(2 , i)
            print(f"{Fore.YELLOW}Convert Binary To"
                  "\n [1] Octal"
                  "\n [2] Decimal"
                  "\n [3] HexaDecimal"
                  "\n [4] Back"
                  "\n [5] Exit")
            #  check12 = check[1] 2
            check12 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
            match check12:
              case 1:
                print(f"{Fore.GREEN}Octal: " + oct(bnvalue))
                break
              case 2:
                print(f"{Fore.GREEN}Decimal: " + bnvalue)
                break
              case 3:
                print(f"{Fore.GREEN}Hexadecimal:" + hex(bnvalue))
                break
              case 4:
                continue
              case 5:
                break
              case _:
                print(f"{Fore.RED}[-] Wrong Selection!!")
                time.sleep(5)
          case 2:
            #  octal to other
            #  oc = octal
            oc = input(f"{Fore.BLUE}Enter Octal Number: ")
            ocvalue = int(oc , 8)
            print(f"{Fore.YELLOW}Convert Octal To"
                  "\n [1] Binary"
                  "\n [2] Decimal"
                  "\n [3] HexaDecimal"
                  "\n [4] Back"
                  "\n [5] Exit")
            #  check13 = check [1] 3
            check13 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
            match check13:
              case 1:
                print(f"{Fore.GREEN}Binary: " + bin(ocvalue))
                break
              case 2:
                print(f"{Fore.GREEN}Decimal: " + ocvalue)
                break
              case 3:
                print(f"{Fore.GREEN}Hexadecimal:" + hex(ocvalue))
                break
              case 4:
                continue
              case 5:
                break
              case _:
                print(f"{Fore.RED}[-] Wrong Selection!!")
                time.sleep(5)
          case 3:
            #  decimal to other
            #  dc = decimal
            dc = int(input("Enter Decimal Number: "))
            print(f"{Fore.YELLOW}Convert Decimal To"
                  "\n [1] Binary"
                  "\n [2] Octal"
                  "\n [3] HexaDecimal"
                  "\n [4] Back"
                  "\n [5] Exit")
            #  check14 = check [1] 4
            check14 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
            match check14:
              case 1:
                print(f"{Fore.GREEN}Binary: " + bin(dc))
                break
              case 2:
                print(f"{Fore.GREEN}Hexadecimal: " + hex(dc))
                break
              case 3:
                print(f"{Fore.GREEN}Octal: " + oct(dc))
                break
              case 4:
                continue
              case 5:
                break
              case _:
                print(f"{Fore.RED}[-] Wrong Selection!!")
                time.sleep(5)
          case 4:
            #  hexadecimal to other
            #  hx = hexadecimal
            hx = input(f"{Fore.BLUE}Enter Hexadecimal Number: ")
            hxvalue = int(hx , 16)
            print(f"{Fore.YELLOW}Convert HexaDecimal To"
                  "\n [1] Binary"
                  "\n [2] Octal"
                  "\n [3] Decimal"
                  "\n [4] Back"
                  "\n [5] Exit")
            #  check15 = check [1] 5
            check15 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
            match check15:
              case 1:
                print(f"{Fore.GREEN}Binary: " + bin(hxvalue))
                break
              case 2:
                print(f"{Fore.GREEN}Octal: " + oct(hxvalue))
                break
              case 3:
                print(f"{Fore.GREEN}Decimal: " + hxvalue)
                break
              case 4:
                continue
              case 5:
                break
              case _:
                print(f"{Fore.RED}[-] Wrong Selection")
                time.sleep(5)
          case 5:
            series = int(input("Enter the Fibonacchi Series Count: "))
            a = 0
            b = 1
            s = 0
            for x in range(series):
              print(s,end=" ")
              s = a+b
              b = a
              a = s
            break
          case 6:
            continue
          case 7:
            # exit
            break
          case _:
            print(f"{Fore.RED}[-] Wrong Selection!!")
            time.sleep(5)
      case 2:
        l = string.ascii_letters
        c = "!@#$%^&*()[]{},`~-=_+*/|?><.;:\'\"\\"
        n = "0123456789"
        a = l+c+n
        print(f"{Fore.YELLOW}Whelcom to The Password Generator"
              "\n choose Tool"
              "\n [0] Help"
              "\n [1] Generate Random Password"
              "\n [2] Create Custom Password"
              "\n [3] Create Pass List"
              "\n [4] Back"
              "\n [5] Exit")
        check2 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
        match check2:
          case 0:
            print(f"{Fore.MAGENTA}[*] Help: "
                  "\n [*] Generate Random Password: Generate Strong RAndom Password"
                  "\n [*] Create Custom Password: Merge Two Section And Create Password"
                  "\n [*] Create Password List For You (Please Don`t use it for Crack)"
                  "\n")
            time.sleep(7)
            continue
          case 1:
            L = int(input(f"{Fore.BLUE}the length of password: "))
            p = "".join(random.sample(a , L))
            print(f"{Fore.GREEN}Random password: " + p)
            break
          case 2:
            sec1 = input(f"{Fore.BLUE}Enter Sections One of Password: ")
            sec2 = input(f"{Fore.BLUE}Enter Sections Two of Password: ")
            pas = sec1+sec2
            print(f"{Fore.GREEN}Custom Password: "+ pas)
            break
          case 3:
            count = int(input("Enter The Count of passwords: "))
            ln = int(input("Enter The Length of Passwords: "))
            l_w = "abcdefghijklmnopqrstuvwxyz"
            u_w = l_w.upper()
            num = "0123456789"
            cha = "!@#$%^&*()[]{},`~-=_+*/|?><.;:\'\"\\"
            all = l_w + u_w + num + cha
            with open("pass.txt" , "a") as file:
              for i in range(count):
                file.write("".join(random.sample(all , ln)))
          case 4:
            continue
          case 5:
            break
          case _:
            print(f"{Fore.RED}[-] Wrong selection!!!")
            time.sleep(5)
      case 3:
        print(f"{Fore.YELLOW}Encryption or Decryption Hash??"
                "\n [0] Help"
                "\n [1] Encryption"
                "\n [2] Decryption"
                "\n [3] Back"
                "\n [4] Exit")
        check3 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
        match check3:
          case 0:
            print(f"{Fore.MAGENTA} [*] Help: "
                  "\n [*] Encryption: Convert Text to MD5 , SHA1 , SHA256 , SHA512 Hash"
                  "\n [*] Decryption: convet MD5 , SHA1 , SHA256 , SA512 Hash to Normal Text"
                  "\n")
            time.sleep(7)
            continue
          case 1:
            print(f"{Fore.YELLOW}Hash What?"
                  "\n [1] Text"
                  "\n [2] File"
                  "\n [3] Back"
                  "\n [4] Exit")
            check32 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
            match check32:
              case 1:
                print(f"{Fore.YELLOW}Welcome to the Hash Encryption Machne"
                    "\n Choose Type of Hash"
                    "\n [1] Md5 hash"
                    "\n [2] Sha1 hash"
                    "\n [3] Sha256 hash"
                    "\n [4] Sha512 hash"
                    "\n [5] Back"
                    "\n [6] Exit")
                #  check32 = check[3] 21
                check321 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
                match check322:
                  case 1:
                      #  hsh = hash
                      hsh = input(f"{Fore.BLUE}Enter Text: ")
                      md5 = hashlib.new("MD5")
                      md5.update(hsh.encode())
                      print(f"{Fore.GREEN}MD5: " + md5.hexdigest())
                      break
                  case 2:
                    #  hsh = hash
                      hsh = input(f"{Fore.BLUE}Enter Text: ")
                      sha1 = hashlib.new("SHA1")
                      sha1.update(hsh.encode())
                      print(f"{Fore.GREEN}Sha1: "+ sha1.hexdigest())
                      break
                  case 3:
                      #  hsh = hash
                      hsh = input(f"{Fore.BLUE}Enter Text: ")
                      sha256 = hashlib.new("SHA256")
                      sha256.update(hsh.encode())
                      print(f"{Fore.GREEN}Sha256: " + sha256.hexdigest())
                      break
                  case 4:
                    #  hsh = hash
                    hsh = input(f"{Fore.BLUE}Enter Text: ")
                    sha512 = hashlib.new("SHA512")
                    sha512.update(hsh.encode())
                    print(f"{Fore.GREEN}Sha512: " + sha512.hexdigest())
                    break
                  case 5:
                    continue
                  case 6:
                    break
                  case _:
                    print(f"{Fore.RED}[-] Wrong Selection")
                    time.sleep(5)
              case 2:
                print(f"{Fore.YELLOW}Welcome to File Hashing Machine"
                  "\n Choose Type of Hash"
                  "\n [1] MD5 Hash"
                  "\n [2] Sha1 Hash"
                  "\n [3] Sha256 Hash"
                  "\n [4] Sha512 Hash"
                  "\n [5] Back"
                  "\n [6] Exit")
                #  check322 = check [3] 22
                check322 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
                match check322:
                  case 1:
                    path = input(f"{Fore.BLUE}Enter Path: ")
                    with open(path , "rb") as opened:
                      file = opened.read()
                      md5 = hashlib.md5()
                      md5.update(file)
                    print(f"{Fore.GREEN}MD5: " + md5.hexdigest())
                    break
                  case 2:
                    path = input(f"{Fore.BLUE}Enter Path: ")
                    with open(path , "rb") as opened:
                      file = opened.read()
                      sha1 = hashlib.sha1()
                      sha1.update(file)
                    print(f"{Fore.GREEN}Sha1: " + sha1.hexdigest())
                    break
                  case 3:
                    path = input(f"{Fore.BLUE}Enter Path: ")
                    with open(path , "rb") as opened:
                      file = opened.read()
                      sha256 = hashlib.sha256()
                      sha256.update(file)
                      print(f"{Fore.GREEN}Sha256: " + sha256.hexdigest())
                    break
                  case 4:
                    path = input(f"{Fore.BLUE}Enter Path: ")
                    with open(path , "rb") as opened:
                      file = opened.read()
                      sha512 = hashlib.sha512()
                      sha512.update(file)
                    print(f"{Fore.GREEN}Sha512: " + sha512.hexdigest())
                    break
                  case 5:
                    continue
                  case 6:
                    break
                  case _:
                    print(f"{Fore.RED}[-] Wrong Selection!!")
                    time.sleep(5)
          case 3:
            continue
          case 4:
            break
          case _:
            print(f"{Fore.RED}[-] Wrong Selection!!")
            time.sleep(5)
      case 4:
        print(f"{Fore.YELLOW}[*] Choose Validation"
              "\n [0] Help"
              "\n [1] National Code Validation"
              "\n [2] Mobile Number Validation"
              "\n [3] Email Validation"
              "\n [4] Back"
              "\n [5] Exit")
        check4 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
        match check4:
          case 0:
            print(f"{Fore.MAGENTA}[*] Help: "
                  "\n [*] National Code Validation: Check Validation of [+] National Code"
                  "\n [*] Mobile Number Validation: Check Validation of Mobile Number(Inter[+] national)"
                  "\n [*] E-mail Validation: Check VAlidation of E-mail Address"
                  "\n") 
            time.sleep(7)
            continue
          case 1:
            def isnatcode(code):
              if len(code) != 10: return print(f"{Fore.GREEN}[+] National Code is invalid")
              if code == "0000000000": return print(f"{Fore.GREEN}[+] National Code is invalid")
              if code == "1111111111": return print(f"{Fore.GREEN}[+] National Code is invalid")
              if code == "2222222222": return print(f"{Fore.GREEN}[+] National Code is invalid")
              if code == "3333333333": return print(f"{Fore.GREEN}[+] National Code is invalid")
              if code == "4444444444": return print(f"{Fore.GREEN}[+] National Code is invalid")
              if code == "5555555555": return print(f"{Fore.GREEN}[+] National Code is invalid")
              if code == "6666666666": return print(f"{Fore.GREEN}[+] National Code is invalid")
              if code == "7777777777": return print(f"{Fore.GREEN}[+] National Code is invalid")
              if code == "8888888888": return print(f"{Fore.GREEN}[+] National Code is invalid")
              if code == "9999999999": return print(f"{Fore.GREEN}[+] National Code is invalid")

              n = int(code[0]) * 10
              n = n + int(code[1] * 9)
              n = n + int(code[2] * 8)
              n = n + int(code[3] * 7)
              n = n + int(code[4] * 6)
              n = n + int(code[5] * 5)
              n = n + int(code[6] * 4)
              n = n + int(code[7] * 3)
              n = n + int(code[8] * 2)
              lchar = int(code[9])
              rmain = n % 11
        
              if rmain == 0 and rmain == lchar: return print(f"{Fore.GREEN}[+] National Code is Valid")
              if rmain == 1 and rmain == lchar: return print(f"{Fore.GREEN}[+] National Code is Valid")
              if rmain > 1 and lchar == 11 - rmain: return print(f"{Fore.GREEN}[+] National Code is Valid")
        
              return print(f"{Fore.GREEN}[+] National Code is Valid")

            natcode = str(input(f"{Fore.BLUE}Enter National Code: "))
            print(isnatcode(natcode))
            break
          case 2: 
            mobnum = input(f"{Fore.BLUE}Enter Mobile Number(with Country prefix): ")
            numb = phonenumbers.parse(mobnum)
            ifmob = phonenumbers.is_possible_number(numb)
            if ifmob == True:
              print(f"{Fore.GREEN}[+] Can Be a Mobile Number")
              break
            else:
              print(f"{Fore.GREEN}[+] Cannot Be a Mobile Number")
            break
          case 3:
            def validemail(inemail):
              return bool(re.match(r'\b[A-Za-z0-9,_%+-]+@[A-Za-z0-9,-]+\.[A-Z|a-z]{2,}\b',inemail))
            email = input(f"{Fore.BLUE}Enter the Email Address: ")
            print(validemail(email))
            if validemail(email) == True:
              print(f"{Fore.GREEN}[+] Can Be an E-mail")
              break
            else:
              print(f"{Fore.GREEN}[+] Cannot Be an E-mail")
              break
          case 4:
            continue
          case 5:
            break
          case _:
            print(f"{Fore.RED}[-] Wrong Selection!!")
            time.sleep(5)
      case 5:
        print(f"{Fore.YELLOW}Choose Tool"
              "\n [0] Help"
              "\n [1] Translate"
              "\n [2] Wikipedia"
              "\n [3] Back"
              "\n [4] Exit")
        check5 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
        match check5:
          case 0:
            print(f"{Fore.MAGENTA} [*] Help: "
                  "\n [*] Translate: Translate Text and File"
                  "\n [*] Wikipedia: input subject and see the Summary about it!"
                  "\n")
            time.sleep(7)
            continue
          case 1:
            print(f"{Fore.YELLOW}Translate What?"
              "\n [0] Help"
              "\n [1] Text"
              "\n [2] File"
              "\n [3] Back"
              "\n [4] Exit")
            check51 = int(input("Enter Number of Tools:"))
            match check51:
              case 1:
                print(f"{Fore.YELLOW}Translate x To x (Text)"
                      "\n [1] Persian To English"
                      "\n [2] English To Persian"
                      "\n [3] Back"
                      "\n [4] Exit")
                check511 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
                match check511:
                  case 1:
                    ftext = input("fE{Fore.BLUE}nter Persian Text: ")
                    eout = GoogleTranslator(source="fa" , target="en").translate(ftext)
                    print(Fore.GREEN + eout)
                    break
                  case 2:
                    etext = input(f"{Fore.BLUE}Enter English Text: ")
                    fout = GoogleTranslator(source="en" , target="fa").translate(etext)
                    print(Fore.GREEN + fout)
                    break
                  case 3:
                    continue
                  case 4:
                    break
                  case _:
                    print(f"{Fore.RED}[-] Wrong Selection!!")
                    time.sleep(5)
              case 2:
                print(f"{Fore.YELLOW}Translate x To x (File)"
                      "\n [1] Persian To Engilsh"
                      "\n [2] English to Persian"
                      "\n [3] Back"
                      "\n [4] Exit")
                check521 = int(input(f"{Fore.BLUE}Enter Number of Tool: "))
                match check521:
                  case 1:
                    path = input(f"{Fore.BLUE}Enter The path: ")
                    file = open(path , encoding="utf8")
                    ffile = file.read()
                    eout = GoogleTranslator(source="fa" , target="en").translate(ffile)
                    print(Fore.GREEN + eout)
                    break
                  case 2:
                    path = input(f"{Fore.BLUE}Enter The path: ")
                    file = open(path)
                    efile = file.read()
                    fout = GoogleTranslator(source="en" , target="fa").translate(efile)
                    print(Fore.GREEN + fout)
                    break
                  case 3:
                    continue
                  case 4:
                    break
                  case _:
                    print(f"{Fore.RED}[-] Wrong Selection!!")
                    time.sleep(5)
              case 3:
                continue
              case 4:
                break
              case _:
                print(f"{Fore.RED}[-] Wrong Selection!!")
                time.sleep(5)
          case 2:
            subject = input(f"{Fore.BLUE}Enter Your Subject: ")
            result = wikipedia.summary(subject)
            print(f"{Fore.GREEN}Summary: " + result)
            break
          case 3:
            continue
          case 4:
            break
          case _:
            print(f"{Fore.RED}[-] Wrong Selection!!")
            time.sleep(5)
      case 6:
        print(f"{Fore.YELLOW}Choose Tools"
              "\n [0] Help"
              "\n [1] Shorting Link"
              "\n [2] Convert Link to Qrcode"
              "\n [3] Back"
              "\n [4] Exit")
        check6 = int(input(f"{Fore.BLUE}Enter Numver of Tool: "))
        match check6:
          case 0:
            print(f"{Fore.MAGENTA} [*] Help: "
                  "\n [*] Shorting Link: Shorting Long URLs"
                  "\n [*] Convert Link to Qrcode: Generate Qrcode Picture From URL"
                  "\n")
            time.sleep(7)
            continue
          case 1:
            def shorten(url):
              base_url = 'http://tinyurl.com/api-create.php?url='
              response = requests.get(base_url + url)
              short_url = response.text
              return short_url
            long_url = input("Enter Your URL: ")
            short_url = shorten(long_url)
            print(short_url)
          case 2:
            url2 = input(f"{Fore.BLUE}Enter The URL: ")
            qrcode.make(url2).save("qrc.png")
            break
          case 3:
            continue
          case 4:
            break
          case _:
            print(f"{Fore.RED}[-] Wrong Selection!!")
            time.sleep(5)
      case 7:
        print(f"{Fore.YELLOW}Choose Information"
              "\n [0] Help"
              "\n [1] Hardware"
              "\n [2] Software"
              "\n [3] Account"
              "\n [4] Network"
              "\n [5] All"
              "\n [6] Back"
              "\n [7] Exit")
        check7 = int(input(f"{Fore.BLUE}Enter Number of Tool:"))
        architec = platform.architecture()
        proc_name = platform.processor()
        proc_type = platform.machine()
        ram = psutil.virtual_memory().total
        sys_ostype = platform.system()
        os_release = platform.release()
        os_version = platform.version()
        os = platform.platform()
        os_edition = platform.win32_edition()
        com_name = platform.node()
        hostname = socket.gethostname()
        ipv6 = socket.gethostbyaddr(hostname)
        Private_ip = socket.gethostbyname(hostname)
        local_ip = requests.get("https://api.ipify.org/").text
        mac = get_mac_address()
        match check7:
          case 0:
            print(f"{Fore.MAGENTA} [*] Help: "
                  "\n [*] Hardware: Hardware Info"
                  "\n [*] Software: OS Info"
                  "\n [*] Account: Host and Computer Name"
                  "\n [*] Netwrok: MAc and IP Addresses"
                  "\n [*] All: Computer Full Info"
                  "\n")
            time.sleep(7)
            continue
          case 1:
            print(f"{Fore.GREEN}[+] Your Computer Hardware Info: "
            f"\n [+] Processor Type: {proc_type}"
            f"\n [+] Processor Name: {proc_name}"
            f"\n [+] Syestem Architecture: {architec} "
            f"\n [+] RAM Size: {ram}")
            break
          case 2:
            print(f"{Fore.GREEN}[+] Your Computer Software Info: "
            f"\n [+] System OS Type: {sys_ostype}"
            f"\n [+] OS Release: {os_release}"
            f"\n [+] OS Version: {os_version}"
            f"\n [+] OS: {os}"
            f"\n [+] OS Edition: {os_edition}")
            break
          case 3:
            print(f"{Fore.GREEN}Y[+] our Computer Account Info: "
            f"\n [+] Hostname: {hostname}"
            f"\n [+] Computer Name: {com_name}")
            break
          case 4:
            print(f"{Fore.GREEN}[+] Your Computer Network Info: "
                f"\n[+] MAC Address {mac}"
                f"\n[+] IPV6 Private Address: {ipv6}"
                f"\n[+] IPV4 Local Address: {local_ip}"
                f"\n[+] IPV4 Private Address: {Private_ip}")
            break
          case 5:
            print(f"{Fore.GREEN}[+] Your Computer Info: "
                f"\n [+] Processor Type: {proc_type}"
                f"\n [+] Ptocessor Name: {proc_name}"
                f"\n [+] Syestem Architecture: {architec}"
                f"\n [+] RAM Size: {ram}"
                f"\n [+] System OS Type: {sys_ostype}"
                f"\n [+] OS Release: {os_release}"
                f"\n [+] OS Version: {os_version}"
                f"\n [+] OS: {os}"
                f"\n [+] OS Edition: {os_edition}"
                f"\n [+] Hostname: {hostname}"
                f"\n [+] Computer Name: {com_name}"
                f"\n [+] MAC Address: {mac}"
                f"\n [+] IPV6 Private Address: {ipv6}"
                f"\n [+] IPV4 Local Address: {local_ip}"
                f"\n [+] IPV4 Private Address: {Private_ip}")
            break
          case 6:
            continue
          case 7:
            break
          case _:
            print(f"{Fore.RED}Wrorng Selection!!")
            time.sleep(5)
      case 8:
        break
      case _:
        print(f"{Fore.RED}[-] Wrong Selection!!")
        time.sleep(5)
except SyntaxError:
  print(traceback.print_exc())
  print(f"{Fore.RED}\n [-] We Get Wrong With Your Syntax!!")
  pass
except NameError:
  print(traceback.print_exc())
  print(f"{Fore.RED}\n [-] Name of Varriable Have Error")
except AttributeError:
  print(traceback.print_exc())
  print(f"{Fore.RED}\n [-] You Set a Invalid Attribute!!")
  pass
except ModuleNotFoundError:
  print(traceback.print_exc())
  print(f"{Fore.Red}\n [-] Something Was Wrong with Your Imported Modules!!")
  pass
except TypeError:
  print(traceback.print_exc())
  print(f"{Fore.RED}\n [-] What is This Type Doing Here?!!")
  pass
except ValueError:
  print(traceback.print_exc())
  print(f"{Fore.RED}\n [-] Inputed Value is Wrong")
  pass
except TimeoutError:
  print(traceback.print_exc())
  print(f"{Fore.RED}\n [-] Connection Time Out!!")
  pass
except Exception:
  print(traceback.print_exc())
  print(f"{Fore.RED}\n [-] Have An Error")
finally:
  print("\n" , "*"*30)

