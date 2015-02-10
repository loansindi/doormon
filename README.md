IRC door bot, docs to come

/etc/systemd/system/doormon.service

[Unit]
Description=Script for doormon
After=doormon.service

[Service]
Type=simple
User=doormon
Group=doormon
ExecStart=/srv/doormon/bot.sh
WorkingDirectory=/srv/doormon
Restart=always
RestartSec=10

[Install]
WantedBy=multi.user.target

/etc/systemd/system/doorbot.service

[Unit]
Description=Door monitoring IRC bot

[Service]
Type=simple
User=doormon
Group=doormon
ExecStart=/srv/doormon/ii -i irc -s chat.freenode.org -n doormon
ExecStartPost=sleep 20
ExecStartPost=/srv/doormon/join.sh
WorkingDirectory=/srv/doormon
Restart=Always
RestartSec=120

[Install]
WantedBy=multi-user.target
