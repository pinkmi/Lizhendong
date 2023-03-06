function out = signal_processing(file)
    cell_name = strsplit(file, "\");
    out= cell_name(3);
    f = 1800;
    [x, fs] = audioread(file);
    N = length(x);
    fft_x = fftshift(fft(x, N));
    k = -N/2:N/2-1;
    D = fs/N;
    noise = 0.01*sin(2*pi*f*k/fs);
    noise = noise';
    xa = x+noise;
    fft_xa = fftshift(fft(xa, N));
    figure(1)
    stem(k*D, abs(fft_x), "Marker", "none");
    axis([0, 8000, 0, 200])
    set(gca, "FontSize", 14)
    set(gca, "linewidth", 2)
    xlabel('Frequency', 'fontsize', 14, 'interpreter', 'tex', "FontWeight", "bold")
    ylabel('Amplitude', 'fontsize', 14, 'interpreter', 'tex', "FontWeight", "bold");grid;
    filename1 = strcat("D:\\image\\origin", ".jpg");
    saveas(1,filename1);
    figure(2)
    stem(k*D, abs(fft_xa), "Marker", "none");
    axis([0, 8000, 0, 200])
    set(gca, "FontSize", 14)
    set(gca, "linewidth", 2)
    xlabel('Frequency', 'fontsize', 14, 'interpreter', 'tex', "FontWeight", "bold")
    ylabel('Amplitude', 'fontsize', 14, 'interpreter', 'tex', "FontWeight", "bold");grid;
    filename2 = strcat("D:\\image\\processed", ".jpg");
    saveas(2,filename2);
end