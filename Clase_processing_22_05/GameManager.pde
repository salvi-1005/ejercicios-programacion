class GameManager{
  
  ArrayList<Martian> marcianos;
  
  GameManager()
  {
    marcianos = new ArrayList<Martian>(); 
    inicializarFormacion();
  } 
  
  public void inicializarFormacion()
  {
    for(int i = 1; i < 6; i++)
  {
    marcianos.add(new RedMartian(i*60, 100));
  }
  for(int i = 1; i < 6; i++)
  {
    marcianos.add(new GreenMartian(i*60, 150));
  }
  }
  
  public void actualizar()
  {
  
  }
  
  public void dibujar()
  {
    for (Martian et: marcianos)
  {
    et.actualizarMarcianos();
    et.dibujarMarcianos();
  }
  
  for (Martian et: marcianos)
  {
    et.actualizarMarcianos();
    et.dibujarMarcianos();
  }
  
  }
}
