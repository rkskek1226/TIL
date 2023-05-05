# 그래프(tf.Graph) : 텐서 계산이 Tensorflow 그래프로 실행되는 것
# 그래프는 파이썬 외부에서 이식을 가능하게 하며 성능이 더 우수한 경향이 있음
# 계산의 단위를 나타내는 tf.Operation 객체와 데이터의 단위를 나타내는 tf.Tensor 객체를 포함함
# Function : Tensorflow 그래프를 빌드하는 파이썬 callable
# tf.function은 일반 함수를 입력으로 받아 Function을 반환
# tf.function은 AutoGraph(tf.autograph) 라이브러리를 사용해 파이썬 코드를 그래프 생성 코드로 변환함


import tensorflow as tf
import timeit
from datetime import datetime


def regular_function(w, x, b):
    return tf.matmul(w, x) + b


x = tf.constant([[1., 2.]])
w = tf.constant([[2.], [3.]])
b = tf.constant(4.)

origin_value = regular_function(w, x, b).numpy()
function_that_uses_graph = tf.function(regular_function)

tf_function_value = function_that_uses_graph(w, x, b).numpy()
print(origin_value == tf_function_value)



@tf.function
def get_MSE1(y, y_pred):
    tmp = tf.pow(y - y_pred, 2)
    return tf.reduce_mean(tmp)


y = tf.random.uniform(shape=(5, ), maxval=10, dtype=tf.int32)
y_pred = tf.random.uniform(shape=(5, ), maxval=10, dtype=tf.int32)
print(y)
print(y_pred)
print(get_MSE1(y, y_pred))

tf.config.run_functions_eagerly(True)   # 즉시 실행 모드 ON
print(get_MSE1(y, y_pred))
tf.config.run_functions_eagerly(False)   # 즉시 실행 모드 OFF
print()


@tf.function
def get_MSE2(y, y_pred):
    print("Calculating MSE")
    tmp = tf.pow(y - y_pred, 2)
    return tf.reduce_mean(tmp)


# print()문이 1번만 실행됨(tf.print()를 사용하면 모두 출력됨)
# 트레이싱이라는 프로세스를 통해 그래프가 생성되는데 파이썬 코드를 다시 실행하지는 않음
get_MSE2(y, y_pred)
get_MSE2(y, y_pred)
get_MSE2(y, y_pred)
print()

tf.config.run_functions_eagerly(True)
get_MSE2(y, y_pred)
get_MSE2(y, y_pred)
get_MSE2(y, y_pred)
print()








