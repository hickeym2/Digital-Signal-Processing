function [ new_photo ] = iterateOverPhotoGeometric( photo1 )

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
            
            %lets square all the color values, datatype = double
            squared_color_values = R.^2 + G.^2 + B.^2;
            
            %arithmetic defaults to a datatype = double
            %this constant number is from the formula
            constant_number = 3 * 255.^2;     
            
            %this is the numerator being inserted into the square root
            sqrt_of_color_values = sqrt(squared_color_values);
            
            %this is the denominator being inserted into a square root
            sqrt_of_constant = sqrt(constant_number);
            
            %performing the division part of the formula
            %the result is a ratio of our total light levels.
            average_color = (sqrt_of_color_values / sqrt_of_constant);
            
            %We need to get the greyscale color, instead of the ratio
            %Multiply the max light level by the ratio
            average_color = average_color  * 255;

            %%construct the new photo and for every color level, insert the
            %%same average color.
            %for the color red, make its value the average color
            new_photo(rows_pixels, columns_pixels, 1) = average_color;
            %for the color green, make its value the average color
            new_photo(rows_pixels, columns_pixels, 2) = average_color;
            %for the color blue make its value the average color
            new_photo(rows_pixels, columns_pixels, 3) = average_color;
        
        end
    end
    
end

