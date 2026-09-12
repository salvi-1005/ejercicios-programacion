public class Empleado{
    private int num;
    private String nom;
    
    public Empleado(int nu, String no){
          this.num = nu;
          this.nom = no;
        }

    public int getNumero() {
        return this.num;
    }

    public String getNombre(){
        return this.nom;
    }
   
    public void setNumero(int newnum){
        this.num = newnum;
    }

    public void setNombre(String newnom){
        this.nom = newnom;
    }

    public void verDatos(){
        System.out.println("Numero: " + num);
        System.out.println("Nombre: " + nom);
    }
    }
  
    

