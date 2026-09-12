public class Main {
    public static void main(String[] args) {

        Comida c = new Comida("torta", 10);
        Microondas m = new Microondas();
        m.insertarComida(c);
        m.retirarComida();
        m.insertarComida(c);
        m.cerrarPuerta();
        m.iniciarCoccion(5, 60);
        m.finalizarCoccion();
        m.iniciarCoccion(6, 120);
        m.abortarCoccion(20);
        m.mostrarEstado();
    } 
}
