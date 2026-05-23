from transformers import pipeline

# 加载翻译模型
# 这里先使用一个示例模型
# 后面你可以替换成自己的壮语模型

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-zh-en"
)

def translate_text(text: str):
    result = translator(text)

    return result[0]['translation_text']