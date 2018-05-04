
public class cole extends Edificio {
	private int numeroAulas;
	private boolean pabellon;
		public cole(String direccion, String codigoPostal, float altura,
			boolean calefaccionCentral) {
		super(direccion, codigoPostal, altura, calefaccionCentral);
		this.numeroAulas=numerodeAulas;
		
		
		// TODO Auto-generated constructor stub
		}
		public int getCapacidadColeguio(){
			int capacidadColegio;
			capacidadColegio=numeroAulas*30;
			return(capacidadColegio);
			
		}
}
