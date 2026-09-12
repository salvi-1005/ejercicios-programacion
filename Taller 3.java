public class Main {
   
    1)
    public class Fecha {
        private int dia;
        private int mes;
        
        public Fecha(int dia, int mes) {
            this.dia = dia;
            this.mes = mes;
        }
        
        public int dia() {
            return this.dia;
        }
        
        public int mes() {
            return this.mes;
        }
        
        public static void main(String[] args) {
            Fecha miFecha = new Fecha(15, 4);
            System.out.println("Día: " + miFecha.dia());  // Salida: 15
            System.out.println("Mes: " + miFecha.mes());  // Salida: 4
        }
    }

    2)
    public class Fecha {
        private int dia;
        private int mes;
        
        public Fecha(int dia, int mes) {
            this.dia = dia;
            this.mes = mes;
        }
        
        public int dia() {
            return this.dia;
        }
        
        public int mes() {
            return this.mes;
        }
        
        @Override
        public String toString() {
            return this.dia + "/" + this.mes;
        }
        
        public static void main(String[] args) {
            Fecha miFecha = new Fecha(15, 4);
            System.out.println(miFecha.toString());  // Salida: 15/4
        }
    }

    3)
    public class Fecha {
        private int dia;
        private int mes;
        
        public Fecha(int dia, int mes) {
            this.dia = dia;
            this.mes = mes;
        }
        
        public int dia() {
            return this.dia;
        }
        
        public int mes() {
            return this.mes;
        }
        
        public void incrementarDia() {
            // Verificar si es el último día del mes
            int ultimoDiaMes;
            switch (this.mes) {
                case 4: case 6: case 9: case 11:
                    ultimoDiaMes = 30;
                    break;
                case 2:
                    // Ignorando años bisiestos
                    ultimoDiaMes = 28;
                    break;
                default:
                    ultimoDiaMes = 31;
                    break;
            }
            
            // Incrementar el día
            this.dia++;
            
            // Verificar si se debe cambiar de mes
            if (this.dia > ultimoDiaMes) {
                this.dia = 1; // Volver al primer día del mes
                this.mes++;   // Incrementar el mes
            }
        }
        
        @Override
        public String toString() {
            return this.dia + "/" + this.mes;
        }
        
        public static void main(String[] args) {
            Fecha miFecha = new Fecha(31, 12);
            System.out.println(miFecha.toString());  // Salida: 31/12
            
            miFecha.incrementarDia();
            System.out.println(miFecha.toString());  // Salida: 1/1
        }
    }

    4)
    public class Fecha {
        private int dia;
        private int mes;
        
        public Fecha(int dia, int mes) {
            this.dia = dia;
            this.mes = mes;
        }
        
        public int dia() {
            return this.dia;
        }
        
        public int mes() {
            return this.mes;
        }
        @Override
        public String toString() {
            return this.dia + "/" + this.mes;
        }
        
        @Override
        public boolean equals(Object obj) {
            if (obj instanceof Fecha) {
                Fecha otraFecha = (Fecha) obj;
                return this.dia == otraFecha.dia && this.mes == otraFecha.mes;
            }
            return false;

    5)
    public class Horario {
        private int hora;
        private int minutos;
        
        public Horario(int hora, int minutos) {
            this.hora = hora;
            this.minutos = minutos;
        }
        
        public int hora() {
            return this.hora;
        }
        
        public int minutos() {
            return this.minutos;
        }
    6)
    public class Horario {
        private int hora;
        private int minutos;
        
        public Horario(int hora, int minutos) {
            this.hora = hora;
            this.minutos = minutos;
        }
        
        public int hora() {
            return this.hora;
        }
        
        public int minutos() {
            return this.minutos;
        }
        
    @Override
    public String toString() {
        return String.format("%02d:%02d", this.hora, this.minutos);
    }

    7)
    public class Horario {
        private int hora;
        private int minutos;
        
        public Horario(int hora, int minutos) {
            this.hora = hora;
            this.minutos = minutos;
        }
        
        public int hora() {
            return this.hora;
        }
        
        public int minutos() {
            return this.minutos;
        }
        
        @Override
        public boolean equals(Object obj) {
            if (this == obj) {
                return true;
            }
            if (obj == null || getClass() != obj.getClass()) {
                return false;
            }
            Horario other = (Horario) obj;
            return hora == other.hora && minutos == other.minutos;

    8)
    public class Recordatorio {
        private String mensaje;
        private Fecha fecha;
        private Horario horario;
        
        public Recordatorio(String mensaje, Fecha fecha, Horario horario) {
            this.mensaje = mensaje;
            this.fecha = new Fecha(fecha.dia(), fecha.mes()); // Se crea una nueva instancia de Fecha para evitar aliasing
            this.horario = new Horario(horario.hora(), horario.minutos()); // Se crea una nueva instancia de Horario para evitar aliasing
        }
        
        public Fecha fecha() {
            return new Fecha(fecha.dia(), fecha.mes()); // Se devuelve una nueva instancia de Fecha para evitar aliasing
        }
        
        public Horario horario() {
            return new Horario(horario.hora(), horario.minutos()); // Se devuelve una nueva instancia de Horario para evitar aliasing
        }
        
        public String mensaje() {
            return mensaje;
        }

    9)
        @Override
    public String toString() {
        return mensaje + " @ " + fecha + " " + horario;
    }

    10)
        @Override
    public boolean equals(Object obj) {
        // Comprobar si el objeto recibido es una instancia de Recordatorio
        if (obj instanceof Recordatorio) {
            // Convertir el objeto a un Recordatorio
            Recordatorio otro = (Recordatorio) obj;
            // Comprobar si los atributos son iguales
            return this.mensaje.equals(otro.mensaje) && this.fecha.equals(otro.fecha) && this.horario.equals(otro.horario);
        }
        // Si el objeto no es un Recordatorio, devolver falso
        return false;
    }

    11)
    public class ArregloRedimensionableDeRecordatorios {
        private Recordatorio[] elementos;
        private int longitud;
        
        public ArregloRedimensionableDeRecordatorios() {
            this.elementos = new Recordatorio[10]; // Tamaño inicial del arreglo
            this.longitud = 0;
        }
        
        public int longitud() {
            return this.longitud;
        }
        public Recordatorio obtener(int i) {
            // Verificar si la posición es válida
            if (i < 0 || i >= this.longitud) {
                throw new IndexOutOfBoundsException("Índice fuera de rango");
            }
            return this.elementos[i];
        }

    12)
    public class ArregloRedimensionableDeRecordatorios {
        private Recordatorio[] elementos;
        private int longitud;
        
        public ArregloRedimensionableDeRecordatorios() {
            this.elementos = new Recordatorio[10]; // Tamaño inicial del arreglo
            this.longitud = 0;
        }
        
        public int longitud() {
            return this.longitud;
        }
        public Recordatorio obtener(int i) {
            // Verificar si la posición es válida
            if (i < 0 || i >= this.longitud) {
                throw new IndexOutOfBoundsException("Índice fuera de rango");
            }
            return this.elementos[i];
        }
    13)
    public class ArregloRedimensionableDeRecordatorios {
        private Recordatorio[] elementos;
        private int longitud;
        
        public ArregloRedimensionableDeRecordatorios() {
            this.elementos = new Recordatorio[10]; // Tamaño inicial del arreglo
            this.longitud = 0;
        }
        
        public int longitud() {
            return this.longitud;
        }

        public Recordatorio obtener(int i) {
            // Verificar si la posición es válida
            if (i < 0 || i >= this.longitud) {
                throw new IndexOutOfBoundsException("Índice fuera de rango");
            }
            return this.elementos[i];
        }

    14)
    public class ArregloRedimensionableDeRecordatorios {
        private Recordatorio[] elementos;
        private int longitud;
        
        // Otros métodos de la clase
        
        public ArregloRedimensionableDeRecordatorios copiar() {
            // Crear un nuevo arreglo con la misma longitud que el original
            ArregloRedimensionableDeRecordatorios copia = new ArregloRedimensionableDeRecordatorios();
            copia.elementos = new Recordatorio[this.longitud];
            copia.longitud = this.longitud;
            // Copiar los elementos al nuevo arreglo
            for (int i = 0; i < this.longitud; i++) {
                copia.elementos[i] = this.elementos[i];
            }
            return copia;
        }
    }

    15)
    public class ArregloRedimensionableDeRecordatorios {
        private Recordatorio[] elementos;
        private int longitud;
        
        // Constructor por copia
        public ArregloRedimensionableDeRecordatorios(ArregloRedimensionableDeRecordatorios otro) {
            // Crear un nuevo arreglo con la misma longitud que el arreglo original
            this.elementos = new Recordatorio[otro.longitud];
            this.longitud = otro.longitud;
            // Copiar los elementos del arreglo original al nuevo arreglo
            for (int i = 0; i < otro.longitud; i++) {
                this.elementos[i] = new Recordatorio(otro.elementos[i]);
            }
        }
    }

    16)
    public class Agenda {
        private Fecha fechaActual;
    
        // Constructor Agenda
        public Agenda(Fecha fecha) {
            this.fechaActual = new Fecha(fecha); // Crear una nueva instancia de Fecha para evitar aliasing
        }
    
        // Método fechaActual
        public Fecha fechaActual() {
            return new Fecha(this.fechaActual); // Devolver una nueva instancia de Fecha para evitar aliasing
        }
    }

    17)
    import java.util.ArrayList;

    public class Agenda {
        private Fecha fechaActual;
        private ArrayList```

    18)
    public class Agenda {
        private Fecha fechaActual;
        private ArrayList```
        




    
}
