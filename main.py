from beautiful_soup import parser_lxml
from db import seeds
from own_scrapy import start_scrapy

if __name__ == '__main__':
    while True:
        print('---------------------------------------------------')
        print('Choice a method for scraping:')
        print('1 - Beautiful soup')
        print('2 - Scrapy')
        print('exit - Exit')
        print('---------------------------------------------------')
        cmd = input('Command: ')
        print(cmd)
        match cmd:
            case '1':
                print('Loading......')
                parser_lxml()
                seeds()
                print('Done.')
            case '2':
                print('Loading......')
                start_scrapy()
                seeds()
                print('Done.')
            case 'exit':
                print('Goodby!')
                quit()
            case _:
                print('Unknown command')
