package algorithms;

import java.awt.Point;
import java.util.ArrayList;

public class DefaultTeam {

  public ArrayList<Point> calculFVS(ArrayList<Point> points, int edgeThreshold) {
    ArrayList<Point> fvs = new ArrayList<Point>();

    for(int i=0;i<5*points.size()/6;i++){
      fvs.add(points.get(i));
    }

    return fvs;
  }
}
