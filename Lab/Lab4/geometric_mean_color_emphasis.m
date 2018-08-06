function [ new_photo ] = geometric_mean_color_emphasis( photo1, color, threshold )
    %This function will emphasize a color in a photo, and greyscale
    %everything else
    
    %color is a string, acceptable values are currently
    %yellow
    
    %get the rows, columns, and color chanels of a photo
    [rows, columns, chanels] = size(photo1);
    %currently chanels is not used.
    
    %%Photo is a double
    photo = im2double(photo1);

    %%Get the dimensions of the old photo and make the new photo the same
    %%dimensions
    new_photo = photo;
    
    for rows_pixels = 1:rows
        for columns_pixels = 1:columns
            %if the color is red
            R = photo(rows_pixels, columns_pixels, 1);
            
            %if the color is green
            G = photo(rows_pixels, columns_pixels, 2);
            
            %if the color is blue
            B = photo(rows_pixels, columns_pixels, 3);
            
            %Defaulting the distance RGB color to 0
            RGB = [0,0,0];
            
            %If the parameter color is yellow, use the yellow color
            if color == "yellow"
                %WIT Yellow
                RGB = [246, 222, 152];
                %HEX code #f6de98
            end
            
            %Compute the distance between the specified RGB value and the
            %actual pixel's RGB value
            r_dist = RGB(1) - R;
            g_dist = RGB(2) - G;
            b_dist = RGB(3) - B;
            
            %Squaring each term
            r_dist2 = r_dist^2;
            g_dist2 = g_dist^2;
            b_dist2 = b_dist^2;
            
            %Sum the three terms
            radicand = r_dist2 + g_dist2 + b_dist2;
            
            %Apply the square root to the sum.
            distance = sqrt(radicand)/255;
            
            %apply a threshold
            if distance > threshold
               %if the distance is greater than the threshold, we want to
               %greyscale the pixel in that row & column
               squared_color_values = R.^2 + G.^2 + B.^2;
               constant_number = 3 * 255.^2;
               sqrt_of_color_values = sqrt(squared_color_values);
               sqrt_of_constant = sqrt(constant_number);
               average_color = (sqrt_of_color_values / sqrt_of_constant);
               average_color = average_color  * 255;
               new_photo(rows_pixels, columns_pixels, 1) = average_color;
               new_photo(rows_pixels, columns_pixels, 2) = average_color;
               new_photo(rows_pixels, columns_pixels, 3) = average_color;
            else
               %continune to build the image without greyscaled pixels
               new_photo(rows_pixels, columns_pixels, 1) = R;
               new_photo(rows_pixels, columns_pixels, 2) = G;
               new_photo(rows_pixels, columns_pixels, 3) = B;
            end
        end
    end
end

