# Zense-Recruitment-Project
Required Modules and tools :
    1. Selenium WebDriver(Command : pip3 install selenium)
    2. Pandas (command : pip3 install pandas)
    3. xlrd-1.2.0 (command : pip3 install xlrd)(for Excel Support)
    4. ChromeDriver 2.35.0 (link : https://chromedriver.storage.googleapis.com/index.html?path=2.35/)
    5. A input.xlsx Excel file to give input OR Libreoffice Calc file in .xlsx extension.(This can be found in Repository).
    6. Google Chrome(Latest Version).
 Instructions to run code :
 1.Open input.xlsx 
        Enter whatsapp usernames in Whatsapp_usernames Column with there corresponding messages in Message Column and save it.
        Make sure to change the absolute paths in auto.py
        In third line, driver = webdriver.Chrome('Absolute path of chromeDriver')
        And also the input.xlsx file should in the same folder where program is there.
 2.python3 auto.py
        login With the use of Whatsapp web Feature and press enter in the terminal.
