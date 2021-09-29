#! /bin/bash
#OS
if type -t wevtutil &> /dev/null

then

    OS=MSWin

elif type -t scutil &> /dev/null

then

    OS=macOS

else

    OS=Linux

fi

echo $OS >> resultado.txt

for i in 192.168.1.{1..255}

do
    ping -c 1 $i > /dev/null 2>&1
    [ $? -eq 0 ] && echo "Node with IP: $i is up." >> resultado.txt
done
for ((counter=10; counter<=500; counter++))
do
    (echo >/dev/tcp/$i/$counter) > /dev/null 2>&1 && echo "$counter open" >> resultado.txt

done