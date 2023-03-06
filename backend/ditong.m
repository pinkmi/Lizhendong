function out=ditong(ap,as,wp,ws)
%直接设计数字滤波器
    Fs=512; %定义采样频率
    omegap=2*wp/Fs; %将模拟指标转换为数字指标
    omegas=2*ws/Fs; %将模拟指标转换为数字指标
    [N,wn]=buttord(omegap,omegas,ap,as); %直接使用数字滤波器设计方式进行设计 
    [b,a]=butter(N,wn); %计算滤波器系统函数分子分母
    disp("分子系数b");
    fprintf("%.4e   ",b);
    fprintf('\n');
    disp('分母系数a');fprintf('%.4e    ',a);fprintf('\n');
    %omega=0:0.01:pi;
    [h, w]=freqz(b,a,Fs);
    out=N;
    ampli=20*log10(abs(h));
    figure;
    plot(w/pi,ampli,"k","linewidth",2)
    xlabel('\fontname{Times New Roman}Digital frequency\fontname{Times New Roman}/\pi', 'fontsize', 14, 'interpreter', 'tex')
    ylabel('\fontname{Times New Roman}Amplitude\fontname{Times New Roman}/dB', 'fontsize', 14, 'interpreter', 'tex');grid;
    set(gca, "FontSize", 14, "FontName", "Times New Roman")
    set(gca, "linewidth", 2)
    filename1 = strcat("D:\\image\\lowpassAM", num2str(ap), num2str(as), num2str(wp), num2str(ws), ".jpg");
    saveas(1,filename1)
    theta=phasez(b,a,Fs);
    figure;
    plot(w/pi,theta*360/(2*pi),"k","linewidth",2)
%     xlabel('数字频率/\pi', "fontsize", 14, "FontWeight", "bold", "FontName", "Times New Roman");
    xlabel('\fontname{Times New Roman}Digital frequency\fontname{Times New Roman}/\pi', 'fontsize', 14, 'interpreter', 'tex')
    ylabel('\fontname{Times New Roman}Phase\fontname{Times New Roman}/°', 'fontsize', 14, 'interpreter', 'tex');grid;
    set(gca, "FontSize", 14, "FontName", "Times New Roman")
    set(gca, "linewidth", 2)
    filename2 = strcat("D:\\image\\lowpassPM", num2str(ap), num2str(as), num2str(wp), num2str(ws), ".jpg");
    saveas(2,filename2)
end