Amount of test tweets: 100
Amount of train tweets: 19900
train classification size: 19900
test classification size: 100
Max tweet size(by words): 51
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding (Embedding)        (None, 51, 100)           2683600   
_________________________________________________________________
conv1d (Conv1D)              (None, 44, 32)            25632     
_________________________________________________________________
max_pooling1d (MaxPooling1D) (None, 22, 32)            0         
_________________________________________________________________
flatten (Flatten)            (None, 704)               0         
_________________________________________________________________
dense (Dense)                (None, 10)                7050      
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 11        
=================================================================
Total params: 2,716,293
Trainable params: 2,716,293
Non-trainable params: 0
_________________________________________________________________
Epoch 1/50
622/622 - 19s - loss: 0.1471 - accuracy: 0.9287
Epoch 2/50
622/622 - 10s - loss: -3.2859e-01 - accuracy: 0.9650
Epoch 3/50
622/622 - 10s - loss: -1.3632e+01 - accuracy: 0.9603
Epoch 4/50
622/622 - 10s - loss: -1.0690e+02 - accuracy: 0.9575
Epoch 5/50
622/622 - 10s - loss: -3.9701e+02 - accuracy: 0.9589
Epoch 6/50
622/622 - 10s - loss: -1.0126e+03 - accuracy: 0.9599
Epoch 7/50
622/622 - 10s - loss: -2.0909e+03 - accuracy: 0.9620
Epoch 8/50
622/622 - 10s - loss: -3.7349e+03 - accuracy: 0.9612
Epoch 9/50
622/622 - 10s - loss: -6.0977e+03 - accuracy: 0.9601
Epoch 10/50
622/622 - 10s - loss: -9.2750e+03 - accuracy: 0.9648
Epoch 11/50
622/622 - 10s - loss: -1.3569e+04 - accuracy: 0.9643
Epoch 12/50
622/622 - 10s - loss: -1.8863e+04 - accuracy: 0.9628
Epoch 13/50
622/622 - 10s - loss: -2.5357e+04 - accuracy: 0.9632
Epoch 14/50
622/622 - 10s - loss: -3.3433e+04 - accuracy: 0.9651
Epoch 15/50
622/622 - 10s - loss: -4.3070e+04 - accuracy: 0.9646
Epoch 16/50
622/622 - 10s - loss: -5.4403e+04 - accuracy: 0.9652
Epoch 17/50
622/622 - 10s - loss: -6.7726e+04 - accuracy: 0.9658
Epoch 18/50
622/622 - 10s - loss: -8.3124e+04 - accuracy: 0.9634
Epoch 19/50
622/622 - 10s - loss: -1.0067e+05 - accuracy: 0.9645
Epoch 20/50
622/622 - 10s - loss: -1.2043e+05 - accuracy: 0.9682
Epoch 21/50
622/622 - 10s - loss: -1.4315e+05 - accuracy: 0.9654
Epoch 22/50
622/622 - 10s - loss: -1.6913e+05 - accuracy: 0.9642
Epoch 23/50
622/622 - 10s - loss: -1.9797e+05 - accuracy: 0.9663
Epoch 24/50
622/622 - 10s - loss: -2.2996e+05 - accuracy: 0.9669
Epoch 25/50
622/622 - 10s - loss: -2.6616e+05 - accuracy: 0.9659
Epoch 26/50
622/622 - 10s - loss: -3.0556e+05 - accuracy: 0.9659
Epoch 27/50
622/622 - 10s - loss: -3.4943e+05 - accuracy: 0.9652
Epoch 28/50
622/622 - 10s - loss: -3.9675e+05 - accuracy: 0.9679
Epoch 29/50
622/622 - 10s - loss: -4.4945e+05 - accuracy: 0.9676
Epoch 30/50
622/622 - 10s - loss: -5.0846e+05 - accuracy: 0.9659
Epoch 31/50
622/622 - 10s - loss: -5.7048e+05 - accuracy: 0.9662
Epoch 32/50
622/622 - 10s - loss: -6.3846e+05 - accuracy: 0.9668
Epoch 33/50
622/622 - 10s - loss: -7.1104e+05 - accuracy: 0.9663
Epoch 34/50
622/622 - 11s - loss: -7.9148e+05 - accuracy: 0.9667
Epoch 35/50
622/622 - 10s - loss: -8.7746e+05 - accuracy: 0.9668
Epoch 36/50
622/622 - 10s - loss: -9.7237e+05 - accuracy: 0.9650
Epoch 37/50
622/622 - 10s - loss: -1.0713e+06 - accuracy: 0.9680
Epoch 38/50
622/622 - 10s - loss: -1.1768e+06 - accuracy: 0.9666
Epoch 39/50
622/622 - 10s - loss: -1.2910e+06 - accuracy: 0.9658
Epoch 40/50
622/622 - 10s - loss: -1.4128e+06 - accuracy: 0.9673
Epoch 41/50
622/622 - 10s - loss: -1.5432e+06 - accuracy: 0.9682
Epoch 42/50
622/622 - 10s - loss: -1.6831e+06 - accuracy: 0.9679
Epoch 43/50
622/622 - 10s - loss: -1.8305e+06 - accuracy: 0.9667
Epoch 44/50
622/622 - 10s - loss: -1.9890e+06 - accuracy: 0.9680
Epoch 45/50
622/622 - 10s - loss: -2.1548e+06 - accuracy: 0.9672
Epoch 46/50
622/622 - 10s - loss: -2.3317e+06 - accuracy: 0.9694
Epoch 47/50
622/622 - 10s - loss: -2.5235e+06 - accuracy: 0.9660
Epoch 48/50
622/622 - 10s - loss: -2.7210e+06 - accuracy: 0.9688
Epoch 49/50
622/622 - 10s - loss: -2.9341e+06 - accuracy: 0.9669
Epoch 50/50
622/622 - 10s - loss: -3.1598e+06 - accuracy: 0.9676
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_2 (Dense)              (None, 50)                1341850   
_________________________________________________________________
dense_3 (Dense)              (None, 1)                 51        
=================================================================
Total params: 1,341,901
Trainable params: 1,341,901
Non-trainable params: 0
_________________________________________________________________
Epoch 1/100
622/622 - 3s - loss: 0.2947 - accuracy: 0.9042
Epoch 2/100
622/622 - 3s - loss: 0.1435 - accuracy: 0.9258
Epoch 3/100
622/622 - 3s - loss: 0.0852 - accuracy: 0.9486
Epoch 4/100
622/622 - 3s - loss: 0.0451 - accuracy: 0.9611
Epoch 5/100
622/622 - 3s - loss: 0.0126 - accuracy: 0.9691
Epoch 6/100
622/622 - 3s - loss: -1.6452e-02 - accuracy: 0.9745
Epoch 7/100
622/622 - 3s - loss: -4.4827e-02 - accuracy: 0.9786
Epoch 8/100
622/622 - 3s - loss: -7.4133e-02 - accuracy: 0.9807
Epoch 9/100
622/622 - 3s - loss: -1.0495e-01 - accuracy: 0.9832
Epoch 10/100
622/622 - 3s - loss: -1.3809e-01 - accuracy: 0.9835
Epoch 11/100
622/622 - 3s - loss: -1.7377e-01 - accuracy: 0.9845
Epoch 12/100
622/622 - 3s - loss: -2.1266e-01 - accuracy: 0.9849
Epoch 13/100
622/622 - 3s - loss: -2.5341e-01 - accuracy: 0.9850
Epoch 14/100
622/622 - 3s - loss: -2.9730e-01 - accuracy: 0.9847
Epoch 15/100
622/622 - 3s - loss: -3.4456e-01 - accuracy: 0.9855
Epoch 16/100
622/622 - 3s - loss: -3.9348e-01 - accuracy: 0.9849
Epoch 17/100
622/622 - 3s - loss: -4.4607e-01 - accuracy: 0.9852
Epoch 18/100
622/622 - 3s - loss: -5.0124e-01 - accuracy: 0.9856
Epoch 19/100
622/622 - 3s - loss: -5.5893e-01 - accuracy: 0.9857
Epoch 20/100
622/622 - 3s - loss: -6.1867e-01 - accuracy: 0.9854
Epoch 21/100
622/622 - 3s - loss: -6.8250e-01 - accuracy: 0.9862
Epoch 22/100
622/622 - 3s - loss: -7.4703e-01 - accuracy: 0.9857
Epoch 23/100
622/622 - 3s - loss: -8.1589e-01 - accuracy: 0.9859
Epoch 24/100
622/622 - 3s - loss: -8.8638e-01 - accuracy: 0.9861
Epoch 25/100
622/622 - 3s - loss: -9.5946e-01 - accuracy: 0.9857
Epoch 26/100
622/622 - 3s - loss: -1.0358e+00 - accuracy: 0.9858
Epoch 27/100
622/622 - 3s - loss: -1.1139e+00 - accuracy: 0.9860
Epoch 28/100
622/622 - 3s - loss: -1.1940e+00 - accuracy: 0.9851
Epoch 29/100
622/622 - 3s - loss: -1.2802e+00 - accuracy: 0.9864
Epoch 30/100
622/622 - 3s - loss: -1.3656e+00 - accuracy: 0.9856
Epoch 31/100
622/622 - 3s - loss: -1.4547e+00 - accuracy: 0.9856
Epoch 32/100
622/622 - 3s - loss: -1.5485e+00 - accuracy: 0.9858
Epoch 33/100
622/622 - 3s - loss: -1.6401e+00 - accuracy: 0.9845
Epoch 34/100
622/622 - 3s - loss: -1.7366e+00 - accuracy: 0.9858
Epoch 35/100
622/622 - 3s - loss: -1.8381e+00 - accuracy: 0.9861
Epoch 36/100
622/622 - 3s - loss: -1.9382e+00 - accuracy: 0.9853
Epoch 37/100
622/622 - 3s - loss: -2.0418e+00 - accuracy: 0.9854
Epoch 38/100
622/622 - 3s - loss: -2.1472e+00 - accuracy: 0.9852
Epoch 39/100
622/622 - 3s - loss: -2.2543e+00 - accuracy: 0.9854
Epoch 40/100
622/622 - 3s - loss: -2.3658e+00 - accuracy: 0.9856
Epoch 41/100
622/622 - 3s - loss: -2.4792e+00 - accuracy: 0.9850
Epoch 42/100
622/622 - 3s - loss: -2.5955e+00 - accuracy: 0.9848
Epoch 43/100
622/622 - 3s - loss: -2.7145e+00 - accuracy: 0.9856
Epoch 44/100
622/622 - 3s - loss: -2.8350e+00 - accuracy: 0.9852
Epoch 45/100
622/622 - 3s - loss: -2.9594e+00 - accuracy: 0.9852
Epoch 46/100
622/622 - 3s - loss: -3.0848e+00 - accuracy: 0.9853
Epoch 47/100
622/622 - 3s - loss: -3.2145e+00 - accuracy: 0.9850
Epoch 48/100
622/622 - 3s - loss: -3.3472e+00 - accuracy: 0.9862
Epoch 49/100
622/622 - 3s - loss: -3.4804e+00 - accuracy: 0.9845
Epoch 50/100
622/622 - 3s - loss: -3.6178e+00 - accuracy: 0.9855
Epoch 51/100
622/622 - 3s - loss: -3.7567e+00 - accuracy: 0.9847
Epoch 52/100
622/622 - 3s - loss: -3.8953e+00 - accuracy: 0.9852
Epoch 53/100
622/622 - 3s - loss: -4.0389e+00 - accuracy: 0.9851
Epoch 54/100
622/622 - 3s - loss: -4.1851e+00 - accuracy: 0.9853
Epoch 55/100
622/622 - 3s - loss: -4.3307e+00 - accuracy: 0.9849
Epoch 56/100
622/622 - 3s - loss: -4.4805e+00 - accuracy: 0.9847
Epoch 57/100
622/622 - 3s - loss: -4.6334e+00 - accuracy: 0.9851
Epoch 58/100
622/622 - 3s - loss: -4.7870e+00 - accuracy: 0.9848
Epoch 59/100
622/622 - 3s - loss: -4.9465e+00 - accuracy: 0.9851
Epoch 60/100
622/622 - 3s - loss: -5.1070e+00 - accuracy: 0.9848
Epoch 61/100
622/622 - 3s - loss: -5.2703e+00 - accuracy: 0.9849
Epoch 62/100
622/622 - 3s - loss: -5.4391e+00 - accuracy: 0.9852
Epoch 63/100
622/622 - 3s - loss: -5.6048e+00 - accuracy: 0.9845
Epoch 64/100
622/622 - 3s - loss: -5.7736e+00 - accuracy: 0.9856
Epoch 65/100
622/622 - 3s - loss: -5.9465e+00 - accuracy: 0.9848
Epoch 66/100
622/622 - 3s - loss: -6.1241e+00 - accuracy: 0.9854
Epoch 67/100
622/622 - 3s - loss: -6.3032e+00 - accuracy: 0.9852
Epoch 68/100
622/622 - 3s - loss: -6.4830e+00 - accuracy: 0.9848
Epoch 69/100
622/622 - 3s - loss: -6.6687e+00 - accuracy: 0.9848
Epoch 70/100
622/622 - 3s - loss: -6.8576e+00 - accuracy: 0.9853
Epoch 71/100
622/622 - 3s - loss: -7.0425e+00 - accuracy: 0.9845
Epoch 72/100
622/622 - 3s - loss: -7.2341e+00 - accuracy: 0.9845
Epoch 73/100
622/622 - 3s - loss: -7.4263e+00 - accuracy: 0.9851
Epoch 74/100
622/622 - 3s - loss: -7.6240e+00 - accuracy: 0.9847
Epoch 75/100
622/622 - 3s - loss: -7.8243e+00 - accuracy: 0.9853
Epoch 76/100
622/622 - 3s - loss: -8.0251e+00 - accuracy: 0.9848
Epoch 77/100
622/622 - 3s - loss: -8.2309e+00 - accuracy: 0.9846
Epoch 78/100
622/622 - 3s - loss: -8.4354e+00 - accuracy: 0.9846
Epoch 79/100
622/622 - 3s - loss: -8.6493e+00 - accuracy: 0.9847
Epoch 80/100
622/622 - 3s - loss: -8.8498e+00 - accuracy: 0.9847
Epoch 81/100
622/622 - 3s - loss: -9.0629e+00 - accuracy: 0.9851
Epoch 82/100
622/622 - 3s - loss: -9.2777e+00 - accuracy: 0.9845
Epoch 83/100
622/622 - 3s - loss: -9.4943e+00 - accuracy: 0.9853
Epoch 84/100
622/622 - 3s - loss: -9.7066e+00 - accuracy: 0.9846
Epoch 85/100
622/622 - 3s - loss: -9.9290e+00 - accuracy: 0.9843
Epoch 86/100
622/622 - 3s - loss: -1.0149e+01 - accuracy: 0.9842
Epoch 87/100
622/622 - 3s - loss: -1.0373e+01 - accuracy: 0.9847
Epoch 88/100
622/622 - 3s - loss: -1.0597e+01 - accuracy: 0.9847
Epoch 89/100
622/622 - 3s - loss: -1.0822e+01 - accuracy: 0.9846
Epoch 90/100
622/622 - 3s - loss: -1.1057e+01 - accuracy: 0.9853
Epoch 91/100
622/622 - 3s - loss: -1.1286e+01 - accuracy: 0.9847
Epoch 92/100
622/622 - 3s - loss: -1.1524e+01 - accuracy: 0.9848
Epoch 93/100
622/622 - 3s - loss: -1.1761e+01 - accuracy: 0.9843
Epoch 94/100
622/622 - 3s - loss: -1.2003e+01 - accuracy: 0.9848
Epoch 95/100
622/622 - 3s - loss: -1.2248e+01 - accuracy: 0.9848
Epoch 96/100
622/622 - 3s - loss: -1.2491e+01 - accuracy: 0.9851
Epoch 97/100
622/622 - 3s - loss: -1.2737e+01 - accuracy: 0.9842
Epoch 98/100
622/622 - 3s - loss: -1.2989e+01 - accuracy: 0.9849
Epoch 99/100
622/622 - 3s - loss: -1.3241e+01 - accuracy: 0.9841
Epoch 100/100
622/622 - 3s - loss: -1.3499e+01 - accuracy: 0.9847
Train Accuracy for MLP model: 98.90 
Test Accuracy for MLP model: 95.00 
Train Accuracy for CNN model: 96.63 
Test Accuracy for CNN model: 90.00 
size of encoded:  26836
MLP model, Review: [crypto will definitley go up. It has a bright future! #bitcoin]
Sentiment: POSITIVE (100.000%) 
size of encoded:  26836
MLP model, Review: [crypto will die soon!!! Please dont buy]
Sentiment: NEGATIVE (100.000%) 


CNN model, Review: [crypto will definitley go up. It has a bright future! #bitcoin]
Sentiment: POSITIVE (100.000%) 
CNN model, Review: [crypto will die soon!!! Please dont buy]
Sentiment: NEGATIVE (100.000%) 
