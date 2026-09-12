public class Trayecto {

    private int distancia;
    private int cantEstaciones;

    public Trayecto(int distancia, int cantEstaciones){
        this.distancia = distancia;
        this.cantEstaciones = cantEstaciones;
    }

    public int getDistancia(){
        return distancia;
    }

    public int getCantEstaciones(){
        return cantEstaciones;
    }
}
