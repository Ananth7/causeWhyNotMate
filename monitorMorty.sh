#! /bin/bash
while  true
do
result=$(ps aux | grep -c  "[python /home/anantrao/causeWhyNotMate/causeWhyNotMorty.py]python /home/anantrao/causeWhyNotMate/causeWhyNotMorty.py")
case $result in
        0) echo "restarting python causeWhyNotMorty.py"
           python ~/causeWhyNotMate/causeWhyNotMorty.py &
           sleep 60
                ;;
        1)
                ;;
        *)
                ;;
esac
done
