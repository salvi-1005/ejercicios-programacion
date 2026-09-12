import java.util.ArrayList;

public class Alumno {

    private String nombre;
    private String apellido;
    private int LU;
    private ArrayList<Double> notas;

    public Alumno(String nombre, String apellido, int LU, ArrayList<Double> notas){
        this.nombre = nombre;
        this.apellido = apellido;
        this.LU = LU;
        this.notas = notas;
    }

    public String getNombre(){
        return this.nombre;
    }

    public void setNombre(String nuevoNombre){
        this.nombre = nuevoNombre;
    }

    public String getApellido(){
        return this.apellido;
    }

    public void setApellido(String nuevoApellido){
        this.apellido = nuevoApellido;
    }

    public int getLU(){
        return this.LU;
    }

    public void setLU(int nuevoLU){
        this.LU = nuevoLU;
    }

    public ArrayList<Double> getNotas(){
        return this.notas;
    }

    public double promedio(){
        double sumaNotas = 0;
        for (double nota: notas){
            sumaNotas += nota;
        }
        double promedioNotas = sumaNotas/notas.size();
        return promedioNotas;
    }

    public String toString(){
        return (nombre + " " + apellido + " " + LU);
    }
    
}
