# Knowledge Distillation of Zero-Shot Labels for Image Classification

This project is a proof of concept in training a basic classifier algorithm using a more expensive generalist algorithm. Training should be cheaper than paying humans to label a training dataset for a classifier, while the trained model will be cheaper to run than the generalist model.

Specifically, I aim to leverage the emergent zero-shot labeling capabilities of a modern text-image transformer model to perform binary image classification, and then use a teacher-student model to distill the transformer model's knowledge in this specific domain.

I will be using OpenAI's [CLIP model](https://huggingface.co/openai/clip-vit-large-patch14) for its well-documented zero-shot labeling capability.

The goal of this project is to demonstrate the ability to use zero-shot methods to more cheaply and quickly develop classification models without the performance costs of evaluating highly complex machine learning models.

## Project Roadmap

1. Evaluate appropriate models for this experiment.

2. Demonstrate knowledge distillation of zero-shot labels for image classification. **I am here.**

3. Compare the training cost, performance, and accuracy of this method versus zero-shot labeling alone.

4. Compare the training cost and accuracy of this method versus a traditional supervised image classification model.

5. If comparisons are favorable, propose possible use cases for this technique. If comparisons are unfavorable, determine why and propose future research into similar topics.

6. Ensure project code is well documented and the experiment is reproducible.