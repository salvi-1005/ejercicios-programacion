public class Equipo {

    private String nombre;
    private int fans;
    private int partidosJugados;
    private int puntos;
    private int partidosGanados;
    private int partidosEmpatados;
    private int partidosPerdidos;
    private int golesAFavor;
    private int golesEnContra;
    private int diferenciaDeGol;

    public Equipo(String nombre, int fans) {
        this.nombre = nombre;
        this.fans = fans;
        this.partidosJugados = 0;
        this.puntos = 0;
        this.partidosGanados = 0;
        this.partidosEmpatados = 0;
        this.partidosPerdidos = 0;
        this.golesAFavor = 0;
        this.golesEnContra = 0;
        this.diferenciaDeGol = 0;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nom){
        this.nombre = nom;
    }

    public int getFans() {
        return fans;
    }

    public void setFans(int cantFans){
        this.fans = cantFans;
    }

    public int getPuntos() {
        return puntos;
    }

    public void setPuntos(int puntos) {
        this.puntos = puntos;
    }

    public int getPartidosJugados() {
        return partidosJugados;
    }

    public void setPartidosJugados(int partidosJugados) {
        this.partidosJugados = partidosJugados;
    }

    public int getPartidosGanados() {
        return partidosGanados;
    }

    public void setPartidosGanados(int partidosGanados) {
        this.partidosGanados = partidosGanados;
    }

    public int getPartidosEmpatados() {
        return partidosEmpatados;
    }

    public void setPartidosEmpatados(int partidosEmpatados) {
        this.partidosEmpatados = partidosEmpatados;
    }

    public int getPartidosPerdidos() {
        return partidosPerdidos;
    }

    public void setPartidosPerdidos(int partidosPerdidos) {
        this.partidosPerdidos = partidosPerdidos;
    }

    public int getGolesAFavor() {
        return golesAFavor;
    }

    public void setGolesAFavor(int golesAFavor) {
        this.golesAFavor = golesAFavor;
    }

    public int getGolesEnContra() {
        return golesEnContra;
    }

    public void setGolesEnContra(int golesEnContra) {
        this.golesEnContra = golesEnContra;
    }

    public int getDiferenciaDeGol() {
        return diferenciaDeGol;
    }

    public void setDiferenciaDeGol(int diferenciaDeGol) {
        this.diferenciaDeGol = diferenciaDeGol;
    }

    public String toString() {
        return nombre + " | " + partidosJugados + "  | " + puntos 
                + "  | " + partidosGanados + "  | " + partidosEmpatados 
                + "  | " + partidosPerdidos + "  | " + golesAFavor 
                + "  | " + golesEnContra + "  | " + diferenciaDeGol;
    }

}
