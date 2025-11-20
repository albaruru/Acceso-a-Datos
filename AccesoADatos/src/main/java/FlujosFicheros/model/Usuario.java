package FlujosFicheros.model;

import lombok.*;
import java.io.Serializable;

// CON LA LIBRERIA LOMBOK PUEDO PONER DIRECTAMENTE ESTO:
    //Getters y setters
    //@Getter
    //@Setter

    //Getters, setters y ToString
    @Data
    //Constructor con TODOO
    @AllArgsConstructor
    //Constructor vacio
    @NoArgsConstructor

    public class Usuario {
        //ATRIBUTOS
        private  static Long SerialVersionUID = 1L;
        private int id;
        private String nombre, apellido, correo, dni;
        private int telefono;


        public Usuario(int i, String alba, String ruano, String correo, String s, String number) {
        }
    }
