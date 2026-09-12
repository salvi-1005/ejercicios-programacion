public class Main {

    public static void main(String[] args) {
        
        Pagina pagina1 = new Pagina(1, "Contenido de la página 1");
        Pagina pagina2 = new Pagina(2, "Contenido de la página 2");
        Pagina pagina3 = new Pagina(3, "Contenido de la página 3");

        Capitulo capitulo1 = new Capitulo("Capítulo 1", 10);
        capitulo1.agregarPagina(pagina1);
        capitulo1.agregarPagina(pagina2);

        Capitulo capitulo2 = new Capitulo("Capítulo 2", 10);
        capitulo2.agregarPagina(pagina3);

        System.out.println("Cantidad de páginas en el capítulo 1: " + capitulo1.getCantidadPaginas());
        System.out.println("Página inicial del capítulo 1: " + capitulo1.getPaginaInicial());
        System.out.println("Página final del capítulo 1: " + capitulo1.getPaginaFinal());
        System.out.println("Total de palabras en el capítulo 1: " + capitulo1.contarPalabras());
        System.out.println("Total de caracteres en el capítulo 1: " + capitulo1.contarCaracteres());

        capitulo1.eliminarPagina(2);
        System.out.println("Cantidad de páginas en el capítulo 1 después de eliminar la página 2: " + capitulo1.getCantidadPaginas());

        Pagina paginaBuscada = capitulo1.buscarPagina(1);
        if (paginaBuscada != null) {
            System.out.println("Página encontrada: " + paginaBuscada.getContenido());
        } else {
            System.out.println("Página no encontrada.");
        }
    }

}