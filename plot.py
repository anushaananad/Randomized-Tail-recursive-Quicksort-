import matplotlib.pyplot as plt
import numpy as np

#Random data
QS_naive_on_random_data_l = [100000,200000,250000,350000,450000]
QS_naive_on_random_data_t = [1.0828227996826172,2.2321082750956216,3.0800811449686685,4.307011604309082,5.5598829587300616]

#QuickSort randomized - random
QS_rand_on_random_data_l = [100000,200000,250000,350000,450000]
QS_rand_on_random_data_t = [1.7336945533752441,3.6076536178588867,4.984167496363322,6.777158339818318,9.497002522150675]

#QuickSort Tail recursive - random
QS_tailrecur_on_random_data_l = [100000,200000,250000,350000,450000]
QS_tailrecur_on_random_data_t = [1.902185599009196,3.980520407358805,5.598591248194377,7.520959854125977,10.196481148401896]

plt.plot(QS_naive_on_random_data_l, QS_naive_on_random_data_t,label="Quicksort naive rand data time")
plt.plot(QS_rand_on_random_data_l, QS_rand_on_random_data_t, label="Quicksort randomized rand data time")
plt.plot(QS_tailrecur_on_random_data_l, QS_tailrecur_on_random_data_t, label="Quicksort Tail-recursive rand data time")
plt.title('Quicksort time comparison on Random dataset')
plt.xlabel("list length")
plt.ylabel("time in seconds")
plt.legend(loc="upper left")
plt.show()

#single valued
QS_naive_on_single_val_data_l = [1000,1500,2000,2500,3000]
QS_naive_on_single_val_data_t = [0.11985460917154948,0.3323500156402588,0.6723294258117676,1.0052847067515056,1.4326109091440837]

QS_rand_on_single_val_data_l = [1000,1500,2000,2500,3000]
QS_rand_on_single_val_data_t = [0.1407783031463623,0.3666975498199463,0.6141944726308187,1.0231750011444092,1.4005641142527263]

QS_tailrecur_on_single_val_data_l = [1000,1500,2000,2500,3000]
QS_tailrecur_on_single_val_data_t = [0.24351954460144043,0.5815362930297852,1.069144328435262,1.5500594774882,2.169408082962036]

plt.plot(QS_naive_on_single_val_data_l, QS_naive_on_single_val_data_t,label="Quicksort naive single val data time")
plt.plot(QS_rand_on_single_val_data_l,QS_rand_on_single_val_data_t,label="Quicksort randomized single val data time")
plt.plot(QS_tailrecur_on_single_val_data_l,QS_tailrecur_on_single_val_data_t,label="Quicksort Tail-recursive single val data time")
plt.title('Quicksort time comparison on Single-valued dataset')
plt.xlabel("list length")
plt.ylabel("time in seconds")
plt.legend(loc="upper left")
plt.show()

#reverse sorted
QS_naive_on_rev_sorted_data_l = [1000,1500,2000,2500,3000]
QS_navie_on_rev_sorted_data_t = [0.10060548782348633,0.22244580586751303,0.4136198361714681,0.6249082088470459,0.91417129834493]

QS_rand_on_rev_sorted_data_l = [1000,1500,2000,2500,3000]
QS_rand_on_rev_sorted_data_t = [0.010340213775634766,0.020153125127156574,0.02692890167236328,0.03258967399597168,0.036373138427734375]

QS_tailrecur_on_rev_sorted_data_l = [1000,1500,2000,2500,3000]
QS_tailrecur_on_rev_sorted_data_t = [0.012996355692545572,0.013607978820800781,0.023600339889526367,0.031495253245035805,0.03291018803914388]


plt.plot(QS_naive_on_rev_sorted_data_l, QS_navie_on_rev_sorted_data_t,label="Quicksort naive rev sorted data time")
plt.plot(QS_rand_on_rev_sorted_data_l,QS_rand_on_rev_sorted_data_t,label="Quicksort randomized rev sorted data time")
plt.plot(QS_tailrecur_on_rev_sorted_data_l,QS_tailrecur_on_rev_sorted_data_t,label="Quicksort Tail-recursive rev sorted data time")
plt.title('Quicksort time comparison on Reverse-sorted dataset')
plt.xlabel("list length")
plt.ylabel("time in seconds")
plt.legend(loc="upper left")
plt.show()

#sorted data
QS_naive_on_sorted_data_l = [100,300,500,700,1000]
QS_navie_on_sorted_data_t = [0.0029986699422200522,0.017285744349161785,0.03459580739339193,0.07879185676574707,0.17490005493164062]

QS_rand_on_sorted_data_l = [100,300,500,700,1000]
QS_rand_on_sorted_data_t = [0.0016621748606363933, 0.004665692647298177,0.008659442265828451,0.009652058283487955,0.013651371002197266]

QS_tailrecur_on_sorted_data_l = [100,300,500,700,1000]
QS_tailrecur_on_sorted_data_t = [0.0015238126118977864,0.003988901774088542,0.008976141611735025,0.009650786717732748,0.01298666000366211]


plt.plot(QS_naive_on_sorted_data_l, QS_navie_on_sorted_data_t,label="Quicksort naive sorted data time")
plt.plot(QS_rand_on_sorted_data_l,QS_rand_on_sorted_data_t,label="Quicksort randomized sorted data time")
plt.plot(QS_tailrecur_on_sorted_data_l,QS_tailrecur_on_sorted_data_t,label="Quicksort Tail-recursive sorted data time")
plt.title('Quicksort time comparison on Sorted dataset')
plt.xlabel("list length")
plt.ylabel("time in seconds")
plt.legend(loc="upper left")
plt.show()




#single val data


#randomdataset -> naive/ randomized/ tail recur
#sorteddata -> all 3 
#revsorted -> all 3
#singlevalued -> all 3

#for taking out the time -> 4 runs for each algo -> ignore 1st . take avg of last3

