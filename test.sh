#!/bin/bash
oldrev="$1"
newrev="$2"
re1="fix"
re2="#[0-9]+"
missed_revs=`git rev-list ${oldrev}..${newrev}`
echo $missed_revs
for rev in ${missed_revs[@]};do
    echo $rev
    message=`git cat-file commit ${rev} | sed '1,/^$/d'`
    echo $message
    if [[ $message =~ $re1  ]];then
        if [[ $message =~ $re2  ]];then
            echo "okay"
        else
            echo "[POLICY] Your message is not formatted correctly"
        fi
    else
        echo "not fix"
    fi
done

