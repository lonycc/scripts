export PATH="/usr/local/sbin:$PATH"
PHP_AUTOCONF="/usr/local/bin/autoconf"
source ~/.bash_aliases
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles
export GOPATH=/usr/local/Cellar/go/1.10
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN
BYel="\e[0;33m"

function start_music() {
    search_music $1 &
}

function search_music() {
    m_path=~/Music/163/
    keyword="."                                                         # default: play all the songs
    if [ -n "$1" ]; then                                                # play songs by keyword
        keyword="$1"
    fi

    song_num="$(ls $m_path | grep -i -e $keyword | wc -l)"                   # Total num of qualified songs
    while [ 1 ]
    do
        dummy1=$((RANDOM))
        timestamp=$(date +%s)
        dummy=$(($dummy1*$timestamp))
        song_index=$(($dummy%$song_num+1))                              # Generate a random song index

        song="$(ls $m_path | grep -i -e $keyword | sed -n "$song_index"p)"   # Get the name of the qualified song
        echo -e "${BYel}$song"
        afplay "$m_path$song"
        wait
    done
}

function next_music() {  # next song
    pid="$(ps -ef | grep afplay | grep -v grep | head -1 | awk '{print $2}')"
    kill -INT $pid
}

function quit_music() { # terminate afplay
    pid="$(ps -ef | grep afplay | grep -v grep | head -1 | awk '{print $2}')"
    ppid="$(ps -ef | grep afplay | grep -v grep | head -1 | awk '{print $3}')"
    kill -INT $ppid && kill -INT $pid
}

function stop_music() { # music stop
    ppid="$(ps -ef | grep afplay | grep -v grep | head -1 | awk '{print $3}')"
    pid="$(ps -ef | grep afplay | grep -v grep | head -1 | awk '{print $2}')"
    kill -TSTP $pid && kill -TSTP $ppid
}

function restore_music() { # music continue
    ppid="$(ps -ef | grep afplay | grep -v grep | head -1 | awk '{print $3}')"
    pid="$(ps -ef | grep afplay | grep -v grep | head -1 | awk '{print $2}')"
    kill -CONT $pid && kill -CONT $ppid
}
