# 📘 Prompt Engineering Notes

## 1. What is an LLM?
- An **LLM (Large Language Model)** is trained on massive amounts of data.  
- It works by predicting the next word in a sequence, based on probability.  
- Example: When typing in Google search or messaging apps, you get word suggestions — this is similar to how LLMs function.  
- When you provide input, the model tries to generate the most probable sequence of words as output.  

---

## 2. Chain of Thought (CoT)
- **Definition**: A reasoning method for LLMs.  
- Helps the model break down a complex problem into smaller steps.  
- Improves accuracy by allowing the model to “think step by step.”  

---

## 3. ReAct Prompting
- **ReAct = Reasoning + Acting**  
- The model not only reasons but also takes actions step by step.  
- Useful for tasks where breaking down the problem and taking intermediate actions lead to better results.  

---

## 4. Writing a Good Prompt
A good prompt should have:  
1. **Context** → Provide necessary background.  
2. **Clarity** → Clear and unambiguous instructions.  
3. **Iterative Refinement** → Improve the prompt based on results.  
4. **Input Data** → Can be text, image, or other formats.  
5. **Output Signal** → Indicate the type of response needed (summary, explanation, list, etc.).  

---

## 5. Zero-Shot Prompting
- **Definition**: Asking the model to perform a task **without providing examples**.  
- Scope is limited since the model must rely only on the given question.  
- Example:  
  - Prompt: *“List 5 cities to visit in Europe.”*  
  - No examples or context are given beforehand.  

---

## 6. Few-Shot Prompting
- **Definition**: Providing a **few examples** before asking the model to perform the task.  
- Helps the model understand exactly what kind of output you expect.  
- Example:  
  - Prompt:  
    ```
    Translate English to Spanish:  
    1. Sea otter → nutria de mar  
    2. Cheese → queso  
    ```  
  - Now the model follows the given examples when translating.  

---

## 7. Components of a Prompt
A prompt is made of:  
1. **Instruction** → Tells the model what task to perform.  
2. **Context** → Provides additional information.  
3. **Input Data** → The actual content (text, image, etc.).  
4. **Output Indicator** → The format or type of result you want.  

│── README.md   # Main notes (theory + examples)
│── images/     # Store handwritten reference images
│── examples/   # Code or JSON prompt examples
```
