import os, shutil, sys

text_extension = {'.txt'}
code_extension = {'.c','.cpp','.java','.python','.js','.ts','.jsx','.css'}
binary_extension = {'.class','.exe','.jar'}
video_extension = {'.mp4','.flv','.mov','.mkv','.m3u8'}
audio_extension = {'.mp3','.m4a','.flac'}
doc_extension = {'.doc','.docx','.xls','.ppt','.pptx','.pdf'}
img_extension = {'.jpg','.jpeg','.png','.bmp'}
compressed_extension = {'.zip','.rar','.7z'}

print('Organising folder : '+sys.argv[1])
directory=sys.argv[1]

for filename in os.listdir(directory):
    file_prefix, file_extension = os.path.splitext(filename)
    if(file_extension in text_extension or file_extension.lower() in text_extension):
        os.makedirs(os.path.dirname(directory+'\\text\\'+filename), exist_ok=True)
        shutil.move(directory+'/'+filename,directory+'/text/'+filename)

    elif(file_extension in img_extension or file_extension.lower() in img_extension):
        os.makedirs(os.path.dirname(directory+'\\images\\'+filename), exist_ok=True)
        shutil.move(directory+'/'+filename,directory+'/images/'+filename)

    elif(file_extension in code_extension or file_extension.lower() in code_extension):
        os.makedirs(os.path.dirname(directory+'\\code\\'+filename), exist_ok=True)
        shutil.move(directory+'/'+filename,directory+'/code/'+filename)

    elif(file_extension in binary_extension or file_extension.lower() in binary_extension):
        os.makedirs(os.path.dirname(directory+'\\binaries\\'+filename), exist_ok=True)
        shutil.move(directory+'/'+filename,directory+'/binaries/'+filename)

    elif(file_extension in video_extension or file_extension.lower() in video_extension):
        os.makedirs(os.path.dirname(directory+'\\videos\\'+filename), exist_ok=True)
        shutil.move(directory+'/'+filename,directory+'/videos/'+filename)

    elif(file_extension in audio_extension or file_extension.lower() in audio_extension):
        os.makedirs(os.path.dirname(directory+'\\audio\\'+filename), exist_ok=True)
        shutil.move(directory+'/'+filename,directory+'/audio/'+filename)

    elif(file_extension in doc_extension or file_extension.lower() in doc_extension):
        os.makedirs(os.path.dirname(directory+'\\docs\\'+filename), exist_ok=True)
        shutil.move(directory+'/'+filename,directory+'/docs/'+filename)

    elif(file_extension in compressed_extension or file_extension.lower() in compressed_extension):
        os.makedirs(os.path.dirname(directory+'\\compressed\\'+filename), exist_ok=True)
        shutil.move(directory+'/'+filename,directory+'/compressed/'+filename)
