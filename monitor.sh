#! /bin/bash
while  true
do
result=$(ps aux | grep -c  "[python /home/anantrao/workspace/praw/rickandmortybot/causeWhyNotMate/causeWhyNotMaty.py]python /home/anantrao/workspace/praw/rickandmortybot/causeWhyNotMate/causeWhyNotMaty.py")
case $result in
        0) echo "restarting python causeWhyNotMaty.py"
           python /home/anantrao/workspace/praw/rickandmortybot/causeWhyNotMate/causeWhyNotMaty.py &
           sleep 60
                ;;
        1)
                ;;
        *)
                ;;
esac
done
