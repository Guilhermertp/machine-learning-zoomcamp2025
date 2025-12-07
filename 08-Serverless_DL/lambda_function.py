import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

# ---------------- Initialization ----------------
preprocessor = create_preprocessor('xception', target_size=(299, 299))
interpreter = tflite.Interpreter(model_path='clothing-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

classes = [
    'dress', 'hat', 'longsleeve', 'outwear', 'pants',
    'shirt', 'shoes', 'shorts', 'skirt', 't-shirt'
]

# ---------------- Prediction ----------------
def predict(url):
    X = preprocessor.from_url(url)
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    float_predictions = [float(p) for p in preds[0]]  # JSON-safe
    return dict(zip(classes, float_predictions))

# ---------------- Lambda handler ----------------
def lambda_handler(event, context):
    try:
        url = event['url']
        return predict(url)
    except KeyError:
        return {"error": "No 'url' key in event"}
    except Exception as e:
        return {"error": str(e)}
