function [ data_xun ] = div_xun( Q )
%UNTITLED2 将数据按旬划分，同时合并年份
%    Q(yy,dd,mm);     年/日/月
%    data_xun(36,yy,dd);  将数据按旬重新划分 

[yy,~,~] = size(Q) ;

for i = 1:36
    for j = 1:yy
        for k = 1:10
        end
        if mod(i,3)==0
        end
    end
end
            
    




end

