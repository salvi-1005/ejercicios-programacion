import java.util.ArrayList;

public class Plataforma {

    private String nombre;
    private ArrayList<Contenido> contenido;
    private ArrayList<Usuario> usuarios;

    public Plataforma(String nombre){
        this.nombre = nombre;
        this.contenido = new ArrayList<>();
        this.usuarios = new ArrayList<>();
    }

    public String getNombre(){
        return this.nombre;
    }

    public Pelicula agregarPelicula(Pelicula pelicula){
        contenido.add(pelicula);
        return pelicula;
    }

    public Serie agregarSerie(Serie serie){
        contenido.add(serie);
        return serie;
    }

    public Usuario registrarUsuario(Usuario usuario){
        usuarios.add(usuario);
        return usuario;
    }

    public void mostrarContenidoMasVisto(){
        System.out.println("El contenido mas visto es: ");
        Contenido contenidoMasVisto = null;
        for (Contenido cont : contenido){
            if (contenidoMasVisto == null || cont.getCantidadVisualizaciones() > contenidoMasVisto.getCantidadVisualizaciones()){
                contenidoMasVisto = cont;
            }
        }
        if (contenidoMasVisto != null){
            System.out.println(contenidoMasVisto.getNombre() + " con " + contenidoMasVisto.getCantidadVisualizaciones() + " visualizaciones");
        } else{
            System.out.println("No hay contenido en la plataforma");
        }
    }

    public void mostrarHistorialDeUnUsuario(Usuario usuario){
        System.out.println("Historial de " + usuario.getNombre() + ":");
        for (Contenido c : usuario.getHistorial()){
            System.out.println(c.getNombre());
        }
    }

    public void mostrarTop5Peliculas(){
        System.out.println("Las 5 peliculas mas vistas son: ");
        ArrayList<Pelicula> peliculas = new ArrayList<>();
        for (Contenido cont : contenido){
            if (cont instanceof Pelicula){
                peliculas.add((Pelicula) cont);
            }
        }
        peliculas.sort((p1, p2) -> Integer.compare(p2.getCantidadVisualizaciones(), p1.getCantidadVisualizaciones()));
        for (int i = 0; i < Math.min(5, peliculas.size()); i++){
            System.out.println("- " + (i+1) + " " + peliculas.get(i).getNombre() + " (" + peliculas.get(i).getCantidadVisualizaciones() + ")");
        }
        
    }
}
