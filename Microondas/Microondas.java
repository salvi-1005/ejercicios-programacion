public class Microondas {

    private boolean puertaAbierta;
    private Comida comida;
    private boolean enCoccion;
    private int intensidad;
    private int segundosTotales;

    public Microondas(){
        this.puertaAbierta = true;
        this.comida = null;
        this.enCoccion = false;
    }

    public void abrirPuerta() {
        if (!enCoccion) {
            puertaAbierta = true;
        } else {
            System.out.println("No se puede abrir mientras cocina");
        }
    }

    public void cerrarPuerta() {
        puertaAbierta = false;
    }

    public void insertarComida(Comida c){
        if (puertaAbierta && comida == null) {
            comida = c;
        } else {
            System.out.println("No se puede insertar comida");
        }
    }

    public void retirarComida(){
        if (puertaAbierta && comida != null) {
            comida = null;
        } else {
            System.out.println("No se puede retirar comida");
        }
    }

    public void iniciarCoccion(int intensidad, int segundos) {
        if (!puertaAbierta && comida != null && !enCoccion) {
            this.enCoccion = true;
            this.intensidad = intensidad;
            this.segundosTotales = segundos;
        } else {
            System.out.println("No se puede iniciar cocción");
        }
    }
    
    public void finalizarCoccion() {
        if (enCoccion) {
            comida.sumarPuntos(intensidad * segundosTotales);
            enCoccion = false;
        }
    }

    public void abortarCoccion(int segundosFaltantes) {
        if (enCoccion) {
            int tiempoCocinado = segundosTotales - segundosFaltantes;
            comida.sumarPuntos(intensidad * tiempoCocinado);
            enCoccion = false;
            puertaAbierta = true;
        }
    }

    public void mostrarEstado() {
        System.out.println("Puerta abierta: " + puertaAbierta);
        System.out.println("En cocción: " + enCoccion);
        System.out.println("Comida: " + (comida == null ? "Vacío" : comida));
    }

}
