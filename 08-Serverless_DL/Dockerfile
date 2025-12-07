FROM public.ecr.aws/lambda/python:3.10

# Install compatible NumPy first
RUN pip install --no-cache-dir "numpy<2"

# Install keras-image-helper
RUN pip install --no-cache-dir keras-image-helper

# Install TFLite runtime compiled against Python 3.10 and Linux x86_64
RUN pip install --no-cache-dir \
    https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

# Copy model and Lambda function
COPY clothing-model.tflite .
COPY lambda_function.py .

# Lambda handler
CMD ["lambda_function.lambda_handler"]
