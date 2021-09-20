oscsend localhost 4001 /oled/aux/line/2 s "installing"
oscsend localhost 4001 /oled/aux/line/3 s "orac module"
oscsend localhost 4001 /oled/aux/line/3 s "4waveFM"
cd ..
mv $1 orac/modules/synth
exit 1
