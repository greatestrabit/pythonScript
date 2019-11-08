if  [ ! "$1" ] ;then
 echo "you have to input a word"
else
 pkill -9 v2ray
 lastid=`cat ~/Software/v2ray/lastid.dat`
 sed -i "s/$lastid/$1/g" ~/Software/v2ray/lastid.dat
 sed -i "s/$lastid/$1/g" ~/Software/v2ray/config.json
 ~/Software/v2ray/v2ray &
fi
