from sklearn.base import TransformerMixin
class NexOff(TransformerMixin):
  def fit(self,x=None,y=None):
    self.cos_sim=y
    self.ip=x
  def getdeliverycode(self,deliverycode,ip):
    return ip[ip.deliverycode == deliverycode]["index"].values[0]
  def getindex(self,index,ip):
    return ip[ip.index == index]["noffer"].values[0]
  def predict(self,y=None):
    self.cindex=self.getdeliverycode(y,self.ip)
    #return self.cindex
    self.nxtoffer=list(enumerate(self.cos_sim[self.cindex]))
    self.sort=sorted(self.nxtoffer,key=lambda x:x[1],reverse=True)
    a=self.sort[0]
    b=a[0]-1
    noffer=self.getindex(b,self.ip)
    return noffer
