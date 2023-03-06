function out = image_processing(file)   
    cell_name = strsplit(file, "\");
    out = cell_name(3);
    pic = imread(file);
    figure(1)
    imshow(pic);
    saveas(1,"D:\image\origin_img.jpg");
    figure(2)
    pic_gray = rgb2gray(pic);
    imshow(pic_gray);
    saveas(2,"D:\image\gray_img.jpg");
end