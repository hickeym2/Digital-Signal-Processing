function [ newPhoto ] = arithmetic_greyscale( photo )
    %get the rows, columns, and color chanels of a photo
    [rows, columns, chanels] = size(photo);
    %chanels is currently not used.
    
    %%Get the dimensions of the old photo and make the new photo the same
    %%dimensions
    newPhoto = photo;
    
    for rowsPixel = 1:rows
        for columnsPixel = 1:columns
            %if the color is red
            R = photo(rowsPixel, columnsPixel, 1);
            
            %if the color is green
            G = photo(rowsPixel, columnsPixel, 2);
            
            %if the color is blue
            B = photo(rowsPixel, columnsPixel, 3);
            
            %average all the RGB colors
            %the number 3 is the number of chanels
            averageColor = (R + G + B)/3;
            
            %Replace every RGB color value with the averageColor value
            newPhoto(rowsPixel, columnsPixel, 1) = averageColor; 
            newPhoto(rowsPixel, columnsPixel, 2) = averageColor; 
            newPhoto(rowsPixel, columnsPixel, 3) = averageColor;
        end
    end
end

