import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

os.chdir('C:\\Users\\ghfin\\Downloads\\geckodriver-v0.29.0-win64')

class ft_account:

    def __init__(self, login, password, training_num, above100, skill_above100):
        self.login = login
        self.password = password
        self.training_num = training_num
        self.above100 = above100
        self.skill_above100 = skill_above100

    def open_website(self, login, password, training_num, above100, skill_above100):

        browser = webdriver.Firefox()
        
        browser.get('https://br.footballteamgame.com')
        time.sleep(5)
        
        loginButton = browser.find_element_by_css_selector('.btn-lg > span:nth-child(1)')
        loginButton.click()

        time.sleep(1)

        loginButtonTwo = browser.find_element_by_css_selector('div.modal-header-tab:nth-child(1) > h5:nth-child(1)')
        loginButtonTwo.click()

        emailAddress = browser.find_element_by_css_selector('div.form-group:nth-child(1) > input:nth-child(1)')
        emailAddress.send_keys(f'{self.login}')


        password = browser.find_element_by_css_selector('div.form-group:nth-child(2) > input:nth-child(1)')
        password.send_keys(f'{self.password}')


        LoginButtonThree = browser.find_element_by_css_selector('#btn-login')
        LoginButtonThree.click()

        time.sleep(10)

        browser.get('https://br.footballteamgame.com/training')
        time.sleep(3)

        bp = browser.find_element_by_css_selector('.grid > div:nth-child(8) > div:nth-child(1) > div:nth-child(2)')
        armacao = browser.find_element_by_css_selector('.grid > div:nth-child(4) > div:nth-child(1) > div:nth-child(2)')
        marcacao = browser.find_element_by_css_selector('.grid > div:nth-child(7) > div:nth-child(1) > div:nth-child(2)')
        resistencia = browser.find_element_by_css_selector('.grid > div:nth-child(5)')
        eficacia = browser.find_element_by_css_selector('.grid > div:nth-child(9)')
        ofensiva = browser.find_element_by_css_selector('.grid > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)')
        defensiva = browser.find_element_by_css_selector('.grid > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)')
        leitura = browser.find_element_by_css_selector('.grid > div:nth-child(6) > div:nth-child(1) > div:nth-child(2)')

        if above100 == True:
            if self.skill_above100 == 'bp':
                bp.click()
            if self.skill_above100 == 'armacao':
                armacao.click()
            if self.skill_above100 == 'marcacao':
                marcacao.click()
            if self.skill_above100 == 'resistencia':
                resistencia.click()
            if self.skill_above100 == 'eficacia':
                eficacia.click()
            if self.skill_above100 == 'ofensiva':
                ofensiva.click()
            if self.skill_above100 == 'defensiva':
                defensiva.click()
            if self.skill_above100 == 'leitura':
                leitura.click()

        def training_count():
            atributo1 = browser.find_element_by_css_selector('div.mobile-training:nth-child(2) > div:nth-child(2)')
            atributo2 = browser.find_element_by_css_selector('div.mobile-training:nth-child(3) > div:nth-child(2)')
            atributo3 = browser.find_element_by_css_selector('div.mobile-training:nth-child(4) > div:nth-child(2)')
            atributo4 = browser.find_element_by_css_selector('div.mobile-training:nth-child(5) > div:nth-child(2)')
            for i in range(3):
                atributo3.click()
                time.sleep(0.1)
                atributo4.click()
                time.sleep(0.1)
            time.sleep(19.6)

        def train_above_100(training_num):
            n = 0
            while n < (training_num/2)*0.85:    
                try:
                    training_count()
                    n += 1
                    print(f'{n*2} Treinos')
                except:
                    time.sleep(2)
                    print('Exception triggered')
                    continue
            browser.quit()

        def train_below_90(training_num):
            n = 0
            while n < training_num/2:
                for i in range(3):
                    armacao.click()
                    time.sleep(0.1)
                    marcacao.click()
                    time.sleep(0.1)
                n += 1
                print(f'{n*2} Treinos')
                time.sleep(29.6)
            browser.quit()
        
        if self.above100 == False:
            train_below_90(self.training_num)
        if self.above100 == True:
            train_above_100(self.training_num)
        

finatti = ft_account('ghfinatti3@gmail.com', '********', 400, False, '')
artur = ft_account('arturm_alves@hotmail.com', '********', 270, True, 'resistencia')
andre = ft_account('andre.taiss@gmail.com', '********', 300, True, 'ofensiva')
finatti.open_website(finatti.login, finatti.password, finatti.training_num, finatti.above100, finatti.skill_above100)
artur.open_website(artur.login, artur.password, artur.training_num, artur.above100, artur.skill_above100)
andre.open_website(andre.login, andre.password, andre.training_num, andre.above100, andre.skill_above100)
