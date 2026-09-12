public abstract class VehiculoMotorizado {
    
    protected String fabricante;
    protected String modelo;
    protected int añoDeFabricacion;
    protected double kilometraje;

    public VehiculoMotorizado(String fab, String mod, int año, double kil){
        this.fabricante = fab;
        this.modelo = mod;
        this.añoDeFabricacion = año;
        this.kilometraje = kil;
    }

    public String getFabricante(){
        return fabricante;
    }

    public String getModelo(){
        return modelo;
    }

    public int getAñoDeFabricacion(){
        return añoDeFabricacion;
    }

    public double getKilometraje(){
        return kilometraje;
    }

    public abstract String toString();

}
