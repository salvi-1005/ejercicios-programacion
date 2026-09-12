import java.util.ArrayList;

public class Usuario {

    private String nombreDeUsuario;
    private ArrayList<Publicacion> publicaciones;
    private int seguidores;
    private int seguidos;
    private ArrayList<Usuario> amigos;
    private int numeroDeAmigos;
    private ArrayList<Usuario> solicitudesPendientes;

    public Usuario(String nombreDeUsuario, int seguidores, int seguidos) {
        this.nombreDeUsuario = nombreDeUsuario;
        this.publicaciones = new ArrayList<>();
        this.seguidores = seguidores;
        this.seguidos = seguidos;
        this.amigos = new ArrayList<>();
        this.numeroDeAmigos = 0;
        this.solicitudesPendientes = new ArrayList<>();
    }

    public void realizarPublicacion(Publicacion publicacion) {
        publicaciones.add(publicacion);
    }

    public void agregarAmigo(Usuario usuario) {
        this.seguidos++;
        this.seguidores++;
        usuario.seguidos++;
        usuario.seguidores++;
        amigos.add(usuario);
        numeroDeAmigos++;
        usuario.amigos.add(this);
        usuario.numeroDeAmigos++;
    }

    public void eliminarAmigo(Usuario usuario) {
        if (amigos.remove(usuario)) {
            this.seguidos--;
            this.seguidores--;
            usuario.seguidos--;
            usuario.seguidores--;
            numeroDeAmigos--;
            usuario.amigos.remove(this);
            usuario.numeroDeAmigos--;
        }
    }

    public void enviarSolicitudDeAmistad(Usuario usuario) {
        if (!amigos.contains(usuario)) {
            solicitudesPendientes.add(usuario);
            System.out.println("Solicitud de amistad enviada a " + usuario.getNombreDeUsuario());
        } else {
            System.out.println("Ya eres amigo de " + usuario.getNombreDeUsuario());
        }
    }

    public void aceptarSolicitudDeAmistad(Usuario usuario) {
        if (!amigos.contains(usuario)) {
            solicitudesPendientes.remove(usuario);
            agregarAmigo(usuario);
            seguidores ++;
            usuario.seguidos ++;
            System.out.println("Solicitud de amistad aceptada. Ahora eres amigo de " + usuario.getNombreDeUsuario());
        } else {
            System.out.println("Ya eres amigo de " + usuario.getNombreDeUsuario());
        }
    }

    public void mostrarFeedDeNoticias() {
        System.out.println("Feed de noticias de " + nombreDeUsuario + ":");
        for (Publicacion publicacion : publicaciones) {
            System.out.println(publicacion.getTitulo() + " - " + publicacion.getContenido() + " (Likes: " + publicacion.getCantidadDeLikes() + ")");
        }
        for (Usuario amigo : amigos) {
            for (Publicacion publicacion : amigo.publicaciones) {
                System.out.println(publicacion.getTitulo() + " - " + publicacion.getContenido() + " (Likes: " + publicacion.getCantidadDeLikes() + ") - Publicado por: " + amigo.nombreDeUsuario);
            }
        }
    }

    public void darLikeAPublicacion(Usuario amigo, String titulo) {
    if (amigos.contains(amigo) && amigo.amigos.contains(this)) {
        for (Publicacion p : amigo.publicaciones) {
            if (p.getTitulo().equals(titulo)) {
                p.setCantidadDeLikes(p.getCantidadDeLikes() + 1);
                return;
            }
        }
    }
    System.out.println("No puedes dar like a esta publicación.");
    }

    public void calcularEstadisticas() {
        System.out.println("Usuario: " + nombreDeUsuario);
        System.out.println("Número de publicaciones: " + publicaciones.size());
        System.out.println("Número de seguidores: " + seguidores);
        System.out.println("Número de seguidos: " + seguidos);
        System.out.println("Número de amigos: " + numeroDeAmigos);
        System.out.println("Promedio de likes por publicación: " + calcularPromedioLikes());
    }

    public double calcularPromedioLikes() {
        int totalLikes = 0;
        for (Publicacion publicacion : publicaciones) {
            totalLikes += publicacion.getCantidadDeLikes();
        }
        return publicaciones.isEmpty() ? 0 : (double) totalLikes / publicaciones.size();
    }

    public String getNombreDeUsuario() {
        return nombreDeUsuario;
    }

}