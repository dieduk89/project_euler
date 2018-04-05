#! /bin/bash

show_help ()
{
	echo "Help";
}

list_ex ()
{
	echo "List" $1;
}

run_file () 
{
	case "$1" in
	"python") 	start_time=$(date +%s%N)/1000;
				python "python/exercise $2/code$3.py";
				finish_time=$(date +%s%N)/1000;
		
				echo "Duration: $((finish_time - start_time)) microseconds.";
				;;
	*)			echo "Unsuported language";	
				;;	
	esac				
}

case "$#" in
	0)	show_help
		;;
	1)	list_ex	$1
		;;
	2)	run_file $1 $2 1
		;;
	3)	run_file $1 $2 $3
		;;
	*)	echo "Too much arguments";
		;;			
esac
