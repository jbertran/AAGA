package algorithms;

import java.awt.Point;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class DefaultTeam {
	
	int threshold;
	
	public ArrayList<Point> calculConnectedDominatingSet(ArrayList<Point> points, int edgeThreshold) {
		this.threshold = edgeThreshold;
		
		ArrayList<Point> MIS;
		//MIS = computeMIS(points);
		MIS = computeMISrand(points);
		System.out.println("Size : " + MIS.size()) ;
		
		ArrayList<Point> blue;
		blue = algorithmA(MIS, points);
		//blue = MIS;
		System.out.println("AlgoA : " + blue.size());
		
		ArrayList<Point> OPT;
		//OPT = localSearch(blue, points);
		OPT = blue;

		System.out.println("Final : " + OPT.size());
		return OPT;
	}

	public ArrayList<Point> computeMIS (ArrayList<Point> pts) {
		ArrayList<Point> MIS = new ArrayList<>();
		
		ArrayList<ColoredPoint> points = new ArrayList<>();
		for (Point p : pts) 
			points.add(new ColoredPoint(p, Color.White));
		
		ArrayList<ColoredPoint> stack = new ArrayList<>();
		stack.add(points.get(0));
		
		while (!stack.isEmpty()) {
			ColoredPoint curr = stack.remove(0);
			if (curr.color == Color.Blue)
				continue;
			curr.color = Color.Black;
			MIS.add(curr);
			
			for (ColoredPoint p : points) {
				if (p.distance(curr) <= threshold) {
					p.color = Color.Blue;
				}
			}
			for (ColoredPoint p : points) {
				if (p.distance(curr) <= threshold) {
					for (ColoredPoint q : points) {
						if (q.color == Color.White && q.distance(p) <= threshold &&
								! stack.contains(q)) {
							stack.add(q);
						}
					}
				}
			}
		}
		
		return MIS;
	}
	public ArrayList<Point> computeMISrand (ArrayList<Point> pts) {
		ArrayList<Point> points = new ArrayList<Point>(pts);
		Collections.shuffle(points);
		return computeMIS(points);
	}
	

	public ArrayList<Point> algorithmA (ArrayList<Point> MIS, ArrayList<Point> points) {
		ArrayList<ColoredPoint> UDG  = new ArrayList<>();
		ArrayList<ColoredPoint> grey = new ArrayList<>();
		
		for (Point p : MIS) {
			UDG.add(new ColoredPoint(p, Color.Black));	
		}
		for (Point p : points)
			if (! MIS.contains(p)) {
				ColoredPoint q = new ColoredPoint(p, Color.Grey) ;
				UDG.add(q)                                       ;
				grey.add(q)                                      ;
			}
	
		for (int i = 5; i > 1; i--) {
			out: while (true) {
				ArrayList<ArrayList<ColoredPoint>> blueBlackComponents = getBlueBlackComponents(UDG); 
				System.out.println("size : " + blueBlackComponents.size());
				for (ColoredPoint p : UDG) {
					if (p.color != Color.Grey)
						continue;
					int j = 0;
					for (ArrayList<ColoredPoint> comp : blueBlackComponents) {
						for (ColoredPoint q : comp) {
							if (q.color == Color.Black && q.distance(p) <= threshold) {
								j++;
								break;
							}
						}
					}
					if (j >= i) {
						p.color = Color.Blue;
						blueBlackComponents = getBlueBlackComponents(UDG);
						continue out;
					}
				}
				break;
			}
		}

		ArrayList<Point> res = new ArrayList<>();
		for (ColoredPoint p : UDG)
			if (p.color == Color.Blue || p.color == Color.Black)
				res.add(p);

		return res;
	}
	
	public ArrayList<ArrayList<ColoredPoint>> getBlueBlackComponents (ArrayList<ColoredPoint> pts) {
		ArrayList<ArrayList<ColoredPoint>> res = new ArrayList<>();
		ArrayList<ColoredPoint> points = new ArrayList<>();
		for (ColoredPoint p : pts) {
			if (p.color == Color.Blue || p.color == Color.Black)
				points.add(p);
		}
		
		ArrayList<ColoredPoint> stack = new ArrayList<>();
		
		while (! points.isEmpty() ) {
			ArrayList<ColoredPoint> currentComponent = new ArrayList<ColoredPoint>();
			stack.add(points.remove(0));
			
			while (! stack.isEmpty()) {
				ColoredPoint p = stack.remove(0);
				currentComponent.add(p);
				for (ColoredPoint q : neighbors(points, p)) {
					if (! currentComponent.contains(q) && ! (q.color == Color.Blue && p.color == Color.Blue)) {
						stack.add(q);
						points.remove(q);
					}
				}
			}
			res.add(currentComponent);
		}		
		
		return res;
	}
	
	
	
	public ArrayList<ColoredPoint> neighbors (ArrayList<ColoredPoint> points, ColoredPoint p) {
		ArrayList<ColoredPoint> res = new ArrayList<>();
		
		for (ColoredPoint q : points) 
			if (q.distance(p) <= threshold)
				res.add(q);
		
		return res;
	}
	
	public ArrayList<Point> neighbors (ArrayList<Point> points, Point p) {
		ArrayList<Point> res = new ArrayList<>();
		
		for (Point q : points) 
			if (q.distance(p) <= threshold)
				res.add(q);
		
		return res;
	}
	
	public int arity (ArrayList<Point> points, Point p) {
		int res = 0;
		
		for (Point q : points) 
			if (q.distance(p) <= threshold)
				res++;
		
		return res;
	}
	
	public ArrayList<Point> localSearch (ArrayList<Point> CDSin, ArrayList<Point> points) {
		ArrayList<Point> CDS;
		ArrayList<Point> CDScpy = new ArrayList<>(CDSin);
		
		out: while (true) {
			CDS = new ArrayList<>(CDScpy);
			
			for (Point p : CDS) {
				CDScpy.remove(p);
				if (isValide(CDScpy, points))
					continue out;
				CDScpy.add(p);
			}
			break;
		}
		
		out: while (true) {
			CDS = new ArrayList<>(CDScpy);
			
			System.out.println("Size : " + CDS.size());
			
			for (Point p : CDS) {
				CDScpy.remove(p);
				for (Point q : CDS) {
					if (p.equals(q)) continue;
					if (p.distance(q) > 3 * threshold) continue;
					CDScpy.remove(q);
					for (Point r : points) {
						if (r.equals(p) || r.equals(q)) continue;
						if (r.distance(p) > 3 * threshold || r.distance(q) > 3 * threshold) continue;
						CDScpy.add(r);
						if (isValide(CDScpy, points))
							continue out;
						CDScpy.remove(r);
					}
					CDScpy.add(q);
				}
				CDScpy.add(p);
			}
			break;
		}
		
		return CDS;
	}
	
	public boolean isValide(ArrayList<Point> CDS, ArrayList<Point> points) {
		ArrayList<Point> notCovered = new ArrayList<Point>(points);
		ArrayList<Point> CDScpy     = new ArrayList<Point>(CDS);
		

		for (Point p : CDScpy) {
			for (Point q : neighbors(points,p))
			// for (Point q : neighbors(points, p))
				notCovered.remove(q);
		}
		if (! notCovered.isEmpty())
			return false;
		
		ArrayList<Point> stack = new ArrayList<>();
		stack.add(CDScpy.remove(0));
		while (! stack.isEmpty()) {
			Point p = stack.remove(0);
			for (Point q : neighbors(CDScpy, p)) {
			// for (Point q : neighborsCDS.get(p)) {
				CDScpy.remove(q);
				if (! stack.contains(q))
					stack.add(q);
			}
		}
		
		return CDScpy.isEmpty();
	}
	

}