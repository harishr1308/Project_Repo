import Extra_features 
import Extra_features2
import pca
import pca2
import logistic
import log_reg
import log
a=Extra_features.main()
#Y_train=pca.pca_imp(a)
b=Extra_features2.main()
X_test=pca2.pca_imp(b)
pca2.plot(X_test)
Y_train=[1,0,0,0,0,0,0,0,1,1]
theta= log_reg.th(X_test,Y_train)
#print '\n \n '
#print theta
#log_reg.plot()
i=log.plot_it
log.learning_parameters(i,Y_train,X_test)
