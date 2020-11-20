# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

try:
  import mechanize
except ModuleNotFoundError:
   print('mechanize not found: pip install mechanize')
from urllib.error import URLError
browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13')]
class SMS:
  class Czech_Republic:
    def Tmobile():
      url = 'https://www.t-mobile.cz/sms/closed.jsp'
      browser.open(url)
      if browser.title() == 'Přihlášení - T-Mobile.cz':
        print(browser.title())
        browser.select_form(action='https://www.t-mobile.cz/.gang/login')
        username = input('Jméno: ')
        password = input('Heslo: ')
        browser.form['username'] = username
        browser.form['password'] = password
        browser.method = 'POST'
        browser.submit()
      if browser.title() == 'Send SMS':
        print('Přihlášen.')
        print('\nPoslat SMS')
        browser.select_form(action='/sms/closed.jsp')
        number = '00420'+input('Číslo: ')
        while not len(number) == 14:
          number ='00420'+input('Zadejte platné číslo: ')
        text = input('Text: ')
        type = input('Zpráva / zpráva na Displej [z/d]: ')
        browser.form['recipients'] = number
        browser.form['text'] = text
        if type == 'z':
          browser.form['mtype'] = ['0']
        elif type == 'd':
          browser.form['mtype'] = ['1']
        else:
          print('Typ nastaven na defaultní.')
        browser.find_control('TMCZcheck').items[0].selected=True
        confirmation = input('Poslat potvrzení? [a/n]: ')
        if confirmation == 'a':
          browser.find_control('confirmation').items[0].selected=True
        elif confirmation == 'n':
          browser.find_control('confirmation').items[0].selected=False
        else:
          print('Potvrzení nastaveno na defaultní.')
        browser.submit()
        print('Zpráva odeslána.')
      elif browser.title() == 'Neoprávněný přístup - T-Mobile.cz':
        print('Zapni Wi-Fi nebo data na T-mobile SIM kartě a restartuj program.')
      elif browser.title() == 'Přihlášení se nezdařilo - T-Mobile.cz':
        print('Přihlášení se nezdařilo. Zkontroluj jméno a heslo.')
      else:
        print('Někde je chyba. Zkus restartovat program.')
 
if __name__ == '__main__':
  try:
    SMS.Czech_Republic.Tmobile()
  except KeyboardInterrupt:
    print('Goodbye.')
  except URLError:
    print('Chyba. Zapni Wi-Fi nebo data.')
  except:
    print('Chyba. Zkus ověřit síťové připojení.')


