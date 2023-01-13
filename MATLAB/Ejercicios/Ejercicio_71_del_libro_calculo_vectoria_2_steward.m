x = [-2:0.1:2];
y = tan(x);
p1 = pi/4;
p2 = 1;
v1 = 1;
v2 = tan(p2);

modulo_v = sqrt(v1^.2+v2.^2);
v1_unitario = v1/modulo_v;
v2_unitario = v2/modulo_v;

plot(x, y)
hold on
scatter(p1, p2, '.')
quiver(p1, p2, v1_unitario, v2_unitario, 'MaxHeadSize', 0.1)
quiver(p1, p2, v2_unitario, v1_unitario, 'MaxHeadSize', 0.1)