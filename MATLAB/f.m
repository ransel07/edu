x = [-6:0.1:6];
y = x.^2;
plot(x, y)
hold on
scatter(3, 9, '.')
v1 = 1;
v2 = 6;
modulo_v = sqrt(v1^.2+v2.^2);
v1_unitario = v1/modulo_v;
v2_unitario = v2/modulo_v;

quiver(3, 9, v1_unitario, v2_unitario, 'MaxHeadSize', 0.1)