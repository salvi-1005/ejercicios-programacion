public class Multiplos {
    
    private int x;
    private int y;

    public Multiplos(int x, int y){
        this.x = x;
        this.y = y;
    }

    public int[] DevolverMultiplos(){
        int[] datos = new int[this.y];
        for (int i = 0; i < this.y; i++) {
            datos[i] = this.x * (i + 1);
        }
        return datos;
    }

}
