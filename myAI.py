def callAI(activationFunction):
	import tensorflow as tf
	from tensorflow.keras import datasets, layers, models
	from keras.models import Sequential
	from keras.layers import Dense, SimpleRNN
	
	fashion_mnist = tf.keras.datasets.fashion_mnist
	
	(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
	
	train_images = train_images / 255.0
	test_images = test_images / 255.0
	
	model = models.Sequential()
	model.add(SimpleRNN(32, input_shape=(28, 28), activation=activationFunction))
	model.add(Dense(units=10, activation=activationFunction))
	model.compile(loss='mean_squared_error', optimizer='adam')
	
	model.compile(optimizer='adam',
	              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
	              metrics=['accuracy'])
	
	model.fit(train_images, train_labels, epochs=5,
	          validation_data=(test_images, test_labels))
	
	test_loss, accuracy = model.evaluate(test_images,  test_labels, verbose=2)
	
	print('\nTest accuracy:', accuracy)
	return accuracy

activationAccuracy = []

activationAccuracy.append(callAI('tanh'))

activationAccuracy.append(callAI('sigmoid'))

activationAccuracy.append(callAI('elu'))

print(activationAccuracy)