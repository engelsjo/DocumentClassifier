# bash script to run k trials with sizes S

# python program and dataset
PY_PROGRAM=src/documentClassifier.py
PY_COMMAND=random
PY_DATASET=data/mergedData/forum-stemmed.data
#PY_DATASET=data/twitterData/sampleTwitterData.txt

# bash temp results
BASH_RANDOM=.temp/random_stdout.txt
BASH_PERCENT=.temp/random_percents.txt

# python aggregator
PY_AGGREGATE=src/postProcessStats.py
PY_OUTPUT=output/random

# ensure that arguments are provided
if [ -z "$1" ]; then
    echo "Missing argument for k: number of iterations per size"
    exit 1
fi
if [ -z "$2" ]; then
    echo "Missing argument for start of s: first size"
    exit 1
fi
if [ -z "$3" ]; then
    echo "Missing argument for end of s: last size"
    exit 1
fi
if [ -z "$4" ]; then
    echo "Missing argument for step: interval between sizes"
    exit 1
fi

# make temp directory to store intermediate results
mkdir -p .temp

# remove old results
rm -f ${BASH_RANDOM}
rm -f ${BASH_PERCENT}

# absolute min and absolute max for sizes of training set should be 1 and 99
K=$1
FIRST=$2
LAST=$3
STEP=$4

# loop from first size to last size using step as incrementing interval
# where n is the current size
for (( n=$FIRST; n<=$LAST; n+=$STEP )); do
    # execute program, saving (overwriting) output file
    python ${PY_PROGRAM} ${PY_COMMAND} ${PY_DATASET} $K $n > ${BASH_RANDOM}
    # search for effectiveness percentages and save to variable
    percents=$(grep -o "\(Effectiveness: \d\d%\)" ${BASH_RANDOM})
    # for each word in space separated list, iterate through
    for percent in $percents; do
        # if item is actually a percent, some are words like "effectiveness"
        if [[ $percent == [0-9][0-9]% ]] ; then
            # save off the percent to a file
            echo $percent >> ${BASH_PERCENT}
        fi
    done
done

# use python script to find the average and maximum of the percentages
OUTPUT_TXT=random_${K}_${FIRST}_${LAST}_${STEP}.txt
python ${PY_AGGREGATE} ${BASH_PERCENT} > ${PY_OUTPUT}/${OUTPUT_TXT}

# print final trials max and average to the std out
cat ${PY_OUTPUT}/${OUTPUT_TXT}
