function [ data_m ] = div_m( Q )
% �����ݰ�����������ͬʱ�ϲ����
%    Q(yy,dd,mm);     ��/��/��
%    data_m(12,yy*31);  �����ݰ������»��� 

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

