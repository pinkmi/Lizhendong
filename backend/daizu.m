function out=daizu(ap,as,fpl,fph,fsl,fsh)
    fs=80;
    omegapl=2*pi*fpl/fs/pi;
    omegaph=2*pi*fph/fs/pi;
    omegasl=2*pi*fsl/fs/pi;
    omegash=2*pi*fsh/fs/pi;
    [N,wn]=buttord([omegapl omegaph],[omegasl omegash],ap,as);
    [bz,az]=butter(N,wn,"stop");
    [h,f]=freqz(bz,az,fs);
    disp("分子系数b");
    fprintf("%.4e   ",bz);
    fprintf('\n');
    disp('分母系数a');fprintf('%.4e    ',az);fprintf('\n');
    out=N;
    ampli=20*log10(abs(h));
    figure
    plot(f/pi,ampli,"k","linewidth",2)
    set(gca, "FontSize", 14, "FontName", "Times New Roman")
    set(gca, "linewidth", 2)
    xlabel('\fontname{Times New Roman}Digital frequency\fontname{Times New Roman}/\pi', 'fontsize', 14, 'interpreter', 'tex', "FontWeight", "bold")
    ylabel('\fontname{Times New Roman}Amplitude\fontname{Times New Roman}/dB', 'fontsize', 14, 'interpreter', 'tex', "FontWeight", "bold");grid;
    filename1 = strcat("D:\\image\\bandstopAM", num2str(ap), num2str(as), num2str(fpl), num2str(fph), num2str(fsl), num2str(fsh), ".jpg");
    saveas(1,filename1);
    figure
    [theta,fx]=phasez(bz,az,fs);
    plot(fx,theta*360/(2*pi),"k","linewidth",2);
    xlabel('\fontname{Times New Roman}Digital frequency\fontname{Times New Roman}/\pi', 'fontsize', 14, 'interpreter', 'tex', "FontWeight", "bold")
    ylabel('\fontname{Times New Roman}Phase\fontname{Times New Roman}/°', 'fontsize', 14, 'interpreter', 'tex', "FontWeight", "bold");grid;
    set(gca, "FontSize", 14, "FontName", "Times New Roman")
    set(gca, "linewidth", 2)
    filename2 = strcat("D:\\image\\bandstopPM", num2str(ap), num2str(as), num2str(fpl), num2str(fph), num2str(fsl), num2str(fsh), ".jpg");
    saveas(2,filename2);
end