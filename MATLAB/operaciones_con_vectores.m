v1 = 3;
v2 = 5;
u1 = -5;
u2 = 3;

quiver(0, 0, v1, v2, 'MaxHeadSize', 0.1)
quiver(-2, 0, u1, u2, 'MaxHeadSize', 0.1, 'Color', 'r')
hold on
a1 = 2 * v1;
a2 = 2 * v2;  
%quiver(1, 0, a1, a2, 'MaxHeadSize', 0.1, 'Color', 'r')
b1 = -3 * v1;
b2 = -3 * v2;
%quiver(2, 0, b1, b2, 'MaxHeadSize', 0.1, 'Color', 'g')
c1 = 7/2 * v1;
c2 = 7/2 * v2;
%quiver(3, 0, c1, c2, 'MaxHeadSize', 0.1, 'Color', 'y')
sum1 = v1 + u1;
sum2 = v2 + u2;
quiver(3, 0, sum1, sum2, 'MaxHeadSize', 0.1, 'Color', 'y')


%       -----Hallar el vector unitario de v------
modulo_v = sqrt(v1^2 + v2^2);

v1_unitario = v1/nodulo_v;
v2_unitario = v2/nodulo_v;

proof = sqrt(v1_unitario^2 + v2_unitario^2);

f(x) = x^2;


