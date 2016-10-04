package algorithms;

import java.awt.Point;

public class ColoredPoint extends Point {

	public Color color;
	
	public ColoredPoint (Point p, Color color) {
		super(p);
		this.color = color;
	}
	
}
