import pathlib
from tkinter import filedialog as fd
from pydub import AudioSegment
from pathlib import Path


sound = AudioSegment.empty()
filepath = fd.askopenfilename()
filename = Path(filepath).stem
extension = pathlib.Path(filepath).suffix.replace('.', '')
command = 'sound=AudioSegment.from_' + extension + '("' + filepath + '")'
exec(command)
save_path = fd.askdirectory()

# TO DO Take format from user
sound.export(
    save_path + "/" + filename + '.flac',
    format='flac'
)

