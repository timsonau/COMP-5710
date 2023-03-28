from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, linear_model
import pandas as pd
import numpy as np 
import mnist
import logging
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical

#create logger obj
format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
file_name  = 'app.log'
logging.basicConfig(format=format_str, filemode='w', filename=file_name, level=logging.INFO)
logObj = logging.getLogger('ml-logger')
    
def readData():
    iris = datasets.load_iris()
    #log because a external data set is being introduced. Can log for poisoning attacks 
    logObj.info("data loaded: iris dataset in readData()")
    print(type(iris.data), type(iris.target))
    X = iris.data
    Y = iris.target
    df = pd.DataFrame(X, columns=iris.feature_names)
    print(df.head())

    return df 

def makePrediction():
    iris = datasets.load_iris()
    #log because a external data set is being introduced. Can log for poisoning attacks 
    logObj.info('data loaded: iris dataset in makePrediction()')
    knn = KNeighborsClassifier(n_neighbors=6)
    knn.fit(iris['data'], iris['target'])
    X = [
        [5.9, 1.0, 5.1, 1.8],
        [3.4, 2.0, 1.1, 4.8],
    ]
    prediction = knn.predict(X)
    print(prediction)    

def doRegression():
    diabetes = datasets.load_diabetes()
    #log because a external data set is being introduced. Can log for poisoning attacks 
    logObj.info('data loaded: diabetes dataset in doRegression()')
    diabetes_X = diabetes.data[:, np.newaxis, 2]
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]
    regr = linear_model.LinearRegression()
    regr.fit(diabetes_X_train, diabetes_y_train)
    diabetes_y_pred = regr.predict(diabetes_X_test)
    #log because a prediction is made with model. Can log and catch model tricking
    logObj.info("prediction made: linear regression model prediction on diabetes_X in doRegression() result \n%s\n", diabetes_y_pred)


def doDeepLearning():
    train_images = mnist.train_images()
    #log because a external data set is being introduced. Can log for poisoning attacks 
    logObj.info('data loaded: mnist training images in doDeepLearning()')
    train_labels = mnist.train_labels()
    #log because a external data set is being introduced. Can log for poisoning attacks 
    logObj.info('data loaded: mnist training labels in doDeepLearning()')

    test_images = mnist.test_images()
    test_labels = mnist.test_labels()


    train_images = (train_images / 255) - 0.5
    test_images = (test_images / 255) - 0.5


    train_images = np.expand_dims(train_images, axis=3)
    test_images = np.expand_dims(test_images, axis=3)

    num_filters = 8
    filter_size = 3
    pool_size = 2

    model = Sequential([
    Conv2D(num_filters, filter_size, input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=pool_size),
    Flatten(),
    Dense(10, activation='softmax'),
    ])
    # Compile the model.
    model.compile(
    'adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
    )

    # Train the model.
    model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=3,
    validation_data=(test_images, to_categorical(test_labels)),
    )
    

    model.save_weights('cnn.h5')

    predictions = model.predict(test_images[:5])
    #log because a prediction is made with model. Can log and catch model tricking.
    logObj.info("prediction made: model prediction on test_images[:5] in doDeepLearning() result \n%s\n", predictions)

    print(np.argmax(predictions, axis=1)) # [7, 2, 1, 0, 4]

    print(test_labels[:5]) # [7, 2, 1, 0, 4]


if __name__=='__main__': 

    data_frame = readData()
    makePrediction() 
    doRegression() 
    doDeepLearning() 