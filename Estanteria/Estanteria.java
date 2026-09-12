public class Estanteria{

    private Estante[] estantes;
    private int cantidadEstantes;

    public Estanteria(int cantidadEstantes) {
        this.cantidadEstantes = cantidadEstantes;
        this.estantes = new Estante[cantidadEstantes];
        for (int i = 0; i < cantidadEstantes; i++) {
            estantes[i] = new Estante();
        }
    }

    public void agregarEstante(Estante estante, int posicion) {
        if (posicion < cantidadEstantes) {
            estantes[posicion] = estante;
        } else {
            System.out.println("No se pueden agregar más estantes, la estantería está llena.");
        }
    }

    public void buscarLibro(String titulo) {
        for (int i = 0; i < cantidadEstantes; i++) {
            for (int j = 0; j < estantes[i].getCantidadLibros(); j++) {
                if (estantes[i].getLibros()[j] != null && estantes[i].getLibros()[j].getNombre().equals(titulo)) {
                    System.out.println("Libro encontrado: " + estantes[i].getLibros()[j].getNombre() + " en el estante " + i + "número " + j);
                    return;
                }
            }
        }
        System.out.println("Libro no encontrado: " + titulo);
    }

    public void listarLibrosEnUnEstanteEspecifico(int posicion) {
        if (posicion < cantidadEstantes) {
            System.out.println("Libros en el estante " + posicion + ":");
            for (int j = 0; j < estantes[posicion].getCantidadLibros(); j++) {
                if (estantes[posicion].getLibros()[j] != null) {
                    System.out.println("- " + estantes[posicion].getLibros()[j].getNombre());
                }
            }
        } else {
            System.out.println("Posición de estante inválida.");
        }
    }

    public void cambiarOrdenDeLosLibrosEnUnEstante(int posicion) {
        if (posicion < cantidadEstantes) {
            Estante estante = estantes[posicion];
            Libro[] libros = estante.getLibros();
            for (int i = 0; i < libros.length / 2; i++) {
                Libro temp = libros[i];
                libros[i] = libros[libros.length - 1 - i];
                libros[libros.length - 1 - i] = temp;
            }
        } else {
            System.out.println("Posición de estante inválida.");
        }
    }

    public int calcularEdadPromedioDeLosLibrosEnUnEstante(int posicion) {
        if (posicion < cantidadEstantes) {
            Estante estante = estantes[posicion];
            Libro[] libros = estante.getLibros();
            int sumaEdades = 0;
            int cantidadLibros = 0;
            for (Libro libro : libros) {
                if (libro != null) {
                    sumaEdades += (2026 - libro.getAñoPublicacion());
                    cantidadLibros++;
                }
            }
            return cantidadLibros > 0 ? sumaEdades / cantidadLibros : 0;
        } else {
            System.out.println("Posición de estante inválida.");
            return 0;
        }
    }

    public String listarLibrosDeUnAutorEspecifico(String autor) {
        StringBuilder resultado = new StringBuilder("Libros de " + autor + ":\n");
        for (int i = 0; i < cantidadEstantes; i++) {
            Libro[] libros = estantes[i].getLibros();
            for (int j = 0; j < libros.length; j++) {
                if (libros[j] != null &&
                    libros[j].getAutor().equalsIgnoreCase(autor)) {
                        resultado.append("- ").append(libros[j].getNombre()).append("\n");
                    }
            }
        }
        return resultado.toString();
    }

}