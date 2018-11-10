function [ data_xun ] = div_xun( Q )
%UNTITLED2 将数据按旬划分，同时合并年份
%    Q(yy,dd,mm);     年/日/月
%    data_xun(36,yy,dd);  将数据按旬重新划分 

[yy,~,~] = size(Q) ;
data_xun = zero(36,yy,11);
for i = 1:36
    for j = 1:yy
        for k = 1:10
            data_xun(i,j,k) = Q(j,k+mod(i,3)*10,ceil(i/3)) ;
        end
        if mod(i,3)==0
            data_xun(i,j,11) = Q(j,31,ceil(i/3)) ;
        end
    end
end



 z=find(data_xun==0);

data_xun(z)=[];

a = sum(sum(sum(data_xun)))   -   sum(sum(sum(Q))) ;




end

