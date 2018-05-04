
public class Segmento {
	private punto p1;
	private punto p2;
	public Segmento(punto p1, punto p2) {
		this.p1 = p1;
		this.p2 = p2;
	}
	public punto getP1() {
		return p1;
	}
	public void setP1(punto p1) {
		this.p1 = p1;
	}
	public punto getP2() {
		return p2;
	}
	public void setP2(punto p2) {
		this.p2 = p2;
	}
	public float getDistance(){
		float distance;
		float c1,c2;
		c1=p2.getX()-p1.getX();
		c2=p1.getX()-p2.getX();
		distance=math. c1^2+c2^2;
				
		return distance; 
	}
}
