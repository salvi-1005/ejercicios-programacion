public class Main {
    public static void main(String[] args) {
        Lamparita l = new Lamparita();

        System.out.println("Estado inicial: " + l.estadoLampara());
        l.encender();
        System.out.println("Después de encender: " + l.estadoLampara());
        l.apagar();
        System.out.println("Después de apagar: " + l.estadoLampara());
    }
}

//Encapsulamiento
//This: Llama al método de la clase

