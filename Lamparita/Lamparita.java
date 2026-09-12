public class Lamparita {

    private boolean estado;

    // Constructor
    public Lamparita() {
        estado = false; // inicialmente apagada
    }

    // Método para encender
    public void encender() {
        this.estado = true;
    }

    // Método para apagar
    public void apagar() {
        this.estado = false;
    }

    // Método para consultar el estado
    public boolean estadoLampara() {
        return estado;
    }

    public String toString(){
        String r = ("La lamparita está:");
        return r;
    }
}

//Objeto: Lamparita
//Atributos: Estado
//Métodos: Encender, apagar, estado de lámpara
    
