#!/bin/bash

#用法 ./MovieClips.sh 电影的绝对路径 时间 (切割好的影片会在/Users/eric/films目录)
#例子：./MovieClips.sh /Users/eric/Movies/神弃之地BD1280高清中英双字版.mp4 10

ClipsMin=$2
File=$1
FilmName=$(echo $File | rev | cut -d '/' -f1 | rev | cut -d "." -f1)
FileSuffix=$(echo $File | rev |cut -d "." -f1 | rev)
FilmTime=$(ffmpeg -i $File 2>&1 | grep 'Duration' | cut -d ' ' -f 4 | sed s/,// | cut -d '.' -f 1)
FilmHour=$(echo $FilmTime | cut -d ':' -f 1)
FilmMin=$(echo $FilmTime | cut -d ':' -f 2)

username=$(users)
fileName="films"


if [ ! $FilmHour == '00' ]
then
	FilmMin=`expr $FilmMin + $FilmHour \* 60`
fi

mkdir -p /Users/$username/$fileName/$FilmName
ClipsNum=`expr $FilmMin / $ClipsMin + 1`
Min='00'
Hour='00'

for ((i=0; i<$ClipsNum; i++))
do
#	echo ffmpeg -ss ${Hour}:${Min}:00 -i $File -c copy -t 00:${Cli$DirName/flims/$FileName/${FileName}-cut${i}.$FileSuffix
	CutNum=`expr $i + 1`
	# echo /Users/$username/$fileName/$FilmName/$FilmName-cut$CutNum.$FileSuffix
	# exit
	ffmpeg -ss $Hour:$Min:00 -i $File -c copy -t 00:$ClipsMin:00 /Users/$username/$fileName/$FilmName/$FilmName-cut$CutNum.$FileSuffix
	Min=`expr $Min + $ClipsMin`

	if [ ${#Min} -lt 2 ]
	then
		Min="0$Min"
	fi
	
	MovieMin=`expr $i \* $ClipsMin`
	if [[ $Min -ge 60 && `expr $MovieMin % 60` -eq 0 ]]
	then
		Hour=`expr $MovieMin / 60`
		Hour="0$Hour"
		Min='00'
	fi
done
echo '执行结束';
