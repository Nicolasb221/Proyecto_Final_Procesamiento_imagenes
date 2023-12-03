# Proyecto_Final_Procesamiento_imagenes

Integrantes:

-Nicolás Enrique Rodriguez Villate

-Nicolás Alberto Bravo Silva

Enlace video youtube: https://www.youtube.com/watch?v=8M7WWgUi6AM&feature=youtu.be 

Todos los datasets, son propios y fueron extraídos por el grupo, por lo que son varias imágenes y se encuentran en archivos comprimidos, tanto aquí, como en Blackboard.

El proyecto consiste en detectar un objeto en video con las herramientas de opencv, como lo son Matching Template y Contornos; y poder observar lo que le sucede en el tiempo a través de una gráfica, la cuál servira como punto de partida para realizar mejores análisis en los ámbitos de las ciencias básicas.

Primero fue escencial utilizar el código de Sacar_frames.py, donde encuentra los fotogramas del video ingresado, llamado en este caso Video3.mp4:

![18](https://user-images.githubusercontent.com/51700993/101202133-d7b48d00-3636-11eb-8a1d-9e789f08ac19.png)

Además también se encuentran unas funciones para hallar la duración del video y de cada fotograma, para contar con el tiempo y poder generar el eje correctamente en x y tener los datos muy bien mapeados, de posición contra el tiempo.

Seguido de esto, se utiliza el código de Object_detection.py, el cuál es encargado de utilizar el algoritmo de Matching Template, encargado de detectar el objeto necesario en la imagen de cada fotograma anteriormente hallado:

![Frame_detected18](https://user-images.githubusercontent.com/51700993/101202449-4560b900-3637-11eb-9a2a-5aff30739590.png)

Para poder encontrar las coordenadas necesarias, se usa contornos en el código centro.py, ya que podemos tener el área y ubicar el punto en el centro del objeto, para después imprimir los datos en dos bloc de notas, con los datos de x y de y, para posteriormente generar la gráfica correspondiente para tener un análisis más acertado de los datos que se necesitan usar. A continuación, un ejemplo de una de las imágenes con contornos, y con las coordenadas dadas:

![Area_imagen18](https://user-images.githubusercontent.com/51700993/101202463-4c87c700-3637-11eb-9eb4-8bc9b3123db5.png)

Como último proceso, se realizo la gráfica de los datos obtenidos por la posición en x y en y; obteniendo una muy buena aproximación de lo que es el recorrido del objeto utilizado:

![WhatsApp Image 2020-12-04 at 3 32 48 PM](https://user-images.githubusercontent.com/51700993/101212020-0be37a00-3646-11eb-9737-e2760dbba3fa.jpeg)
