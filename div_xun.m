function [ data_xun ] = div_xun( Q )
%UNTITLED2 �����ݰ�Ѯ���֣�ͬʱ�ϲ����
%    Q(yy,dd,mm);     ��/��/��
%    data_xun(36,yy,dd);  �����ݰ�Ѯ���»��� 

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

