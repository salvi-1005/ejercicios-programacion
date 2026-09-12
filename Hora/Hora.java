public class Hora{

    private int hora;
    private int minutos;
    private int segundos;
    
    public Hora(){
        hora = 0;
        minutos = 0;
        segundos = 0;
    }

    public Hora(int h, int m, int s){
        hora = h;
        minutos = m;
        segundos = s;

    }

    public void mostrar(){
        System.out.printf("%02d:%02d:%02d\n", hora, minutos, segundos);
    }

    public Hora suma(Hora h){
        int ho = this.hora + h.hora;
        int m = this.minutos + h.minutos;
        int s = this.segundos + h.segundos;

        if (s >= 60){
            s -= 60;
            m += 1;
        }

        if (m >= 60) {
            m -= 60;
            ho += 1;
        }

        if (ho >= 24) {
            ho -= 24;
        }

        return new Hora(ho,m,s);
    }

    public void suma2(Hora h){
        this.hora = this.hora + h.hora;
        this.minutos = this.minutos + h.minutos;
        this.segundos = this.segundos + h.segundos;

        if (this.segundos >= 60){
            this.segundos -= 60;
            this.minutos += 1;
        }

        if (this.minutos >= 60) {
            this.minutos -= 60;
            this.hora += 1;
        }

        if (this.hora >= 24) {
            this.hora -= 24;
        }
    }
}

