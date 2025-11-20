package FlujosFicheros;

import FlujosFicheros.Controller.OperacionesFicheros;

public class Main {
    public static void main (String[] args) {
        OperacionesFicheros operaciones = new OperacionesFicheros();

        //operaciones.lecturaFicheros ("src/main/java/FlujosFicheros/Ficheros/Escritura.txt");
        //operaciones.lecturaFicherosBuffer ("src/main/java/FlujosFicheros/Ficheros/Ejemplo.txt");
        //operaciones.escrituraSimple("src/main/java/FlujosFicheros/Ficheros/Escritura.txt");
        //operaciones.escrituraCompleja("src/main/java/FlujosFicheros/Ficheros/EscrituraBuffered.txt");
        operaciones.escrituraObjetos("src/main/java/FlujosFicheros/Ficheros/EscrituraObjetos.txt");

    }
}
