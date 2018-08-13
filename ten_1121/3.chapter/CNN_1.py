from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np

# 카데고리 지정하기
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)

# 이미지 크기 지정하기
image_w = 64
image_h = 64

# 데이터 열기
X_train, X_test, Y_train, Y_test = np.load("./image/5obj.npy")

# 데이터 정규화하기
X_train = X_train.astype("float") / 256
X_test = X_test.astype("float") / 256
print('X_train shape:', X_train.shape)

model = Sequential()
model.add(Convolution2D(32, (3, 3), padding='same', input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Convolution2D(64, (3, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# 모델 훈련하기
model.fit(X_train, Y_train, batch_size=32, epochs=50)

# # 모델 평가하기
# score = model.evaluate(X_test,Y_test)
# print('loss=', score[0])
# print('accuracy=',score[1])

# 모델 평가하기
pre = model.predict(X_test)
for i, v in enumerate(pre):
    pre_ans = v.argmax()
    ans = Y_test[i].argmax()
    dat = X_test[i]
    if ans == pre_ans:
        continue

    print("[NG]", categories[pre_ans], "!=", categories[ans])
    print(v)
    if not os.path.exists("./image/error"):
        os.mkdir("./image/error")
    fname = "image/error/" + str(i) + "-" + categories[pre_ans] + "-ne-" + categories[ans] + ".png"
    dat *= 256
    img = Image.fromarray(np.unit8(dat))
    img.save(fname)

score = model.evaluate(X_test, Y_test)
print('loss=', score[0])
print('accuracy=', score[1])
