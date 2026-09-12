public class Main {

    public static void main(String[] args){

        Plataforma plataforma = new Plataforma("Netflix");

        Contenido pelicula1 = plataforma.agregarPelicula(new Pelicula("Toy Story 3"));
        Contenido pelicula2 = plataforma.agregarPelicula(new Pelicula("Cars"));
        Contenido pelicula3 = plataforma.agregarPelicula(new Pelicula("Shrek"));
        Contenido pelicula4 = plataforma.agregarPelicula(new Pelicula("El Senior De Los Anillos"));
        Contenido pelicula5 = plataforma.agregarPelicula(new Pelicula("Batman"));
        Contenido pelicula6 = plataforma.agregarPelicula(new Pelicula("Alicia En El Pais De Las Maravillas"));
        Contenido pelicula7 = plataforma.agregarPelicula(new Pelicula("Metegol"));
        Contenido pelicula8 = plataforma.agregarPelicula(new Pelicula("Monsters Inc"));
        Contenido pelicula9 = plataforma.agregarPelicula(new Pelicula("Mi Villano Favorito"));
        Contenido pelicula10 = plataforma.agregarPelicula(new Pelicula("Lluvia De Hamburguesas"));

        Contenido serie1 = plataforma.agregarSerie(new Serie("Breaking Bad"));
        Contenido serie2 = plataforma.agregarSerie(new Serie("El Juego Del Calamar"));
        Contenido serie3 = plataforma.agregarSerie(new Serie("La Casa De Papel"));
        Contenido serie4 = plataforma.agregarSerie(new Serie("Envidiosa"));
        Contenido serie5 = plataforma.agregarSerie(new Serie("Los Soprano"));

        Usuario usuario1 = plataforma.registrarUsuario(new Usuario("juan0505"));
        Usuario usuario2 = plataforma.registrarUsuario(new Usuario("salvi1005"));
        Usuario usuario3 = plataforma.registrarUsuario(new Usuario("mili1711"));
        Usuario usuario4 = plataforma.registrarUsuario(new Usuario("chiqui0512"));
        Usuario usuario5 = plataforma.registrarUsuario(new Usuario("pau0602"));
        Usuario usuario6 = plataforma.registrarUsuario(new Usuario("ale0709"));
        Usuario usuario7 = plataforma.registrarUsuario(new Usuario("tito1508"));

        usuario1.verContenido(pelicula1);
        usuario2.verContenido(pelicula1);
        usuario3.verContenido(pelicula1);
        usuario4.verContenido(pelicula1);
        usuario5.verContenido(pelicula1);
        usuario6.verContenido(pelicula1);
        usuario7.verContenido(pelicula1);

        usuario1.verContenido(pelicula2);
        usuario2.verContenido(pelicula2);
        usuario3.verContenido(pelicula2);
        usuario4.verContenido(pelicula2);
        usuario5.verContenido(pelicula2);
        usuario6.verContenido(pelicula2);

        usuario1.verContenido(pelicula3);
        usuario2.verContenido(pelicula3);
        usuario3.verContenido(pelicula3);
        usuario4.verContenido(pelicula3);
        usuario5.verContenido(pelicula3);

        usuario1.verContenido(pelicula4);
        usuario2.verContenido(pelicula4);
        usuario3.verContenido(pelicula4);
        usuario4.verContenido(pelicula4);

        usuario1.verContenido(pelicula5);
        usuario2.verContenido(pelicula5);
        usuario3.verContenido(pelicula5);

        usuario1.verContenido(pelicula6);
        usuario2.verContenido(pelicula6);

        usuario2.verContenido(pelicula7);

        usuario7.verContenido(pelicula8);
        usuario6.verContenido(pelicula8);

        usuario5.verContenido(pelicula9);
        usuario4.verContenido(pelicula9);

        usuario3.verContenido(pelicula10);
        usuario2.verContenido(pelicula10);
        usuario1.verContenido(pelicula1);

        usuario1.verContenido(serie1);
        usuario2.verContenido(serie1);
        usuario3.verContenido(serie1);
        usuario4.verContenido(serie1);
        usuario5.verContenido(serie1);

        usuario2.verContenido(serie2);
        usuario6.verContenido(serie2);
        usuario7.verContenido(serie2);
        usuario3.verContenido(serie2);

        usuario1.verContenido(serie3);
        usuario4.verContenido(serie3);
        usuario5.verContenido(serie3);

        usuario2.verContenido(serie4);
        usuario6.verContenido(serie4);

        usuario5.verContenido(serie5);

        plataforma.mostrarContenidoMasVisto();

        plataforma.mostrarHistorialDeUnUsuario(usuario1);

        plataforma.mostrarTop5Peliculas();

    }
    
}
