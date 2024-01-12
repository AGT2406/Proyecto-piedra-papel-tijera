# PROYECTO-RPS

Este proyecto consta de una carpeta "doc" que contiene la tabla del entorno de tareas, la imagen del agente, y la explicación del programa RPS y un pequeño archivo con la información adicional que lleva el programa RPSLS.

En la carpeta SCR está el juego de piedra_papel_tijera (RPS) y de piedra_papel_tijera_lagarto_spock (RPLS)

En la carpeta "test" está el pytest para hacer las pruebas del programa completo (RPLS)

En la raíz se encuentran el archivo pytest y el gitignore.

El juego intenta cumplir con la OCP, ya que está abierto a la extensión y cerrado a la modificación, ya que no necesita modificarse para agregar nuevas opciones, simplemente se agregarían en "acciones_juego", ya que la lógica está basada en una lista de acciones. La única parte que podría no ser tan fácil de extender sería en el apartado de "evaluar_juego", ya que la lógica está incorporada en condiciones específicas en "evaluar_juego", y habría que modificar esa función. 

El juego también cumple con la SRP ya que la IA se encarga de aprender y elegir las acciones basadas en jugadas aprendidas, y puede cambiar si la lógica para elegir las acciones se modifica o si se agregan más opciones de juego. Cumple ya que tiene una única responsabilidad, gestionar la lógica de la IA. 
