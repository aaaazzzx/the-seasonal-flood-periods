function [ data_m ] = div_m( Q )
% 将数据按月重新排序，同时合并年份
%    Q(yy,dd,mm);     年/日/月
%    data_m(12,yy*31);  将数据按月重新划分 

[yy,~,~] = size(Q) ;
data_m = zeros(12,yy*31);
for i = 1:12
    for j = 1:yy
        for k = 1:31
            data_m(i,(j-1)*31+k) = Q(j,k,i) ;
        end
    end
end


end

