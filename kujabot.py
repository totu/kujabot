# -*- coding: cp1252 -*-
import libbot

def main():
    kujis = libbot.Bot('kujis_testi3')
    kujis.connect_network('irc.quakenet.org')
    kujis.join_channel('kujalla')
    kujis.start()

if __name__ == '__main__':
    main()
