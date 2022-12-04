from selenium import webdriver
from time import sleep
from os import environ


class Check_biala_lista:
    def __init__(self):
        environ['MOZ_HEADLESS'] = '1'  # Browser to background
        global driver
        driver = webdriver.Firefox(executable_path="geckodriver.exe") #geckodriver full path, by default firefox
        driver.get('https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka')
        self.numer_konta_field = driver.find_element_by_xpath( "/html/body/div[2]/form/div[2]/div[2]/div[1]/div[1]/fieldset[1]/label")
        self.nip_field = driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/div[2]/div[1]/div[1]/fieldset[2]/label")
        self.regon_field = driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/div[2]/div[1]/div[1]/fieldset[3]/label")
        self.nazwa_podmiotu_fld = driver.find_element_by_xpath( "/html/body/div[2]/form/div[2]/div[2]/div[1]/div[1]/fieldset[4]/label")
        self.txt_input_field = driver.find_element_by_xpath('//*[@id="inputType"]')
        self.szukaj_btn = driver.find_element_by_xpath('//*[@id="sendTwo"]')
        self.szukaj_btn2 = driver.find_element_by_xpath('//*[@id="sendOne"]')


    #returns result of search
    def return_result(self, wait_time=2):
        sleep(wait_time)
        try:
            return (driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[2]/div/div[1]/div').text,  # returns search ID
                    driver.find_element_by_xpath('/html/body/div[2]/div[5]/table[1]/tbody/tr/td[2]').text,  # returns company name
                    driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[1]/div/h4').text,  # VAT register active status
                    driver.find_element_by_xpath('/html/body/div[2]/div[5]/table[3]/tbody/tr/td[2]').text,  # returns if company is still active
                    driver.find_element_by_xpath('/html/body/div[2]/div[5]/table[11]/tbody/tr/td[2]').text.replace("\n", ",")) # returns bank accounts)
        except:
            return("Podmiot nie istnieje lub nie figuruje w rejestrze VAT")


    #checks vendor by account number
    def by_numer_konta(self, numer_konta=None, wait_time=2) -> str:
        sleep(wait_time)
        if numer_konta is not None:
            self.numer_konta_field.click()
            self.txt_input_field.send_keys(str(numer_konta))
            try:
                self.szukaj_btn.click()
            except:
                self.szukaj_btn2.click()
            return Check_biala_lista.return_result(self)


    # checks vendor by VAT_ID number
    def by_NIP(self, nip, wait_time=2):
        sleep(wait_time)
        if nip is not None:
            self.nip_field.click()
            self.txt_input_field.send_keys(str(nip))
            try:
                self.szukaj_btn.click()
            except:
                self.szukaj_btn2.click()
            return Check_biala_lista.return_result(self)


    # checks vendor by REGON number
    def by_REGON(self, regon, wait_time=2):
        sleep(wait_time)
        if regon is not None:
            self.regon_field.click()
            self.txt_input_field.send_keys(str(regon))
            try:
                self.szukaj_btn.click()
            except:
                self.szukaj_btn2.click()
            return Check_biala_lista.return_result(self)


    # checks vendor by name
    def by_nazwa(self, nazwa_podmiotu = None, wait_time=2):
        sleep(wait_time)
        if nazwa_podmiotu is not None:
            self.nazwa_podmiotu_fld.click()
            self.txt_input_field.send_keys(str(nazwa_podmiotu))
            try:
                self.szukaj_btn.click()
            except:
                self.szukaj_btn2.click()
            return Check_biala_lista.return_result(self)


if __name__ == "__main__":
    cbl = Check_biala_lista()
    cbl.by_NIP("Number_input_here")
    cbl.by_REGON("Number_input_here")
    cbl.by_nazwa("Company_Name_input_here")
    cbl.by_numer_konta("Company_Bank_Acc_input_here")
