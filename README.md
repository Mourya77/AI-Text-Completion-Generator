# 🚀 AI Text Completion Generator

Generate creative text continuations using GPT-2 or GPT-Neo. Includes a Gradio UI for easy interaction.
A powerful text generation tool using GPT-2/GPT-Neo models with customizable creativity controls and Gradio UI.

## Features
- Dual Model Support: Compare outputs from GPT-2 (fast) and GPT-Neo (high-quality)
- Customizable Generation:
  - Adjust output length (10-100 tokens)
  - Control creativity with temperature (0.1-1.5)
- User-Friendly Interface: Gradio web app for easy interaction
- Colab Ready: One-click run in Google Colab with free GPU

## Requirements
transformers>=4.28.1
gradio>=3.23.0
torch>=2.0.0

## Usage
python text_completion.py
Then open http://localhost:7860 in your browser.

**Try Sample Prompts**
-"The future of AI will..."
-"In a magical forest..."
-"Quantum computing can..."

**🧠 Models Used**
Model	        Parameters	  Best For

GPT-2	        117M	        Fast generations
GPT-Neo       125M          Creative writing
