from keras.datasets import  mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils


image_w = 28
image_h = 28
nb_classes = 10

def main():
    # MNIST 데이터 읽어 들이기
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()

    # 모델 구축
    model = build_model()
    model.fit(X_train, Y_train, batch_size = 128, epochs = 20, verbose=1, validation_data = (X_test, Y_test))

    # 모델 저장
    model.save_weights('mnist.hdf5')

    # 모델 평가
    score = model.evaluate(X_test, Y_test, verbose = 0)
    print('score=', score)

def build_model():
    # MLP 모델 구축
    model = Sequential()
    # model = Sequential()
    model.add(Dense(512, input_shape=(784,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(10))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',optimizer=RMSprop(), metrics=['accuracy'])

    return model
if __name__ == '__main__':
    main()