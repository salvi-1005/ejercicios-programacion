public class Main {

    public static void main(String[] args) {
        
        Usuario usuario1 = new Usuario("salvi.dangelo", 0, 0);
        Usuario usuario2 = new Usuario("tomeravner84", 0, 0);

        Publicacion publicacion1 = new Publicacion("Mi primer post", "¡Hola a todos! Esta es mi primera publicación en esta red social.", usuario1);
        Publicacion publicacion2 = new Publicacion("Mi segundo post", "¡Estoy emocionado de compartir más contenido con ustedes!", usuario1);
        Publicacion publicacion3 = new Publicacion("¡Hola a todos!", "¡Estoy emocionado de unirme a esta red social!", usuario2);
        Publicacion publicacion4 = new Publicacion("Mi primer post", "¡Hola a todos! Esta es mi primera publicación en esta red social.", usuario2);

        usuario1.realizarPublicacion(publicacion1);
        usuario1.realizarPublicacion(publicacion2);
        usuario2.realizarPublicacion(publicacion3);
        usuario2.realizarPublicacion(publicacion4);

        usuario1.agregarAmigo(usuario2);
        usuario1.mostrarFeedDeNoticias();
        usuario1.calcularEstadisticas();
        usuario1.darLikeAPublicacion(usuario2, "¡Hola a todos!");
        System.out.println("Likes en la publicación de " + publicacion3.getAutor().getNombreDeUsuario() + ": " + publicacion3.getCantidadDeLikes());
        usuario2.calcularEstadisticas();


    }
}