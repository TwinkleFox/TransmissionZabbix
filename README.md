# TransmissionZabbix
Zabbix template to monitor Transmission

Шаблон для мониторинга Transmission в Zabbix

Начать с установки компонента transmissionrpc

$ sudo apt install python-transmissionrpc

Загрузить в /usr/lib/zabbix/externalscripts фвйл transmission.py

Задать этому файлу права на исполнение.

Присоединить этот шаблон к хосту с тем же IP что и сервер на котором transmision-daemon.

Добавить хосту макрос {$TRANSMISSIONPOST} указывающий номер порта веб-интерфейса Transmission. Обычно это 9091. Авторизация должна быть отключена.
