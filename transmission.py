#!/usr/bin/python
# -- coding: utf-8 --
import sys
import traceback
import transmissionrpc
if len (sys.argv) >= 3:
    try:
        client = transmissionrpc.Client(sys.argv[1], port=sys.argv[2])
    except Exception as e:
        print('Ошибка подключения')
        raise SystemExit
    torrents = client.info()
    if len (sys.argv) == 5:
        for tid, torrent in torrents.iteritems():
            if (sys.argv[3] == torrent.hashString):
                if (sys.argv[4] == 'name'):
                    print torrent.name.encode('utf-8')
                elif (sys.argv[4] == 'status'):
                    print torrent.status
                elif (sys.argv[4] == 'size'):
                    print torrent.totalSize
                elif (sys.argv[4] == 'ratio'):
                    print torrent.uploadRatio
                elif (sys.argv[4] == 'error'):
                    print torrent.error
                else:
                    print int(torrent.progress)
    elif len (sys.argv) == 4:
        stat = 0
        for tid, torrent in torrents.iteritems():
            if (sys.argv[3] == 'download'):
                stat = stat + int(torrent.rateDownload) * 8
            elif (sys.argv[3] == 'upload'):
                stat = stat + int(torrent.rateUpload) * 8
            elif (sys.argv[3] == 'size'):
                stat = stat + int(torrent.totalSize)
            else:
                stat += 1
        print stat
    else:
        stat = 0
        print '{\"data\":[',
        for tid, torrent in torrents.iteritems():
            if (stat > 0):
                print ',',
            print '{\"{#TORENTHASH}\":\"' + torrent.hashString + '\"}',
            stat += 1
        print ']}'
else:
    print 'Не указаны параметры подключения: ./transmission.py IP PORT'
