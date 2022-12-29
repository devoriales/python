#!/bin/bash
# devoriales.com, 2022
# wrapper script to run the battle of Python 3.10 and Python 3.11

echo "Battle of Python 3.10 and Python 3.11"
countdown=5
while [ $countdown -gt 0 ]
do
    echo "Fight begins in $countdown"
    sleep 1
    countdown=$((countdown-1))
    if [ $countdown -eq 0 ]
    then
        echo "Let's get ready to rumble!"
        sleep 2
    fi

done


# set Python version to 3.10
source venv_310/bin/activate
# print the python version
echo "Python version: $(python --version)"
start=$(date +%s)
# run the python script
python battle.py
end=$(date +%s)
runtime_310=$((end-start))
echo "Runtime: $runtime_310 seconds"

# set Python version to 3.11
source venv_311/bin/activate
echo "Python version: $(python --version)"
start_311=$(date +%s)
python battle.py
end_311=$(date +%s)
runtime_311=$((end_311-start_311))
echo "Runtime: $runtime_311 seconds"

# compare the runtimes
if [ $runtime_310 -lt $runtime_311 ]
then
    echo "Python 3.10 is faster than Python 3.11 by $((runtime_311-runtime)) seconds"
    echo "in percentage: $((runtime_310*100/runtime_311))%"
else
    echo "Python 3.11 is faster than Python 3.10 by $((runtime_310-runtime_311)) seconds"
    echo "in percentage: $((runtime_311*100/runtime_310))%"
fi
