import gradio as gr

# Basit bir greet fonksiyonu oluşturuyoruz
def greet(name):
    return "Hello, " + name + "!"

# Gradio arayüzünü başlatıyoruz
gr.Interface(fn=greet, inputs="text", outputs="text").launch(share=True, debug=True)
