import os
import numpy as np
import gradio as gr


def flip_text(x):
    return x[::-1]


def flip_image(x):
    return np.fliplr(x)


with gr.Blocks() as demo:
    gr.Markdown("Flip text or image files using this demo.")
    with gr.Tab("Flip Text"):
        text_input = gr.Textbox()
        text_output = gr.Textbox()
        text_button = gr.Button("Flip")
    with gr.Tab("Flip Image"):
        with gr.Row():
            image_input = gr.Image()
            image_output = gr.Image()
        image_button = gr.Button("Flip", elem_classes=["special-button"])

    with gr.Accordion("Open for More!"):
        gr.Markdown("Look at me...")

    text_button.click(
        flip_text, inputs=text_input, outputs=text_output, api_name="text-flipper"
    )
    image_button.click(
        flip_image, inputs=image_input, outputs=image_output, api_name="image-flipper"
    )

demo.launch(share=False, debug=True, server_port=8050, server_name="0.0.0.0")