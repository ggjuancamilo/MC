#genera un directorio donde se trabajara todo
mkdir JuanGallego_hw1
cp tanual.py JuanGallego_hw1
cp tempvsalt2014.py JuanGallego_hw1
cp tpatrones.py JuanGallego_hw1
cp varilla.py JuanGallego_hw1

#me lleva a tal dir
cd JuanGallego_hw1

# Descarga el archivo
wget https://github.com/ComputoCienciasUniandes/MetodosComputacionales/raw/master/homework/2016-01/hw1/IDEAM.txt.zip

#descomprime el archivo a utilizar
unzip IDEAM.txt.zip

#toma todas las lineas con la palabra Estacion y toma el num de la estacion, seguido por la latitud y dpto, longitud y elevacion.
grep ESTACION IDEAM.txt | awk '{print $10;}'> Estacion.csv

grep LATITUD IDEAM.txt | awk '{print $2 $3 ",",$8;}' > Latitud.csv

grep LONGITUD IDEAM.txt | awk '{print $2 $3;}' > Longitud.csv

grep ELEVACION IDEAM.txt | awk '{print $2 $3;}' > Elevacion.csv

#genera un arch csv con la con las columnas Estacion, Latitud, dpto, longitud, elevacion respectivamente boonito
paste Estacion.csv Latitud.csv Longitud.csv Elevacion.csv | awk '{print $1,",",$2,$3,","$4,","$5,",",$6;}' > clavex.csv
uniq -c clavex.csv > clave.csv
#elimina archivos inservibles
rm Estacion.csv
rm Latitud.csv
rm Longitud.csv
rm Elevacion.csv
rm clavex.csv
sed -i 's/^........//g' clave.csv

awk '{print $1}' clave.csv > est.txt



#Genera csv con estacion y año
awk '/VALORES MEDIOS  DIARIOS DE TEMPERATURA/,/MEDIA DE MAXIMOS/' IDEAM.txt | awk '/ANO/'|awk '{print $10,","$7;}' > EstAno.csv  

#toma los valores medios mensuales
awk '/VALORES MEDIOS  DIARIOS DE TEMPERATURA/,/MEDIA DE MAXIMOS/' IDEAM.txt | awk '/MEDIA  /' > int1.csv
grep -v INCOMPLETOS int1.csv > int2.csv
grep -v REGISTRADOS int2.csv > todobello.csv
rm int1.csv
rm int2.csv


#comandos para limpiar porqueria
sed -i 's/ 1 /   /g' todobello.csv
sed -i 's/ 2 /   /g' todobello.csv
sed -i 's/ 3 /   /g' todobello.csv
sed -i 's/ 4 /   /g' todobello.csv
sed -i 's/ 5 /   /g' todobello.csv
sed -i 's/ 6 /   /g' todobello.csv
sed -i 's/ 7 /   /g' todobello.csv
sed -i 's/ 8 /   /g' todobello.csv
sed -i 's/ 3.$//g' todobello.csv
cut -c 1-124 todobello.csv > todobellob.csv
rm todobello.csv
cp todobellob.csv todobello.csv
sed -i 's/ 4/  /g' todobello.csv
sed -i 's/ 5/  /g' todobello.csv
sed -i 's/ 6/  /g' todobello.csv
sed -i 's/ 3/  /g' todobello.csv
sed -i 's/ 8/  /g' todobello.csv
sed -i 's/*/ /g' todobello.csv


cp todobello.csv todobello.txt
rm todobello.csv

sed -i 's/MEDIA               //g' todobello.txt
sed -i 's/         /,/g' todobello.txt
sed -i 's/     /,/g' todobello.txt

cp todobello.txt todobello.csv

# genera el archivo tempvst
paste EstAno.csv todobello.csv > tempvstiempo.csv

cp tempvstiempo.csv tempvstiempoo.txt

sed 's/,,/,     /g' tempvstiempoo.txt | sed 's/,/ /g' > tempvstiempo.txt




#Genero un .csv con los datos medio de temperatura anuales
awk '/VALORES MEDIOS  DIARIOS DE TEMPERATURA/,/I D E A M/' IDEAM.txt | awk '/VALORES  ANUALES/,/MEDIA/' | grep 'MEDIA' | awk '{print $2}' > mediaAnual.csv
paste EstAno.csv mediaAnual.csv > tAnual.csv
cp tAnual.csv tAnual.txt
sed -i 's/,//g' tAnual.txt


#toma las elevacione
awk '/VALORES MEDIOS  DIARIOS DE TEMPERATURA/,/MEDIA DE MAXIMOS/' IDEAM.txt | grep 'ELEVACION'|awk '{print $2;}' > elevacion.csv
#genera un archivo con las temperaturas vs las alturas
paste EstAno.csv elevacion.csv mediaAnual.csv > patrones.csv
awk '{print $1,$2,",",$3,",",$4}' patrones.csv > tempvsaltt.csv

grep 2014 tempvsaltt.csv > tempvsalt.txt
sed -i 's/,/ /g' tempvsalt.txt
rm tempvsaltt.csv
rm patrones.csv
rm elevacion.csv
rm mediaAnual.csv
rm EstAno.csv
rm todobello.csv
rm todobellob.csv
rm todobello.txt

#corre los .py
python tanual.py 
python tempvsalt2014.py
python tpatrones.py
python varilla.py
