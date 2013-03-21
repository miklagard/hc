for easy-thumbnails i had to install PIL like that:
sudo apt-get install libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev

for i in libjpeg.so libfreetype.so libz.so
    do ln -s /usr/lib/x86_64-linux-gnu/$i $VIRTUAL_ENV/lib/
done
pip uninstall pil
pip install pil
