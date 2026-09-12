import java.util.ArrayList;
import java.util.Comparator;
import java.time.LocalDate;

public class Torneo {

    private ArrayList<Equipo> equipos;
    private ArrayList<Partido> partidos;

    public Torneo() {
        this.equipos = new ArrayList<>();
        this.partidos = new ArrayList<>();
    }

    public ArrayList<Equipo> getEquipos() {
        return equipos;
    }

    public ArrayList<Partido> getPartidos() {
        return partidos;
    }

    public Equipo cargarEquipo(String nombre, int cantidadFans) {
        Equipo equipo = new Equipo(nombre, cantidadFans);
        equipos.add(equipo);
        return equipo;
    }

    public void cargarPartido(Equipo equipoLocal, Equipo equipoVisitante, LocalDate fecha, int golesLocal, int golesVisitante) {
        if (!equipos.contains(equipoLocal) || !equipos.contains(equipoVisitante)){
            System.out.println("El equipo no está cargado en el torneo."); 
            return; 
        }
        Partido partido = new Partido(equipoLocal, equipoVisitante, fecha, golesLocal, golesVisitante);
        partidos.add(partido);
        //Gana el equipo local:
        if (golesLocal > golesVisitante) {
            equipoLocal.setPuntos(equipoLocal.getPuntos() + 3);
            equipoLocal.setPartidosGanados(equipoLocal.getPartidosGanados() + 1);
            equipoLocal.setGolesAFavor(equipoLocal.getGolesAFavor() + golesLocal);
            equipoLocal.setGolesEnContra(equipoLocal.getGolesEnContra() + golesVisitante);
            equipoLocal.setDiferenciaDeGol(equipoLocal.getDiferenciaDeGol() + (golesLocal - golesVisitante));
            equipoLocal.setPartidosJugados(equipoLocal.getPartidosJugados() + 1);
            
            equipoVisitante.setPartidosPerdidos(equipoVisitante.getPartidosPerdidos() + 1);
            equipoVisitante.setGolesAFavor(equipoVisitante.getGolesAFavor() + golesVisitante);
            equipoVisitante.setGolesEnContra(equipoVisitante.getGolesEnContra() + golesLocal);
            equipoVisitante.setDiferenciaDeGol(equipoVisitante.getDiferenciaDeGol() + (golesVisitante - golesLocal));
            equipoVisitante.setPartidosJugados(equipoVisitante.getPartidosJugados() + 1);

        //Gana el equipo visitante:
        } else if (golesVisitante > golesLocal) {
            equipoVisitante.setPuntos(equipoVisitante.getPuntos() + 3);
            equipoVisitante.setPartidosGanados(equipoVisitante.getPartidosGanados() + 1);
            equipoVisitante.setGolesAFavor(equipoVisitante.getGolesAFavor() + golesVisitante);
            equipoVisitante.setGolesEnContra(equipoVisitante.getGolesEnContra() + golesLocal);
            equipoVisitante.setDiferenciaDeGol(equipoVisitante.getDiferenciaDeGol() + (golesVisitante - golesLocal));
            equipoVisitante.setPartidosJugados(equipoVisitante.getPartidosJugados() + 1);
            
            equipoLocal.setPartidosPerdidos(equipoLocal.getPartidosPerdidos() + 1);
            equipoLocal.setGolesAFavor(equipoLocal.getGolesAFavor() + golesLocal);
            equipoLocal.setGolesEnContra(equipoLocal.getGolesEnContra() + golesVisitante);
            equipoLocal.setDiferenciaDeGol(equipoLocal.getDiferenciaDeGol() + (golesLocal - golesVisitante));
            equipoLocal.setPartidosJugados(equipoLocal.getPartidosJugados() + 1); 
        
        //empate: 
        } else {
            equipoLocal.setPuntos(equipoLocal.getPuntos() + 1);
            equipoLocal.setPartidosEmpatados(equipoLocal.getPartidosEmpatados() + 1);
            equipoLocal.setPartidosJugados(equipoLocal.getPartidosJugados() + 1);
            equipoLocal.setGolesAFavor(equipoLocal.getGolesAFavor() + golesLocal);
            equipoLocal.setGolesEnContra(equipoLocal.getGolesEnContra() + golesVisitante);
            
            equipoVisitante.setPuntos(equipoVisitante.getPuntos() + 1);
            equipoVisitante.setPartidosEmpatados(equipoVisitante.getPartidosEmpatados() + 1);
            equipoVisitante.setPartidosJugados(equipoVisitante.getPartidosJugados() + 1);
            equipoVisitante.setGolesAFavor(equipoVisitante.getGolesAFavor() + golesVisitante);
            equipoVisitante.setGolesEnContra(equipoVisitante.getGolesEnContra() + golesLocal);
        }
    }

    public void mostrarPartidosFecha(LocalDate fecha) {
        for (Partido partido : partidos) {
            if (partido.getFecha().equals(fecha)) {
                System.out.println(partido.resultado());
            }
        }
    }

    public void mostrarTabla() {
        System.out.println("Equipo | Ju | Pu | Ga | Em | Pe | GF | GC | DG");
        //Ordeno los equipos por puntos, y si hay empate, desempata la diferencia de gol:
        equipos.sort(Comparator.comparingInt(Equipo::getPuntos).reversed().thenComparing(Comparator.comparingInt(Equipo::getDiferenciaDeGol).reversed()));
        for (Equipo equipo : equipos) {
            System.out.println(equipo.toString());
        }
    }

    public void mostrarEquipoMasGoleador(){
        System.out.println("El equipo mas goleador: ");
        Equipo equipoMasGoleador = null;
        for (Equipo equipo : equipos){
            if (equipoMasGoleador == null || equipo.getGolesAFavor() > equipoMasGoleador.getGolesAFavor()){
                equipoMasGoleador = equipo;
            }
        }
        if (equipoMasGoleador != null){
            System.out.println(equipoMasGoleador.toString());
        } else{
            System.out.println("No hay equipos registrados en el torneo");
        }

    }
    
    
}
