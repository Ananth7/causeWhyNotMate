#! /bin/bash
while  true
do
result=$(ps aux | grep -c  "[python /home/anantrao/justalilbit/causeWhyNotMaty.py]python /home/anantrao/justalilbit/causeWhyNotMaty.py")
case $result in
        0) echo "restarting python causeWhyNotMaty.py"
           python ~/justalilbit/causeWhyNotMaty.py &
           sleep 60
                ;;
        1)
                ;;
        *)
                ;;
esac
done
