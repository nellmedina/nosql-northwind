for f in *.csv
do
    filename=$(basename "$f")
    extension="${filename##*.}"
    filename="${filename%.*}"
    mongoimport --uri "mongodb+srv://<username>:<password>@mongodb1-8fvmd.mongodb.net/northwind" -c "$filename" --type csv --file "$f" --headerline
done