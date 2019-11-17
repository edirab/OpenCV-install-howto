### Инструкция по сборке OpenCV 4.1.1 под Windows

##### Глава 1. Сборка
***
1. Скачиваем с github.com opencv-4-1-1 и opencv-contrib-4-1-1 (последние стабильные на момент сборки)

        Branch: master -> Tags -> 4.1.1

2. Распаковываем в удобные папки. У меня это были 

        C:\Program Files\opencv-4-1-1 и 
        C:\Program Files\opencv-contrib-4-1-1

3. Скачиваем последний cmake (3.16.0)

       Нам понадобится cmake-gui.exe
       Кнопка Configure -> проект под MSVS 2019, конфигурация х64, native compiler
	
4. После чего начинается чтение файлов CMake

5. Меняем следующие параметы:

    0. `OPENCV_EXTRA_MODULES_PATH = "C:/Program Files/opencv-contrib-4-1-1/modules"`
        - backslahs заменяем на foreslash
            
	0. `ENABLE_PRECOMPILED_HEADERS = flase`
	
	0. `WITH_PROTOBUF = false`
	
	0. `OPENCV_ENABLE_NONFREE = true`
	
	0. `WITH_GSTREAMER = false`
	
	        В системе должен быть установлен python 2 и python 3
	
	0. `PYTHON2_EXECUTABLE = "C:/Program Files/Python27/python.exe"`
	
	0. `CMAKE_CONFIGURATION_TYPES = Release; Debug`
	    
	    - нужно собирать обе версии, по умолчанию включено
	
	0. Дополнительно можно сразу подключить библиотеку Eigen
	
6. Снова жмём configure
7. Если ошибок нет, жмём Generate. Если есть - гуглим и фиксим
8. Запускаем Visual Studio **от администратора**. Заходим в папку C:\Program Files\opencv-4-1-1\build,
там открываем файл OpenCV.sln

9. Нажимаем собрать решение) Ждём минут 30-40.
10. Как итог будет: собрано 149, ошибок 0, пропущено 9
11. Правый клик по решению - Свойства - Свойства конфигурации - отключаем BUILD_ALL и включаем INSTALL
12. Снова собираем и, о чудо, появилась папка с именем install в build
13. Повторяем тоже самое для другой конфигурации.

##### Глава 2. Установка
***

Во вновь созданном решении переходим

        Проект - Свойства - ...
        
   **АХТУНГ! Сразу же переключаемся на "Все конфигурации"** 
        
1. ... С\С++ - Дополнительные каталоги включаемых библиотек -
 
        `C:\Program Files\opencv-4-1-1\build\install\include` 

2. ... Компоновщик - Общее - Дополнительные каталоги включаемых библиотек -

        Это путь до наших dll'ек
        C:\Program Files\opencv-4-1-1\build\install\x64\vc16\bin
        
3. ... Компоновщик - Ввод - Дополнительные зависимости -

        Сюда нужно прописать все lib'ы
        *d.lib означает debug
        
        opencv_aruco411d.lib
        opencv_bgsegm411d.lib
        opencv_bioinspired411d.lib
        opencv_calib3d411d.lib
        opencv_ccalib411d.lib
        opencv_core411d.lib
        opencv_datasets411d.lib
        opencv_dpm411d.lib
        opencv_face411d.lib
        opencv_features2d411d.lib
        opencv_flann411d.lib
        opencv_fuzzy411d.lib
        opencv_gapi411d.lib
        opencv_hdf411d.lib
        opencv_hfs411d.lib
        opencv_highgui411d.lib
        opencv_imgcodecs411d.lib
        opencv_imgproc411d.lib
        opencv_img_hash411d.lib
        opencv_line_descriptor411d.lib
        opencv_ml411d.lib
        opencv_objdetect411d.lib
        opencv_optflow411d.lib
        opencv_phase_unwrapping411d.lib
        opencv_photo411d.lib
        opencv_plot411d.lib
        opencv_quality411d.lib
        opencv_reg411d.lib
        opencv_rgbd411d.lib
        opencv_saliency411d.lib
        opencv_shape411d.lib
        opencv_stereo411d.lib
        opencv_stitching411d.lib
        opencv_structured_light411d.lib
        opencv_superres411d.lib
        opencv_surface_matching411d.lib
        opencv_tracking411d.lib
        opencv_video411d.lib
        opencv_videoio411d.lib
        opencv_videostab411d.lib
        opencv_xfeatures2d411d.lib
        opencv_ximgproc411d.lib
        opencv_xobjdetect411d.lib
        opencv_xphoto411d.lib
        
4. Для конфигурации Release делаем тоже самое, только с другими lib'ами
 
        ... Компоновщик - Ввод - Дополнительные зависимости - *.lib

##### Глава 3. Использование
***
   
1. В Windows 10 для доступа приложений к камере необходимо изменить параметры конфиденциальности.
    
        Все параметры - Конфиденциальность - Доступ к камере - Разрешить приложениям доступ к камере 