arg=$1

answer=$(echo -n "$(python $arg.py)" | md5sum)

echo Answer: $answer