from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout,Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils
from sklearn.cross_validation import train_test_split
import numpy as np

# optimizers - 학습에 대한 것을 제공, 최적화(최적경로 접근)을(를) 위한 방법들을 갖고 있음
# p.189 참고

image_w = 28
image_h = 28
nb_classes = 10

def main():
    # 폰트 이미지 데이터 읽기
    xy = np.load("./image/font_draw.npz")
    X = xy["x"]
    Y = xy["y"]

    # 데이터 정규화하기
    X = X.reshape(X.shape[0], image_w * image_h).astype('float32')
    X/= 255
    Y = np_utils.to_categorical(Y, 10)

    # 학습 전용 데이터와 테스트 전용 데이터 나누기
    X_train,X_test,y_train,y_test = train_test_split(X,Y)
    # 모델 구축하기
    model = build_model()
    model.fit(X_train,y_train,
              batch_size=128, epochs=20, verbose=1,
              validation_data=(X_test,y_test))
    # 모델 저장하기
    model.save_weights('font_draw.hdf5')

    # 모델 평가하기
    score = model.evaluate(X_test,y_test,verbose=0)
    print('score=',score)

def build_model():
    # MLP 모델 구축
    model = Sequential()
    model.add(Dense(512,input_shape=(784,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(512))

    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10))

    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer=RMSprop(),
                  metrics=['accuracy'])
    return model

if __name__ == '__main__':
    main()