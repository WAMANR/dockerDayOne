PORT=$1
TASKS=$2
GENERAL_WORKERS=$3
ADD_WORKERS=$4
MULT_WORKERS=$5
COUNT=0
PORTLIST=""


    while [ $GENERAL_WORKERS -gt 0 ]
    do
        docker run --network=dockerNetwork -e ADD=true -e MULT=true -e PORT=$PORT --name worker$COUNT -d worker
        GENERAL_WORKERS=$(( $GENERAL_WORKERS - 1 ))
        PORT=$(( $PORT + 1 ))
        COUNT=$(( $COUNT + 1 ))
        PORTLIST="$PORTLIST;$(echo $PORT),gen"
    done

    while [ $ADD_WORKERS -gt 0 ]
    do
        #docker run --network=dockerNetwork -e ADD=true -e MULT=false -e PORT=$PORT --name worker$COUNT -d worker
        ADD_WORKERS=$(( $ADD_WORKERS - 1 ))
        PORT=$(( $PORT + 1 ))
        COUNT=$(( $COUNT + 1 ))
        PORTLIST="$PORTLIST;$(echo $PORT),add"
    done

    while [ $MULT_WORKERS -gt 0 ]
    do
        #docker run --network=dockerNetwork -e ADD=false -e MULT=true -e PORT=$PORT --name worker$COUNT -d worker
        MULT_WORKERS=$(( $MULT_WORKERS - 1 ))
        PORT=$(( $PORT + 1 ))
        COUNT=$(( $COUNT + 1 ))
        PORTLIST="$PORTLIST;$(echo $PORT),mult"
    done

    docker run --network=dockerNetwork -e PORT=3000 -e TASKS=$TASKS -e WORKERS=$PORTLIST --name planner -d planner

    echo $PORTLIST
    



