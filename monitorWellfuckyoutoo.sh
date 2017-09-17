#! /bin/bash
while  true
do
result=$(ps aux | grep -c  "[python /home/anantrao/workspace/praw/wellfuckyoutoo/causeWhyNotMate/causeWhyNotMaty.py]python /home/anantrao/workspace/praw/wellfuckyoutoo/causeWhyNotMate/causeWhyNotMaty.py")
case $result in
        0) echo "restarting python causeWhyNotMaty.py"
           python /home/anantrao/workspace/praw/wellfuckyoutoo/causeWhyNotMate/causeWhyNotMaty.py &
           sleep 60
                ;;
        1)
                ;;
        *)
                ;;
esac
done
