#! /bin/bash
while  true
do
result=$(ps aux | grep -c  "[python /home/anantrao/workspace/praw/causeWhyNotMate/canYouProveYouAre/causeWhyNotMaty.py]python /home/anantrao/workspace/praw/causeWhyNotMate/canYouProveYouAre/causeWhyNotMaty.py")
case $result in
        0) echo "restarting python causeWhyNotMaty.py"
           python /home/anantrao/workspace/praw/causeWhyNotMate/canYouProveYouAre/causeWhyNotMaty.py &
           sleep 60
                ;;
        1)
                ;;
        *)
                ;;
esac
done
