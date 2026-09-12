import java.time.LocalDate;

public class Main {

    public static void main(String[] args){

        Torneo torneo = new Torneo();

        Equipo Team_A = torneo.cargarEquipo("Team A", 100);
        Equipo Team_B = torneo.cargarEquipo("Team B", 200);
        Equipo Team_C = torneo.cargarEquipo("Team C", 300);
        Equipo Team_D = torneo.cargarEquipo("Team D", 400);
        Equipo Team_E = torneo.cargarEquipo("Team E", 500);
        Equipo Team_F = torneo.cargarEquipo("Team F", 600);
        Equipo Team_G = torneo.cargarEquipo("Team G", 700);
        Equipo Team_H = torneo.cargarEquipo("Team H", 800);
        
        //Fecha 1: 4 de noviembre:
        torneo.cargarPartido(Team_A, Team_B, LocalDate.of(2023, 11, 4), 2, 0);
        torneo.cargarPartido(Team_C, Team_D, LocalDate.of(2023, 11, 4), 2, 1);
        torneo.cargarPartido(Team_E, Team_F, LocalDate.of(2023, 11, 4), 2, 2);
        torneo.cargarPartido(Team_G, Team_H, LocalDate.of(2023, 11, 4), 2, 3);

        //Fecha 2: 12 de noviembre: 
        torneo.cargarPartido(Team_B, Team_A, LocalDate.of(2023, 11, 12), 1, 1);
        torneo.cargarPartido(Team_C, Team_D, LocalDate.of(2023, 11, 12), 3, 0);
        torneo.cargarPartido(Team_F, Team_E, LocalDate.of(2023, 11, 12), 1, 2);
        torneo.cargarPartido(Team_H, Team_G, LocalDate.of(2023, 11, 12), 0, 0);
        

        //Resultados de partidos 12 de noviembre
        torneo.mostrarPartidosFecha(LocalDate.of(2023, 11, 12));

        //Tabla de posiciones:
        torneo.mostrarTabla();

        torneo.mostrarEquipoMasGoleador();

    }
    
}
