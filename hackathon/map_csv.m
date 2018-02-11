

function map_csv()
    % Main file
    map = 'maps.csv'
    
    plot_file(map, 'Signal Strength of Wifi', 0);
end

function plot_file(input_file, my_title, linear)
    display(strcat('Plotting ', my_title))
    % This function takes an input file name and plots the data
    data = csvread(input_file);

    figure;
    
    scatter_plot_signal(data)
    
    figure;
    plot_delaunay(data)
    
    title(my_title);
    xlabel('X (m)');
    ylabel('Y (m)');
    zlabel('Signal Strength (%)');
end

function scatter_plot_signal(data)
    % plots the xy vectors
    scatter3(data(:, 1), data(:, 2), data(:,3), 'r');
    % axis style equal
end

function plot_delaunay(data)
    tri = delaunay(data(:, 1), data(:, 2));
    h = trisurf(tri, data(:, 1), data(:, 2), data(:,3));
    axis vis3d;

end
