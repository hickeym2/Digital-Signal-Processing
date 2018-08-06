% Question 1
matrix1 =   [1,5,3,7;4,7,6,10;2,4,3,2;5,2,8,3]      
matrix2 =   (1/9)*[1,1,1;1,1,1;1,1,1]   %Filter    
matrix3 = conv2(matrix1, matrix2, 'valid')

%Question 3

matrix4 = [5,4,4,5;1,2,1,2;3,8,9,3;1,3,3,1]
matrix5 = [-1,-1,-1;-1,8,-1;-1,-1,-1]   %Filter
matrix6 = conv2(matrix4, matrix5, 'valid')

%Question 5
%imshow(imageOfInterest, []);

%Question 6
%photoOut = conv2(imageOfInterest, matrix2, 'valid');
%imshow(photoOut,[]);

%Question 7
%photoOut2 = conv2(imageOfInterest, matrix5, 'valid')
%imshow(photoOut2,[])

%Question 8
matrix7 = (1/256)* [1,4,6,4,1;
                    4,16,24,16,4;
                    6,24,36,24,6;
                    4,16,24,16,4;
                    1,4,6,4,1]
                
%photoOut3 = conv2(imageOfInterest, matrix7, 'valid');                
%imshow(photoOut3, [])

matrix8 = (-1/256)*[1,4,6,4,1;
                    4,16,24,16,4;
                    6,24,-476,24,6;
                    4,16,24,16,6;
                    1,4,6,4,1]

photoOut4 = conv2(imageOfInterest, matrix8, 'valid')
imshow(photoOut4, [])
