package algorithms;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;

public class Main {

    static final int SAMPLESIZE = 500;

    public static void density() {
        int [] sizes = {1000, 1500, 2000, 2500, 3000};

        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
                new FileOutputStream("data/density.dat"), "utf-8"))) {
            writer.write("cloudsize timeav nodecountav\n");
            for (int size : sizes) {
                Tester t = new Tester(size, 800, 55);
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
        int [] sizes = {1000, 1500, 2000, 2500, 3000};

        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
                new FileOutputStream("data/size.dat"), "utf-8"))) {
            writer.write("cloudsize timeav nodecountav\n");
            for (int size : sizes) {
                Tester t = new Tester(size, 800, 55);
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
        ArrayList<Integer> thresholds = new ArrayList<>();
        for (int i=10; i<65; i++)
            thresholds.add(i);

        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
                new FileOutputStream("data/connex.dat"), "utf-8"))) {
            writer.write("cloudsize timeav nodecountav\n");
            for (int th : thresholds) {
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
