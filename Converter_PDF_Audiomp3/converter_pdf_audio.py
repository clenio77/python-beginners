from gtts import gTTS
import PyPDF2

# Function to read pdf document
def pdf_to_text(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

    return text

# Function to transform text in audio
def text_to_audio(text, output_file):
    tts = gTTS(text)        
    tts.save(output_file)

#example usage:
pdf_file = "sql.pdf"
output_audio_file = "sql_audio.mp3"

text = pdf_to_text(pdf_file)
text_to_audio(text, output_audio_file)


    