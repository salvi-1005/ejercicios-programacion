import java.time.LocalDate;

public class Partido {

    private LocalDate fecha;
    private Equipo equipoLocal;
    private Equipo equipoVisitante;
    private int golesLocal;
    private int golesVisitante;

    public Partido(Equipo equipoLocal, Equipo equipoVisitante, LocalDate fecha, int golesLocal, int golesVisitante) {
        this.equipoLocal = equipoLocal;
        this.equipoVisitante = equipoVisitante;
        this.fecha = fecha;
        this.golesLocal = golesLocal;
        this.golesVisitante = golesVisitante;
    }

    public LocalDate getFecha() {
        return fecha;
    }

    public void setFecha(LocalDate fec){
        this.fecha = fec;
    }

    public Equipo getEquipoLocal() {
        return equipoLocal;
    }

    public void setEquipoLocal(Equipo loc){
        this.equipoLocal = loc;
    }

    public Equipo getEquipoVisitante() {
        return equipoVisitante;
    }

    public void setEquipoVisitante(Equipo vis){
        this.equipoVisitante = vis;
    }

    public int getGolesLocal() {
        return golesLocal;
    }

    public int getGolesVisitante() {
        return golesVisitante;
    }

    public void setGolesLocal(int golesLocal) {
        this.golesLocal = golesLocal;
    }

    public void setGolesVisitante(int golesVisitante) {
        this.golesVisitante = golesVisitante;
    }


    public String resultado() {
        return "Fecha: " + fecha + ", " + equipoLocal.getNombre() + " (" + golesLocal + ") "  + "- " + equipoVisitante.getNombre() + " (" + golesVisitante + ")" ;
    }

}