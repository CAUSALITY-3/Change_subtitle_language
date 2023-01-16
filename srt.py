from googletrans import Translator

translator = Translator()

# provide file name with location 
file1 = open('input_file.srt', 'r',encoding="utf-8")  
Lines = file1.readlines()
file1.close()
# provide output file name with location 
file2 = open('output_file.srt', 'w', encoding="utf-8")
for i in Lines:
    
    try:
        try:
            if (type(int(i))==int):
                file2.write(i)
        except:
            if ('-->' in i):
                file2.write(i)
            else:
                translated = translator.translate(i, src='en', dest='ml') #source language = en (English) and destination/output language = ml (malayalam) or take your own.
                file2.write(f"{translated.text} \n")
    except:
        file2.write(i)

file2.close()