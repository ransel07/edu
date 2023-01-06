v1 = 3;
v2 = 5;
quiver(0, 0, v1, v2, 'MaxHeadSize', 0.1)
hold on
a1 = 2 * v1;
a2 = 2 * v2;
quiver(1, 0, a1, a2, 'MaxHeadSize', 0.1, 'Color', 'r')
b1 = -3 * v1;
b2 = -3 * v2;
quiver(2, 0, b1, b2, 'MaxHeadSize', 0.1, 'Color', 'g')
c1 = 7/2 * v1;
c2 = 7/2 * v2;
quiver(3, 0, c1, c2, 'MaxHeadSize', 0.1, 'Color', 'y')
