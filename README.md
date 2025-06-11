# LLM Models that can Visualize images
# 🧠 Vision-Capable Large Language Models (LLMs)

This repository lists **Large Language Models (LLMs) with visual capabilities**, i.e., models that can interpret, reason over, or generate responses based on **images, charts, documents**, and other visual data.

## 📋 Multimodal LLMs with Vision Support

| Model Name | Developer | Vision Features | Open/Closed | Notes |
|------------|-----------|------------------|--------------|-------|
| **GPT-4o** | OpenAI | Vision (images, charts, documents) | Closed-source | Integrated into ChatGPT (Plus/Pro); supports image input |
| **Gemini 1.5 Pro** | Google DeepMind | Vision (image, diagrams, screenshots, etc.) | Closed-source | Used in Google AI Studio, Gemini app |
| **Claude 3 Opus** | Anthropic | Vision (images, documents) | Closed-source | Available via Claude.ai (paid tier) |
| **LLaVA** | UC Berkeley et al. | Image understanding, QA, captioning | Open-source | Fine-tuned from Vicuna + CLIP/BLIP |
| **LLaVA-1.5 / LLaVA-Next** | Community | Improved LLaVA | Open-source | Higher accuracy on visual benchmarks |
| **MiniGPT-4** | Community | Image captioning, reasoning | Open-source | Lightweight and easy to fine-tune |
| **Qwen-VL / Qwen-VL-Chat** | Alibaba | Image captioning, OCR, QA | Open-source | Strong multilingual and visual reasoning |
| **InternVL / InternGPT** | Shanghai AI Lab | Visual grounding, reasoning | Open-source | Supports visual instruction-following |
| **Fuyu** | Adept AI | Native multimodal transformer | Closed-source | Designed from scratch for V+L tasks |
| **IDEFICS** | Hugging Face | Captioning, multimodal generation | Open-source | Supports large multimodal datasets |
| **GIT / GIT2** | Microsoft | General image-text understanding | Open-source | Versatile visual encoder-decoder |
| **Kosmos-2** | Microsoft | Visual QA, grounding, OCR | Open-source | Capable of spatial and visual reasoning |
| **BLIP / BLIP-2** | Salesforce | VQA, captioning | Open-source | Strong visual encoder + language model |
| **Flamingo / Flamingo-80B** | DeepMind | Few-shot visual reasoning | Closed-source | Multimodal prompting enabled |
| **PaLI / PaLI-X** | Google | Multilingual vision-language reasoning | Closed-source | Scales up to 500B+ parameters |
| **Owl-ViT / OWL-ViT2** | Google Research | Object detection via text prompts | Open-source | Great for open-vocabulary detection |

---

## 🧠 Common Capabilities

- Visual Question Answering (VQA)
- Image Captioning
- OCR (Text in Images)
- Scene and Diagram Understanding
- Image-based Reasoning (memes, charts, UI)
- Multilingual Visual-Language Tasks

---

## ✅ Recommended Open-Source Models to Try Locally

- [LLaVA-1.5](https://github.com/haotian-liu/LLaVA)
- [MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4)
- [Qwen-VL](https://huggingface.co/Qwen/Qwen-VL-Chat)
- [BLIP-2](https://github.com/salesforce/BLIP)
- [InternVL](https://github.com/OpenGVLab/InternVL)

All of the above are available via Hugging Face or GitHub, and can be run locally with a GPU.

---

## 📢 Contributions

If you know of any other **multimodal models** with visual support, feel free to open a PR or issue!

