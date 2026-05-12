public class Entity3 extends Entity {
    private int[] directCost;

    // Perform any necessary initialization in the constructor
    public Entity3() {
        directCost = new int[NetworkSimulator.NUMENTITIES];
        directCost[0] = 0;
        directCost[1] = 1;
        directCost[2] = 3;
        directCost[3] = 7;

        for (int i = 0; i < NetworkSimulator.NUMENTITIES; i++)
            for (int j = 0; j < NetworkSimulator.NUMENTITIES; j++)
                distanceTable[i][j] = 999;

        for (int n = 0; n < NetworkSimulator.NUMENTITIES; n++)
            if (n != 0 && directCost[n] < 999)
                distanceTable[n][n] = directCost[n];

        int[] mincost = new int[NetworkSimulator.NUMENTITIES];
        for (int i = 0; i < NetworkSimulator.NUMENTITIES; i++) {
            int min = 999;
            for (int j = 0; j < NetworkSimulator.NUMENTITIES; j++)
                if (distanceTable[i][j] < min)
                    min = distanceTable[i][j];
            mincost[i] = min;
        }
        mincost[0] = 0;

        for (int n = 1; n < NetworkSimulator.NUMENTITIES; n++)
            if (directCost[n] < 999) {
                NetworkSimulator.toLayer2(new Packet(0, n, mincost));
                System.out.println("Time " + NetworkSimulator.getClocktime() +
                        ": Node 0 sends initial packet to " + n);
            }
        System.out.println("Node 0 initialized.");
        printDT();
    }

    // Handle updates when a packet is received. Students will need to call
    // NetworkSimulator.toLayer2() with new packets based upon what they
    // send to update. Be careful to construct the source and destination of
    // the packet correctly. Read the warning in NetworkSimulator.java for more
    // details.
    public void update(Packet p) {
        int src = p.getSource();
        System.out.print("Time " + NetworkSimulator.getClocktime() +
                ": Node 0 receives packet from " + src + " with costs: [");
        for (int i = 0; i < NetworkSimulator.NUMENTITIES; i++) {
            System.out.print(p.getMincost(i));
            if (i < NetworkSimulator.NUMENTITIES - 1)
                System.out.print(", ");
        }
        System.out.println("]");

        int[] oldMin = new int[NetworkSimulator.NUMENTITIES];
        for (int i = 0; i < NetworkSimulator.NUMENTITIES; i++) {
            int min = 999;
            for (int j = 0; j < NetworkSimulator.NUMENTITIES; j++)
                if (distanceTable[i][j] < min)
                    min = distanceTable[i][j];
            oldMin[i] = min;
        }

        for (int i = 0; i < NetworkSimulator.NUMENTITIES; i++) {
            int newCost = directCost[src] + p.getMincost(i);
            if (newCost < 0 || newCost > 999)
                newCost = 999;
            if (newCost < distanceTable[i][src])
                distanceTable[i][src] = newCost;
        }

        int[] newMin = new int[NetworkSimulator.NUMENTITIES];
        for (int i = 0; i < NetworkSimulator.NUMENTITIES; i++) {
            int min = 999;
            for (int j = 0; j < NetworkSimulator.NUMENTITIES; j++)
                if (distanceTable[i][j] < min)
                    min = distanceTable[i][j];
            newMin[i] = min;
        }
        newMin[0] = 0;

        boolean changed = false;
        for (int i = 0; i < NetworkSimulator.NUMENTITIES; i++)
            if (newMin[i] != oldMin[i]) {
                changed = true;
                break;
            }

        if (changed) {
            System.out.println("Time " + NetworkSimulator.getClocktime() +
                    ": Node 0 distance table updated.");
            for (int n = 1; n < NetworkSimulator.NUMENTITIES; n++)
                if (directCost[n] < 999) {
                    NetworkSimulator.toLayer2(new Packet(0, n, newMin));
                    System.out.println("Time " + NetworkSimulator.getClocktime() +
                            ": Node 0 sends update to " + n);
                }
        } else {
            System.out.println("Time " + NetworkSimulator.getClocktime() +
                    ": Node 0 no change, no update sent.");
        }
        printDT();
    }

    public void linkCostChangeHandler(int whichLink, int newCost) {
        System.out.println("Node 0: link cost to " + whichLink +
                " changed to " + newCost + " (ignored in basic assignment)");
    }

    public void printDT() {
        System.out.println();
        System.out.println("           via");
        System.out.println(" D0 |   1   2   3");
        System.out.println("----+------------");
        for (int i = 1; i < NetworkSimulator.NUMENTITIES; i++) {
            System.out.print("   " + i + "|");
            for (int j = 1; j < NetworkSimulator.NUMENTITIES; j++) {
                if (distanceTable[i][j] < 10) {
                    System.out.print("   ");
                } else if (distanceTable[i][j] < 100) {
                    System.out.print("  ");
                } else {
                    System.out.print(" ");
                }

                System.out.print(distanceTable[i][j]);
            }
            System.out.println();
        }
    }
}