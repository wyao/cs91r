for i in 5 10 20 50 100 200 500 1000 5000 10000
do
    python ps1.py -n$i -m$i -r$((2*i)) -i5 >> varyN.txt
done

for i in 5 10 20 50 100 200 500 1000 5000 10000
do
    python ps1.py -n$i -m$i -r$i -i5 >> lowMissRate.txt
done

for i in 5 10 20 50 100 200 500 1000 5000 10000
do
    python ps1.py -n$i -m$i -r$((10*i)) -i5 >> highMissRate.txt
done

for i in 5 10 20 50 100 200 500 1000 5000 10000
do
    python ps1.py -n$i -m$((i/5)) -r$((2*i)) -i5 >> fewLookups.txt
done