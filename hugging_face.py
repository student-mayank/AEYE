from transformers import pipeline

def Img2Text(url):
    image_to_text = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    
    text = image_to_text(url)[0]['generated_text']
    print(text)
    return text