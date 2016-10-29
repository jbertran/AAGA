package algorithms;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;

public class Main {

    static final int SAMPLESIZE = 500;

    public static void density() {
        // Work out threshold from density for 1k nodes
        // baseline 55 for 1k nodes in 800 xyrange
        int size = 1000;
        int xyrange = 800;

        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
                new FileOutputStream("data/density.dat"), "utf-8"))) {
            writer.write("cloudsize timeav nodecountav\n");
            for (float d=1; d<2; d+=0.1) {
                int thresh = 0; //??
                Tester t = new Tester(size, xyrange, thresh);
                HashMap<String, Float> data = t.runInstances(SAMPLESIZE);
                String toprint = String.valueOf(size) + " " +
                        data.get("timeav") + " " +
                        data.get("nodecountav") + "\n";
                System.out.println(toprint);
                writer.write(toprint);
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void size() {
        // Threshold updates for correct connexity
        // xyrange updates for correct density
        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
                new FileOutputStream("data/size.dat"), "utf-8"))) {
            writer.write("cloudsize timeav nodecountav\n");
            for (int size=1000; size<4500; size+=500) {
                int thresh = 0; //??
                int xyrange = 0; //??
                Tester t = new Tester(size, xyrange, thresh);
                HashMap<String, Float> data = t.runInstances(SAMPLESIZE);
                String toprint = String.valueOf(size) + " " +
                        data.get("timeav") + " " +
                        data.get("nodecountav") + "\n";
                System.out.println(toprint);
                writer.write(toprint);
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void connex() {
        int size = 1000;
        int xyrange = 800;

        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
                new FileOutputStream("data/connex.dat"), "utf-8"))) {
            writer.write("cloudsize timeav nodecountav\n");
            for (int th=0; th<65; th++) {
                Tester t = new Tester(size, xyrange, th);
                HashMap<String, Float> data = t.runInstances(SAMPLESIZE);
                String toprint = String.valueOf(th) + " " +
                        data.get("timeav") + " " +
                        data.get("nodecountav") + "\n";
                System.out.println(toprint);
                writer.write(toprint);
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String [] args) {
        boolean density = false;
        boolean connex= true;
        boolean size = false;

        System.out.println("Density:");
        if (density)
            density();
        else
            System.out.println("Skipped");
        System.out.println("Thresholds:");
        if (connex)
            connex();
        else
            System.out.println("Skipped");
    }
}
