arg=$1

answer=$(uv run $arg.py | md5sum | awk '{print $1}')

echo Answer: $answer
