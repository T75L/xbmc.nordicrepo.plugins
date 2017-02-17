# television plugin edited by notec
# -*- coding: utf-8 -*-

# for more info please visit kamaihd.net

import xbmcgui,xbmcplugin 
plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty( "Fanart_Image", img )
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)


add_video_item('https://nrk1us-f.akamaihd.net/i/nrk1us_0@102847/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': '   - [B][COLOR yellowgreen] -  TV [/COLOR] [COLOR red]NORWAY [/COLOR] [COLOR white]- [/B][/COLOR] -'},img='special://home/addons/plugin.video.nordictv/resources/art/no.png')

add_video_item('https://nrk1us-f.akamaihd.net/i/nrk1us_0@102847/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 1 (NO)'},img='special://home/addons/plugin.video.nordictv/resources/art/nrk1.png')
add_video_item('https://nrk2us-f.akamaihd.net/i/nrk2us_0@107231/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 2 (NO)'},img='special://home/addons/plugin.video.nordictv/resources/art/nrk2.png')
add_video_item('https://nrk3us-f.akamaihd.net/i/nrk3us_0@107233/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 3 (NO)'},img='special://home/addons/plugin.video.nordictv/resources/art/nrk3.png')

add_video_item('http://dr01-lh.akamaihd.net/i/dr01_0@147054/master.m3u8?b=100-2000|X-Forwarded-For=77.66.34.57',{ 'title': '   - [B][COLOR yellowgreen] -  TV [/COLOR] [COLOR white]DENMARK [/COLOR] [COLOR white]- [/B][/COLOR] -'},img='special://home/addons/plugin.video.nordictv/resources/art/dk.png')

add_video_item('http://dr01-lh.akamaihd.net/i/dr01_0@147054/master.m3u8?b=100-2000|X-Forwarded-For=77.66.34.57',{ 'title': 'DR 1 (DK)'},img='special://home/addons/plugin.video.nordictv/resources/art/dr_1.png')
add_video_item('http://dr02-lh.akamaihd.net/i/dr02_0@147055/master.m3u8?b=100-2000|X-Forwarded-For=77.66.34.57',{ 'title': 'DR 2 (DK)'},img='special://home/addons/plugin.video.nordictv/resources/art/dr_2.png')
add_video_item('http://dr03-lh.akamaihd.net/i/dr03_0@147056/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DK 3 (DK)'},img='special://home/addons/plugin.video.nordictv/resources/art/dr_3.png')

add_video_item('https://svt10-lh.akamaihd.net/i/svt10_0@77505/master.m3u8|X-Forwarded-For=194.15.212.134',{ 'title': '   - [B][COLOR yellowgreen] -  TV [/COLOR] [COLOR blue]SWEDEN [/COLOR] [COLOR white]- [/B][/COLOR] -'},img='special://home/addons/plugin.video.nordictv/resources/art/se.png')

add_video_item('https://svt10-lh.akamaihd.net/i/svt10_0@77505/master.m3u8|X-Forwarded-For=194.15.212.134',{ 'title': 'SVT 1 (SE)'},img='special://home/addons/plugin.video.nordictv/resources/art/svt_1.png')
add_video_item('https://svt12-lh.akamaihd.net/i/svt12_0@77507/master.m3u8|X-Forwarded-For=194.15.212.134',{ 'title': 'SVT 2 (SE)'},img='special://home/addons/plugin.video.nordictv/resources/art/svt_2.png')
add_video_item('https://svt11-lh.akamaihd.net/i/svt11_0@77506/master.m3u8|X-Forwarded-For=194.15.212.134',{ 'title': 'SVT Kunskap (SE)'},img='special://home/addons/plugin.video.nordictv/resources/art/svt_k.png')

add_video_item('https://svt11-lh.akamaihd.net/i/svt11_0@77506/master.m3u8|X-Forwarded-For=194.15.212.134',{ 'title': '   - [B] - [COLOR yellowgreen] MORE CHANNELS [/COLOR] - [/B] -'},img='special://home/addons/plugin.video.nordictv/resources/art/flag.png')
add_video_item('https://nrksuper-lh.akamaihd.net/i/nrksupertvus_0@108447/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK Super (NO)'},img='special://home/addons/plugin.video.nordictv/resources/art/nrk_s.png')
add_video_item('https://nrktegnsprak-lh.akamaihd.net/i/nrktegnsprak_0@111177/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK Tegnsprak (NO)'},img='special://home/addons/plugin.video.nordictv/resources/art/nrk_t.png')
add_video_item('http://dr04-lh.akamaihd.net/i/dr04_0@147057/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DR K (DK)'},img='special://home/addons/plugin.video.nordictv/resources/art/dr_k.png')
add_video_item('http://dr05-lh.akamaihd.net/i/dr05_0@147058/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DR Ramasjang (DK)'},img='special://home/addons/plugin.video.nordictv/resources/art/dr_r.png')
add_video_item('http://dr06-lh.akamaihd.net/i/dr06_0@147059/master.m3u8?b=100-1600|X-Forwarded-For=77.66.34.57',{ 'title': 'DK Ultra (DK)'},img='special://home/addons/plugin.video.nordictv/resources/art/dr_u.png')

xbmcplugin.endOfDirectory(plugin_handle)
