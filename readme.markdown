forked from: https://github.com/tpisto/pdf-fill-form

pre-compiled dylibs for the `pdf-fill-form` node module so we can run it on
heroku at AutoFi

on heroku, export `LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/app/opt/lib`

install qt5 and link it to poppler on linux:
```bash
cd /app && export opt=/app/opt && echo $opt \
  && export {CFLAGS="-I$opt/include",CXXFLAGS="-I$opt/include -Wno-switch -std=c++11",LDFLAGS=-L$opt/lib,PKG_CONFIG_PATH=$opt/lib/pkgconfig,PATH=$PATH:$opt/bin} \
  && wget https://download.qt.io/official_releases/qt/5.7/5.7.1/single/qt-everywhere-opensource-src-5.7.1.tar.xz \
  && tar xvf qt-everywhere-opensource-src-5.7.1.tar.xz \
  && cd qt-everywhere-opensource-src-5.7.1 \
  && ./configure -prefix $opt -c++std c++11 \
    -opensource -confirm-license -release -accessibility \
    -qt-zlib -qt-libpng -qt-libjpeg -qt-xcb -qt-pcre \
    -no-glib -no-cups -no-sql-sqlite -no-qml-debug -no-opengl -no-egl -no-largefile \
    -no-xinput2 -no-sm -no-icu -nomake examples -nomake tests \
    -skip qtactiveqt -skip qtlocation -skip qtmultimedia -skip qtserialport \
    -skip qtquickcontrols -skip qtscript -skip qtsensors -skip qtwebsockets \
    -skip qtxmlpatterns -skip qt3d -skip qtvirtualkeyboard \
  && make -j4 \
  && make install && cd .. && rm -rf qt-*

cd /app && export opt=/app/opt && echo $opt \
  && export {CFLAGS="-I$opt/include -Wno-return-type",CXXFLAGS="-I$opt/include -Wno-return-type -std=c++11",LDFLAGS=-L$opt/lib,PKG_CONFIG_PATH=$opt/lib/pkgconfig,PATH=$PATH:$opt/bin} \
  && wget https://poppler.freedesktop.org/poppler-0.51.0.tar.xz \
  && tar xvf poppler-0.51.0.tar.xz && cd poppler-0.51.0 \
  && ./configure \
    --prefix=$opt \
    --enable-build-type=release \
    --disable-poppler-qt4 \
    --disable-poppler-cpp \
    --disable-static \
  && make -j4 \
  && make install && cd .. && rm -rf poppler-*
```
