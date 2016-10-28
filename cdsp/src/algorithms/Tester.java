package algorithms;

import java.awt.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

public class Tester {

    final int SAMPLESIZE = 50;

    int cloudSize;
    int xrange;
    int yrange;
    int threshold;

    DefaultTeam solver;

    Random generator = new Random();

    public Tester (int cloudSize, int xyrange, int threshold) {
        this.cloudSize = cloudSize;
        this.xrange = xyrange;
        this.yrange = xyrange;
        this.threshold = threshold;
        this.solver = new DefaultTeam(threshold);
    }

    ArrayList<Point> generateCloud() {
        generator.setSeed(System.currentTimeMillis());
        ArrayList<Point> res = new ArrayList<>();
        for (int i=0; i<cloudSize; i++)
            res.add(new Point(generator.nextInt(xrange), generator.nextInt(yrange)));
        return res;
    }

    HashMap<String, Long> instanceData (ArrayList<Point> points) {
        HashMap<String, Long> res = new HashMap<>();

        long before = System.currentTimeMillis();
        ArrayList<Point> CDS = solver.calculConnectedDominatingSet(points, this.threshold);
        long after = System.currentTimeMillis();
        long time = after - before;

        res.put("time", time);
        res.put("nodecount", new Long(CDS.size()));

        return res;
    }

    public HashMap<String, Float> runInstances (int instanceCount) {

        ArrayList<Point> points = generateCloud();

        float time = 0;
        float nodeCount = 0;
        for (int i=0; i<instanceCount; i++) {
            HashMap<String, Long> data = instanceData(points);
            time += data.get("time");
            nodeCount += data.get("nodecount");
            System.out.println(String.valueOf(time) +
                    " " + String.valueOf(data.get("time")) +
                    " " + String.valueOf(data.get("nodecount")));
        }

        HashMap<String, Float> res = new HashMap<>();
        res.put("timeav", time/instanceCount);
        res.put("nodecountav", nodeCount/instanceCount);

        return res;
    }
}