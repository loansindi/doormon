#!/usr/bin/sh
while inotifywait -qq /srv/doormon/irc/chat.freenode.org/#pumpingstationone/out;
do
tail -n 1 "/srv/doormon/irc/chat.freenode.org/#pumpingstationone/out" > input
gawk  '{if ($4 == "!open") system("curl http://frontdoor.pumpingstationone.org:8080/open") > "/srv/doormon/irc/chat.freenode.org/#pumpingstationone/in"}' input
done

