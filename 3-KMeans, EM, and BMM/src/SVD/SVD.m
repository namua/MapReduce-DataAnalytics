A = [2 5 0 6 0 3 5;1 4 9 0 0 3 0;5 0 5 0 4 1 1;0 8 0 4 8 1 0;1 9 6 3 7 8 9;10 2 3 0 5 2 5];
[U,S,V] = svd(A);

figure
for i = 1:7
    x = V(1,i);
    y = V(2,i);
    dx = 0.01; dy = 0.01; 
    scatter(x,y);
    hold on
    name = strcat('word',int2str(i));
    text(x+dx, y+dy, name);
    hold on
end
title('scatter plot of the remapped 2D space');

