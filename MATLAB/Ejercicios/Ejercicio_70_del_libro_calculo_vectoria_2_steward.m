x = [-6:0.1:6];
y = -x.^2 + 5;
p1 = 1;
p2 = 4;
v1 = 1;
v2 = -2;

modulo_v = sqrt(v1^.2+v2.^2);
v1_unitario = v1/modulo_v;
v2_unitario = v2/modulo_v;

plot(x, y)
hold on
scatter(p1, p2, '.')
quiver(p1, p2, v1_unitario, v2_unitario, 'MaxHeadSize', 0.1)
quiver(p1, p2, v1_unitario, -v2_unitario, 'MaxHeadSize', 0.1)