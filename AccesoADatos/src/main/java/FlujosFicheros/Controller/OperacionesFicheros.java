package FlujosFicheros.Controller;


import FlujosFicheros.model.Usuario;

import javax.imageio.IIOException;
import java.io.*;

public class OperacionesFicheros {

/*
    //PARA LEER MEDIENTE UN FILEREADER QUE ES LETRA A LETRA
    public void lecturaFicheros(String path) {
        File file = new File(path);
        // Si queremos comprobar si existe o no
        //if(!file.exists()){
        //    file.createNewFile();
        // }
        FileReader fileReader = null; // Se pone null porque hay que cerrar
        try {
            fileReader = new FileReader(file);
            // Esta linea seria para leer solo un numero ->  int numero = fileReader.read();  // read puede dar error de compilacion por eso se ponen excepciones
            int numero;
            while ((numero = fileReader.read()) != -1) {
                System.out.println((char) (numero/9)); // me devuelve todas las letras
            }
            //System.out.println((char) numero);// con char pasamos de numero a letra
        } catch (IOException e) {
            System.out.println("No puedes hacer la lectura");
        } finally {
            try {
                fileReader.close();

            } catch (IOException | NullPointerException e) { // | es or esto o esto
                System.out.println("Error al cerrar");
            }
        }
    }

    //PARA LEER MEDIENTE UN BUFFERREADER QUE ES FUILA A FILA
    public void lecturaFicherosBuffer(String path) {
        File file = new File(path);
        // Si queremos comprobar si existe o no
        //if(!file.exists()){
        //    file.createNewFile();
        // }
        BufferedReader bufferedReader = null; // Se pone null porque hay que cerrar

        try {
            bufferedReader = new BufferedReader(new FileReader(file));
            String linea = null;
            while ((linea = bufferedReader.readLine()) != null) {
                System.out.println(linea);
            }


        } catch (IOException e) {
            System.out.println("No puedes hacer la lectura");

        } finally {

            try {
                bufferedReader.close();

            } catch (IOException | NullPointerException e) { // | es or esto o esto
                System.out.println("Error al cerrar");
            }
        }
    }
 */
/*
    //ESCRITURA SENCILLA
    public void escrituraSimple (String path) {
        File file = new File(path); //creamos

        //comprobamos si existe o no
        if (!file.exists()){
            try {
                file.createNewFile();
            } catch (IOException e) {
                System.out.println("La creacion no se puede dar");
            }
        }

        FileWriter fileWriter = null; // Se pone null porque hay que cerrar
        String mensaje = "El enunciado del examen es este: XXX";

        try {
            fileWriter = new FileWriter(file,true); //posibilidad de fallo por no tener permisos de escritura
            //fileWriter.write(mensaje); // lo que se ponga en los parentesis lo escribe, los numeros significan caracteres o letras pero si lo escribes entre comillas se escribe bien. puedes meter una variable.
            for (int i = 0; i < mensaje.length() ; i++) { //bucle para leer el mensaje completo
                char letra = mensaje.charAt(i); // para sacar la letra
                //System.out.println(letra); //saca a consola letra a letra
                //System.out.println((int)letra); //saca a consola los valores numericos de las letras
                fileWriter.write(((int)letra)*9); //saca a consola letra a letra
            }


        } catch (IOException e) {
            System.out.println("No puedes escribir");
        } finally {
            try {
                fileWriter.close();
            } catch (IOException | NullPointerException e) {
                System.out.println("Error en el cerrado de fichero.");
            }
        }


    }

    public void escrituraCompleja (String path) {
        File file = new File(path);
        if (!file.exists()); {
            try {
                file.createNewFile();
            } catch (IOException e) {
                System.out.println("Error en el IO");
            }
        }
        PrintWriter printWriter =null;

        try {
            printWriter = new PrintWriter(new FileWriter(file,true));
            printWriter.println("Esta es la primera linea.");
            printWriter.println("Esta es la segunda linea.");

        } catch (IOException e) {
            System.out.println("Error en el IO");
        } finally {
            try {
                printWriter.close();
            } catch (NullPointerException e) {
                System.out.println("Error en el cerrado");
            }
        }
    }

 */

    public void escrituraObjetos (String path){

        Usuario usuario = new Usuario(1,"alba","ruano","correo","123A","123");
        File file =  new File (path);

        if (!file.exists()){
            try {
                file.createNewFile();
            } catch (IOException e) {
                System.out.println("No tienes permisos de creacion");
            }
        }

        ObjectOutputStream dos = null;

        try {
            dos = new ObjectOutputStream(new FileOutputStream(file));
            dos.writeObject(usuario);

        } catch (FileNotFoundException e) {
            System.out.println("Fichero indicado incorrecto");

        } catch (IOException e) {
            System.out.println("No puedes escribir");

        } finally {
            try {
                dos.close();
            } catch (IOException | NullPointerException e) {
                System.out.println("El fichero no se puede cerrar");
            }
        }

    }


}
