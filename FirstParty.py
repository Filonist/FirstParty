import requests # для запросов к сайтам
from bs4 import BeautifulSoup # для парсинга страниц
import fake_useragent # для создания юзер агентов, чтобы доказать, что я не робот
import subprocess # для работы с os, открытия скачанных файлов
import time # для создания задержек
import getpass # для получения юзернейма пользователя компа
from selenium import webdriver # для выполнения действий в хроме для разработчика
from selenium.webdriver.common.by import By # для нахождения элементов по какому-то объекту


def winrar():
    try:
        link = "https://www.win-rar.com/postdownload.html?&L=4"
        response = requests.get(f'{link}')
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('a', id= 'downloadlink').get('href')
        program = requests.get(f'https://www.win-rar.com{data}').content
        program_name = data.split('/')[-1]
        
        with open(f'C:\\Users\\Vitalina\\Downloads\\{program_name}', 'wb') as file:
            file.write(program)
        
        return f'{program_name} has been downloaded'
    except:
        return 'WinRar not installed'

def python():
    try:
        link = "https://www.python.org/downloads/"
        response = requests.get(f'{link}')
        soup = BeautifulSoup(response.text, 'html.parser')
        full_data = soup.find('div', class_ = 'download-os-windows')
        data = full_data.find('a', class_ = 'button').get('href')
        program_name = data.split('/')[-1]   
        program = requests.get(f'{data}').content

        with open(f'C:\\Users\\Vitalina\\Downloads\\{program_name}', 'wb') as file:
            file.write(program)
        
        return f'{program_name} has been downloaded'
    except:
        return 'Python not installed'

def chrome():
    try:
        link = "http://dl.google.com/chrome/install/chrome_installer.exe"
        program_name = link.split('/')[-1]   
        program = requests.get(f'{link}').content

        with open(f'C:\\Users\\Vitalina\\Downloads\\{program_name}', 'wb') as file:
            file.write(program)
        
        return f'{program_name} has been downloaded'
    except:
        return 'Google Chrome not installed'
    
    
def chrome_install():
    try:
        username = getpass.getuser()
        subprocess.Popen(fr"C:\Users\{username}\Downloads\chrome_installer.exe /silent /install")
        print("Установка")

        time.sleep(5)
    except:
        print('Install is not finished')
        a = input()



def yandex():
    try:
        user = fake_useragent.UserAgent().random
        header = {'user-agent': user}
        
        link = "https://yandex.ru/soft/browsers/"
        response = requests.get(f'{link}', headers= header)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('div', class_ = 'lc-button-list__container')
        full_data = data.find('a', class_ = 'Link link lc-link lc-button lc-button_theme_shadow lc-button_size_xl lc-button_type_link lc-button-list__item').get('href')

        program = requests.get(f'{full_data}', headers= header).content
        program_name = 'Yandex.exe'
     
        with open(f'C:\\Users\\Vitalina\\Downloads\\{program_name}', 'wb') as file:
            file.write(program)
        
        return f'{program_name} has been downloaded'
    except:
        return 'Yandex not installed'


def YaDisk():
    try:
        user = fake_useragent.UserAgent().random
        header = {'user-agent': user}
        
        link = "https://360.yandex.ru/disk/download/"
        response = requests.get(f'{link}', headers= header)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('div', class_ = 'Content_1iEBKla_97HVaE9tuQYp3q')
        full_data = data.find('a', class_ = 'Button2 Button2_type_link Button2_size_xxl Button2_view_brand Button_1fq4euQWK_3ti9Eq-ofaPf').get('href')
        program = requests.get(f'{full_data}', headers= header).content
        program_name = full_data.split('/')[-2]
     
        with open(f'C:\\Users\\Vitalina\\Downloads\\{program_name}', 'wb') as file:
            file.write(program)
        
        return f'{program_name} has been downloaded'
    except:
        return 'YaDisk not installed'

def telegram():
    try:
        user = fake_useragent.UserAgent().random
        header = {'user-agent': user}
        program_name = 'Telegram.exe'
        
        link = "https://desktop.telegram.org/?setln=ru"
        response = requests.get(f'{link}', headers= header)
        soup = BeautifulSoup(response.text, 'html.parser')
        full_data = soup.find('a', class_ = 'td_download_btn').get('href')
        program = requests.get(f'https:{full_data}').content
     
        with open(f'C:\\Users\\Vitalina\\Downloads\\{program_name}', 'wb') as file:
            file.write(program)
        
        return f'{program_name} has been downloaded'
    except:
        return 'Telegram not installed'
    
def KeePass():
    try:
        link = "https://sourceforge.net/projects/keepass/files/KeePass%202.x/"
        
        response = requests.get(f'{link}')
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('span', class_ = 'name')
        spisok = []
        for i in data:
            spisok.append(i.text)
        version = spisok[0]
        response1 = requests.get(f'{link}/{version}/')
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        data1 = soup1.find('a', title = 'Click to download KeePass-2.55-Setup.exe').get('href')
        program_name = data1.split('/')[-2]   
        program = requests.get(f'{data1}').content


        with open(f'C:\\Users\\Vitalina\\Downloads\\{program_name}', 'wb') as file:
            file.write(program)
        
        return f'{program_name} has been downloaded'
    except:
        return 'KeePass not installed'


def VSCode():
    try:
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'safebrowsing.enabled': 'false'}
        chromeOptions.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(chromeOptions)
        link = "https://code.visualstudio.com/"

        driver.get(link)
        time.sleep(3)
        botton = driver.find_element(By.XPATH, '//*[@id="download-buttons-win"]')
        botton.click()
        time.sleep(3)
        driver.get('chrome://downloads/')
        time.sleep(40)

        driver.close()
        driver.quit()
        
        print('VSCode has been downloaded')
    except:
        print('VSCode not installed')




def kasper():
    try:
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'safebrowsing.enabled': 'false'}
        chromeOptions.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(chromeOptions)
        link = "https://www.kaspersky.ru/downloads/free-antivirus"

        driver.get(link)
        time.sleep(3)
        botton = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/div/section/div/div[3]/div[2]/div/div[2]/div/div[3]/div/button/span')
        botton.click()
        time.sleep(3)
        driver.get('chrome://downloads/')
        time.sleep(20)

        driver.close()
        driver.quit()
            
        print('Kaspersky Free has been downloaded')
    except:
        print('Kaspersky Free not installed')







if __name__ == '__main__':
    print('======================================')
    print(chrome()) # Скачивание установщика Chrome
 #   print(chrome_install()) # Установка Chrome
    print(winrar()) # Скачивание установщика WinRar
    print(python()) # Скачивание установщика Python 
    print(yandex()) # Скачивание установщика Yandex
    print(YaDisk()) # Скачивание установщика YaDisk
    print(telegram()) # Скачивание установщика Telegram
    print(KeePass()) # Скачивание установщика KeePass
    print(VSCode()) # Скачивание установщика VSCode
    print(kasper()) # Скачивание установщика Kaspersky Free
    print('======================================')
