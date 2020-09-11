## Preparación
* Definir directorio de trabajo
* Borrar archivos temporales

## Proceso
* Lista de documentos a procesar es un archivo .csv en un formato predeterminado
	* Lista de columnas: 
	* Separador: "|"
	* Cada linea es un documento: un veredicto
	* **El archivo se carga en un arreglo de vectores**
* La información del archivo .csv se usará para llenar una plantilla. Es necesario conectar el contenido de cada fila en la variable adecuada.
* Diccionario
	* Hay una definición de etiquetas para las variables de la plantilla

* Leer archivo .csv
* Loop sobre las lineas
	* Cargar diccionario
	* Generar archivo del veredicto: correlativo_CI_estudiante_apellido_nombre.odt
	* Sustituir valores en el archivo de veredicto
	* Agregar linea en historial de veredictos generados por enviar:
		* Copiar linea del archivo original
* Borrar archivo .csv (input)
