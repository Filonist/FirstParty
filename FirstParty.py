import requests # для запросов к сайтам
from bs4 import BeautifulSoup # для парсинга страниц
import fake_useragent # для создания юзер агентов, чтобы доказать, что я не робот
import subprocess # для работы с os, открытия скачанных файлов
import time # для создания задержек
import getpass # для получения юзернейма пользователя компа
from selenium import webdriver # для выполнения действий в хроме для разработчика
from selenium.webdriver.common.by import By # для нахождения элементов по какому-то объекту
import getpass
import random
import os
from pathlib import Path
import winapps
import pyzipper  

username = getpass.getuser()
program_directory = input('Директория, куда устанавливать приложения: ')
program_directory = program_directory.replace('"', '')


def winrar():
    try:
        link = "https://www.win-rar.com/postdownload.html?&L=4"
        response = requests.get(f'{link}')
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('a', id= 'downloadlink').get('href')
        program = requests.get(f'https://www.win-rar.com{data}').content
        program_name = data.split('/')[-1]
        
        with open(f'C:\\Users\\{username}\\Downloads\\{program_name}', 'wb') as file:
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

        with open(f'C:\\Users\\{username}\\Downloads\\{program_name}', 'wb') as file:
            file.write(program)
        
        return f'{program_name} has been downloaded'
    except:
        return 'Python not installed'

def chrome():
    try:
        link = "http://dl.google.com/chrome/install/chrome_installer.exe"
        program_name = link.split('/')[-1]   
        program = requests.get(f'{link}').content

        with open(f'C:\\Users\\{username}\\Downloads\\{program_name}', 'wb') as file:
            file.write(program)
        
        return f'{program_name} has been downloaded'
    except:
        return 'Google Chrome not installed'
    
    


def yandex():
    # try:
    #     spisok = ['Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0']
    #     header = {'User-Agent':random.choice(spisok)}
    #     link = "https://yandex.ru/soft/browsers/"
    #     response = requests.get(f'{link}',headers=header)
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     data = soup.find('div', class_ = 'lc-button-list__container')
    #     full_data = data.find('a', class_ = 'Link link lc-link lc-button lc-button_theme_shadow lc-button_size_xl lc-button_type_link lc-button-list__item').get('href')
    #     program = requests.get(f'{full_data}',headers=header).content
    #     program_name = 'Yandex.exe'
    #     with open(f'C:\\Users\\{username}\\Downloads\\{program_name}', 'wb') as file:
    #         file.write(program)
        
    #     return f'{program_name} has been downloaded'
    # except:
    #     print('Yandex not installed')

            try:
                chromeOptions = webdriver.ChromeOptions()
                prefs = {'safebrowsing.enabled': 'false'}
                chromeOptions.add_experimental_option("prefs", prefs)

                driver = webdriver.Chrome(chromeOptions)
                link = "https://yandex.ru/soft/browsers/"

                driver.get(link)
                time.sleep(3)
                botton = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/span/section/div[1]/div[1]/div[3]/section/div/div/div/div[1]/div/div[3]/section/div/div/div[1]/a')
                botton.click()
                time.sleep(3)
                driver.get('chrome://downloads/')
                time.sleep(10)

                driver.close()
                driver.quit()
                    
                print('Yandex has been downloaded')
            except:
                print('Yandex not installed')

def YaDisk():
    try:
        # user = fake_useragent.UserAgent().random
        # header = {'user-agent': user}
        
        link = "https://360.yandex.ru/disk/download/"
        response = requests.get(f'{link}')
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('div', class_ = 'Content_1iEBKla_97HVaE9tuQYp3q')
        full_data = data.find('a', class_ = 'Button2 Button2_type_link Button2_size_xxl Button2_view_brand Button_1fq4euQWK_3ti9Eq-ofaPf').get('href')
        program = requests.get(f'{full_data}').content
        program_name = full_data.split('/')[-2]
     
        with open(f'C:\\Users\\{username}\\Downloads\\{program_name}', 'wb') as file:
            file.write(program)
        
        return f'{program_name} has been downloaded'
    except:

            try:
                chromeOptions = webdriver.ChromeOptions()
                prefs = {'safebrowsing.enabled': 'false'}
                chromeOptions.add_experimental_option("prefs", prefs)

                driver = webdriver.Chrome(chromeOptions)
                link = "https://360.yandex.ru/disk/download/"

                driver.get(link)
                time.sleep(3)
                botton = driver.find_element(By.XPATH, '/html/body/div/main/section[1]/div[1]/div/div/a[1]')
                botton.click()
                time.sleep(3)
                driver.get('chrome://downloads/')
                time.sleep(10)

                driver.close()
                driver.quit()
                    
                print('Yandex Disk has been downloaded')
            except:
                print('Yandex Disk not installed')

def telegram():
    try:
        # user = fake_useragent.UserAgent().random
        # header = {'user-agent': user}
        program_name = 'Telegram.exe'
        
        link = "https://desktop.telegram.org/?setln=ru"
        response = requests.get(f'{link}')
        soup = BeautifulSoup(response.text, 'html.parser')
        full_data = soup.find('a', class_ = 'td_download_btn').get('href')
        program = requests.get(f'https:{full_data}').content
     
        with open(f'C:\\Users\\{username}\\Downloads\\{program_name}', 'wb') as file:
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


        with open(f'C:\\Users\\{username}\\Downloads\\{program_name}', 'wb') as file:
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

def VMWare():
    
    try:
        spisok = ['Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0']
        header = {'User-Agent':random.choice(spisok)}
        link = "https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html"
        response = requests.get(f'{link}',headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('div', class_ = 'card-box shadow textcard bg-white height text-gray').find('a', class_ = 'linkdisplay mb-2 plain-text').get('href')
        program = requests.get(f'https://www.vmware.com{data}',headers= header).content

        program_name = 'VMware Workstation.exe'
        
        with open(f'C:\\Users\\{username}\\Downloads\\{program_name}', 'wb') as file:
            file.write(program)
        
        return f'{program_name} has been downloaded'
    except:
        return 'VMware Workstation not installed'


def chrome_install(direct):
    
    try:
        if not search('google'):
            subprocess.Popen(fr"{direct} /silent /install")
            print("Установка Google")
            cher = 0
            while cher == 0:
                if not search('google'):
                    print('Идёт установка...')
                    time.sleep(15)
                    cher = 0
                else:
                    print('Установлено')
                    cher = 1
                    time.sleep(6)
                    break
        else:
            print('Google уже установлен')
    except:
        print('Google install is not finished')




def winrar_install(direct):
    try:
        if not search('winrar'):
            subprocess.Popen(fr"{direct} /S")
            print("Установка WinRar")
            cher = 0
            while cher == 0:
                if not search('winrar'):
                    print('Идёт установка...')
                    time.sleep(5)
                    cher = 0
                else:
                    print('Установлено')
                    cher = 1
                    time.sleep(6)
                    break
        else:
            print('WinRar уже становлен')
    except:
        print('WinRar install is not finished')

     
def python_install(direct):
    try:
        if not search('python'):
            subprocess.Popen(fr"{direct}")
            print("Установка Python")
            cher = 0
            while cher == 0:
                if not search('python'):
                    print('Идёт установка...')
                    time.sleep(15)
                    cher = 0
                else:
                    print('Установлено')
                    cher = 1
                    time.sleep(6)
                    break
        else:
            print('Python уже становлен')
    except:
        print('Python install is not finished')
     
        
 
def keepass_install(direct):

    try:
        if not search('keepass'):
            subprocess.Popen(fr"{direct} /VERYSILENT /NORESTART")
            print("Установка Keepass")
            cher = 0
            while cher == 0:
                if not search('keepass'):
                    print('Идёт установка...')
                    time.sleep(5)
                    cher = 0
                else:
                    print('Установлено')
                    cher = 1
                    time.sleep(6)
                    break
        else:
            print('Keepass уже становлен')
    except:
        print('Keepass install is not finished')            
        
def kaspersky_install(direct):

    try:
        if not search('kasper'):
            subprocess.Popen(fr"{direct} /s /qn")
            print("Установка Kaspsersky")
            cher = 0
            while cher == 0:
                if not search('kasper'):
                    print('Идёт установка...')
                    time.sleep(30)
                    cher = 0
                else:
                    print('Установлено')
                    cher = 1
                    time.sleep(6)
                    break
        else:
            print('Kaspsersky уже становлен')
    except:
        print('Kaspsersky install is not finished')  
        
def vmware_install(direct):
    print("Установка VMware")
    try:
        if not search('vmware'):
            subprocess.Popen(fr"{direct}")
            print("Установка VMWare")
            cher = 0
            while cher == 0:
                if not search('vmware'):
                    print('Идёт установка...')
                    time.sleep(5)
                    cher = 0
                else:
                    print('Установлено')
                    cher = 1
                    time.sleep(6)
                    break
        else:
            print('VMWare уже установлен')
    except:
        print('VMWare install is not finished')     
        
        
def yandex_install(direct):
    print('Установка Yandex')
    directory = f'C:\\Users\\{username}\\AppData\\Local\\Yandex\\YandexBrowser\\Application'
    try:
        files = os.listdir(directory)
        print('Yandex уже установлен')
    except:
        subprocess.Popen(fr"{direct} --silent --do-not-launch-browser")
        selector = 0
        while selector == 0:
            try:
                files = os.listdir(directory)
                print('Yandex почти установлен')
                time.sleep(60)
                print('Yandex установлен')
                selector = 1
            except:
                print("Идёт установка...")
                time.sleep(10)
                selector = 0


def yadisk_install(direct):
    print('Установка Yandex Disk')
    directory = f'C:\\Users\\{username}\\AppData\\Roaming\\Yandex\\YandexDisk2\\'

    try:
        files = os.listdir(directory)
        full_directory = (f'{directory}{files[0]}')
        underfules = os.listdir(full_directory)
        print('Yandex Disk уже установлен')
    except:
        subprocess.Popen(fr"{direct} /S")
        selector = 0
        while selector == 0:
            try:
                files = os.listdir(directory)
                print('Yandex Disk почти установлен')
                time.sleep(60)
                print('Yandex Disk установлен')
                selector = 1
            except:
                print("Идёт установка...")
                time.sleep(10)
                selector = 0


def telegram_install(direct):
    print('Установка Telegram')
    directory = f'C:\\Users\\{username}\\AppData\\Roaming\\Telegram Desktop'
    try:
        files = os.listdir(directory)
        print('Telegram уже установлен')
    except:
        subprocess.Popen(fr"{direct} /VERYSILENT /NORESTART")
        selector = 0
        while selector == 0:
            try:
                files = os.listdir(directory)
                print('Telegram почти установлен')
                time.sleep(30)
                print('Telegram установлен')
                selector = 1
            except:
                print("Идёт установка...")
                time.sleep(10)
                selector = 0

def vscode_install(direct):
    print('Установка VSCode')
    directory = f'C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code'
    try:
        files = os.listdir(directory)
        print('VSCode уже установлен')
    except:
        subprocess.Popen(fr"{direct} /VERYSILENT")
        selector = 0
        while selector == 0:
            try:
                files = os.listdir(directory)
                print('VSCode почти установлен')
                time.sleep(30)
                print('VSCode установлен')
                selector = 1
            except:
                print("Идёт установка...")
                time.sleep(10)
                selector = 0



def office_install(direct):
    print("Установка Office")
    try:
        if not search('office'):
            subprocess.Popen(fr"{direct} -aiS -gm2")
            print("Установка Office")
            cher = 0
            while cher == 0:
                if not search('office'):
                    print('Идёт установка...')
                    time.sleep(60)
                    cher = 0
                else:
                    print('Установлено')
                    cher = 1
                    time.sleep(6)
                    subprocess.run(['powershell.exe', 'irm https://massgrave.dev/get | iex'])
                    break
        else:
            print('Office уже установлен')
    except:
        print('Office install is not finished')     

def photoshop_install(direct):
    print("Установка Photoshop")
    try:
        if not search('photoshop'):
            decrypt(direct, b'111')
            new_direct = direct[0:-9] + '.exe'
            os.mkdir(program_directory +'\\' + 'Photoshop')
            install_path = (program_directory + '\\' + 'Photoshop')
            subprocess.Popen(fr"{new_direct} -S /XPATH={install_path} /XVCR")
            print("Установка Photoshop")
            cher = 0
            while cher == 0:
                if not search('Photoshop'):
                    print('Идёт установка...')
                    time.sleep(30)
                    cher = 0
                else:
                    print('Установлено')
                    cher = 1
                    time.sleep(6)
                    break
        else:
            print('Photoshop уже установлен')
    except:
        print('Photoshop install is not finished')    
    
        
def audition_install(direct):
    print("Установка Audition")
    try:
        if not search('audition'):
            decrypt(direct, b'111')
            new_direct = direct[0:-9] + '.exe'
            os.mkdir(program_directory +'\\' + 'Audition')
            install_path = (program_directory + '\\' + 'Audition')
            subprocess.Popen(fr"{new_direct} -S /XPATH={install_path} /XDISABLENET=1 /XVCR")
            print("Установка Audition")
            cher = 0
            while cher == 0:
                if not search('audition'):
                    print('Идёт установка...')
                    time.sleep(30)
                    cher = 0
                else:
                    print('Установлено')
                    cher = 1
                    time.sleep(6)
                    break
        else:
            print('Audition уже установлен')
    except:
        print('Audition install is not finished')             





def filename(name):

    directory = (f'C:\\Users\\{username}\\Downloads\\')
    files = os.listdir(directory)
    for i in range(len(files)):
        if files[i].startswith(name) == True:
            path = directory+ files[i]
            break
    return path
              
           
def search(name):
    for app in winapps.search_installed(name):
        return app

        
def decrypt(file_path, word):
    descrypt_path = f'C:\\Users\\{username}\\Downloads\\'
    with pyzipper.AESZipFile(file_path, 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) \
            as extracted_zip:
        try:
            extracted_zip.extractall(pwd=word, path=descrypt_path)
        except RuntimeError as ex:
            print(ex)        
        
        
print('''================================================================================================================
********  ***  ********   *******  *************     *********  ***********  ********  *************  **      **
********  ***  **    **  ********  *************     *********  ***********  **    **  *************  **      **
**             **    **  **             ***          **     **  **       **  **    **       ***       **      **
********  ***  *******   *******        ***          *********  **       **  *******        ***       **********
********  ***  ** ****   ********       ***          *********  ***********  *******        ***        *********
**        ***  **    **        **       ***          **         ***********  **    **       ***               **
**        ***  **    **  ********       ***          **         **       **  **    **       ***       **********       
**        ***  **    **  ********       ***          **         **       **  **    **       ***       **********      
================================================================================================================''')        
        
        
if __name__ == '__main__':
    print(' ')
    print(chrome()) # Скачивание установщика Chrome +
    print(winrar()) # Скачивание установщика WinRar +
    print(python()) # Скачивание установщика Python  +
    print(telegram()) # Скачивание установщика Telegram + 
    print(KeePass()) # Скачивание установщика KeePass +
    print(yandex()) # Скачивание установщика Yandex 
    print(YaDisk()) # Скачивание установщика YaDisk 
    print(VSCode()) # Скачивание установщика VSCode +
    print(kasper()) # Скачивание установщика Kaspersky Free +
    print(VMWare()) # Скачивание установщика VMWare Workstation
    chrome_install(filename('chrome')) # Установка Google
    winrar_install(filename('winrar')) # Установка WinRar   
    python_install(filename('python')) # Установка Python
    keepass_install(filename('KeePass')) # Установка KeePass
    kaspersky_install(filename('kasper')) # Установка Kaspersky
    vmware_install(filename('VMware')) # Установка VMware
    yandex_install(filename('Yandex.exe')) # Установка Yandex
    yadisk_install(filename('YandexDisk')) # Установка Yandex Disk
    telegram_install(filename('Telegram')) # Установка Telegram
    vscode_install(filename('VSCode')) # Установка VSCode

    print('''=============================================================================
1. Отключите антивирус
2. Закиньте установщики в папку Загрузки (Office, Photoshop, Audition, Дрова)
=============================================================================
# ''')
    while True:
        answer = input('Готово? [y/n]:')
        if (answer == 'у' or answer == 'y'):
            office_install(filename('Office'))
            photoshop_install(filename('Adobe Ph'))
            audition_install(filename('Adobe Audi'))
            break
        else:
            print('правила')

    input("END")
    print('======================================')